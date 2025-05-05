# DASHBOARD/charts.py

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import base64
import io
from io import BytesIO, StringIO


def display_charts(df):
    """
    Display a variety of interactive charts with download and share options.
    """
    st.subheader("📊 Chart Builder")
    st.markdown("---")

    # CSS for hover animation effect
    st.markdown(
        """
        <style>
        .stPlotlyChart:hover {box-shadow: 0 0 20px #ffd70066; transition: all 0.3s ease;}
        </style>
        """, unsafe_allow_html=True
    )

    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    all_cols = df.columns.tolist()

    chart_type = st.selectbox(
        "Chart Type", [
            "Line", "Bar", "Pie", "Area", "Scatter", "Histogram", "Treemap",
            "Waterfall", "Funnel", "Bubble", "Candlestick", "KPI",
            "Radar", "Pareto", "Sankey"
        ]
    )

    x_axis = st.selectbox("X-Axis", options=all_cols)
    y_axis = st.multiselect("Y-Axis", options=numeric_cols)
    color_by = st.selectbox("Color By (optional)", options=[None] + all_cols)

    if x_axis and y_axis:
        try:
            # Generate the figure
            fig = create_figure(df, chart_type, x_axis, y_axis, color_by)
            fig.update_layout(
                transition_duration=500,
                hovermode='x unified',
                hoverlabel=dict(bgcolor='white', font_size=13)
            )

            # Display chart
            st.plotly_chart(fig, use_container_width=True)

            # Download chart as HTML
            buf_html = StringIO()
            fig.write_html(buf_html)
            html_bytes = buf_html.getvalue().encode()
            st.download_button(
                "📥 Download Chart as HTML", html_bytes,
                "chart.html", mime="text/html"
            )

            # Download chart as PNG
            img_bytes = fig.to_image(format='png')
            st.download_button(
                "📷 Download Chart as PNG", img_bytes,
                "chart.png", mime="image/png"
            )

            # Download underlying chart data as CSV
            data = df[[x_axis] + y_axis].dropna()
            csv_bytes = data.to_csv(index=False).encode()
            st.download_button(
                "📄 Download Chart Data (CSV)", csv_bytes,
                "chart_data.csv", mime="text/csv"
            )

            # Shareable data link (copy this link to share data)
            b64 = base64.b64encode(csv_bytes).decode()
            share_link = f"data:file/csv;base64,{b64}"
            st.markdown(f"🔗 Share Chart Data Link: {share_link}")

        except Exception as e:
            st.error(f"Error rendering chart: {e}")
    else:
        st.info("Please select both X-axis and Y-axis for charting.")


def create_figure(df, chart_type, x_axis, y_axis, color_by):
    """
    Create a Plotly figure based on the specified chart type and axes.
    """
    df_clean = df.dropna(subset=[x_axis] + y_axis)
    melted = df_clean.melt(
        id_vars=[x_axis], value_vars=y_axis,
        var_name='Metric', value_name='Value'
    )

    if chart_type == 'Line':
        return px.line(melted, x=x_axis, y='Value', color=color_by or 'Metric')
    if chart_type == 'Bar':
        return px.bar(melted, x=x_axis, y='Value', color=color_by or 'Metric', barmode='group')
    if chart_type == 'Pie' and len(y_axis) == 1:
        return px.pie(df_clean, names=x_axis, values=y_axis[0], color=color_by)
    if chart_type == 'Area':
        return px.area(melted, x=x_axis, y='Value', color=color_by or 'Metric')
    if chart_type == 'Scatter':
        return px.scatter(melted, x=x_axis, y='Value', color=color_by or 'Metric', size='Value')
    if chart_type == 'Histogram':
        return px.histogram(df_clean, x=x_axis, y=y_axis[0])
    if chart_type == 'Treemap':
        return px.treemap(df_clean, path=[x_axis], values=y_axis[0])
    if chart_type == 'Waterfall':
        return go.Figure(go.Waterfall(x=df_clean[x_axis], y=df_clean[y_axis[0]]))
    if chart_type == 'Funnel':
        return px.funnel(df_clean, x=y_axis[0], y=x_axis)
    if chart_type == 'Bubble':
        return px.scatter(df_clean, x=x_axis, y=y_axis[0], size=y_axis[0])
    if chart_type == 'Candlestick':
        return go.Figure(data=[go.Candlestick(
            x=df_clean[x_axis],
            open=df_clean[y_axis[0]], high=df_clean[y_axis[1]],
            low=df_clean[y_axis[2]], close=df_clean[y_axis[3]]
        )])
    if chart_type == 'KPI':
        return go.Figure(go.Indicator(
            mode='number+delta',
            value=df_clean[y_axis[0]].mean(),
            delta={'reference': df_clean[y_axis[0]].median()}
        ))
    if chart_type == 'Radar':
        fig = go.Figure()
        for col in y_axis:
            fig.add_trace(go.Scatterpolar(
                r=df_clean[col], theta=df_clean[x_axis], fill='toself', name=col
            ))
        return fig
    if chart_type == 'Pareto':
        sorted_df = df_clean.sort_values(by=y_axis[0], ascending=False)
        sorted_df['cum_sum'] = sorted_df[y_axis[0]].cumsum()
        sorted_df['cum_perc'] = 100 * sorted_df['cum_sum'] / sorted_df[y_axis[0]].sum()
        fig = go.Figure()
        fig.add_trace(go.Bar(x=sorted_df[x_axis], y=sorted_df[y_axis[0]]))
        fig.add_trace(go.Scatter(
            x=sorted_df[x_axis], y=sorted_df['cum_perc'], yaxis='y2',
            mode='lines+markers', name='Cumulative %'
        ))
        return fig
    if chart_type == 'Sankey':
        labels = list(df_clean[x_axis].unique())
        return go.Figure(go.Sankey(
            node=dict(label=labels),
            link=dict(
                source=[0]*len(df_clean),
                target=[1]*len(df_clean),
                value=df_clean[y_axis[0]]
            )
        ))
    # Fallback
    return px.bar(melted, x=x_axis, y='Value', color=color_by or 'Metric')
