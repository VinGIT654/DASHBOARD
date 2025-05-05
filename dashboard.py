import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import traceback

# File uploader and data loader
def load_data():
    st.sidebar.title("📁 Upload Your Data")
    uploaded_file = st.sidebar.file_uploader("Upload Excel or CSV file", type=['csv', 'xlsx'])

    if uploaded_file:
        try:
            file_size = uploaded_file.size
            st.sidebar.caption(f"File size: {round(file_size / 1024**2, 2)} MB")

            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file, engine='openpyxl')
            else:
                st.sidebar.error("Unsupported file type.")
                return None

            return df

        except Exception as e:
            st.sidebar.error(f"Failed to load file: {str(e)}")
            st.sidebar.code(traceback.format_exc())
            return None
    return None

# Plot Tree Map
def plot_tree_map(df):
    numeric_cols = df.select_dtypes(include='number').columns
    categorical_cols = df.select_dtypes(include='object').columns

    # Check if there are valid numeric columns and categorical columns
    if len(numeric_cols) >= 1 and len(categorical_cols) >= 1:
        try:
            # Use the first categorical column for path and first numeric column for values
            fig = px.treemap(df, path=[categorical_cols[0]], values=numeric_cols[0])
            st.plotly_chart(fig)
        except Exception as e:
            st.error(f"❌ Error creating Treemap: {str(e)}")
    else:
        st.warning("⚠️ Cannot create Treemap. Ensure there is at least one categorical and one numeric column.")


# Plot Pie Chart
def plot_pie_chart(df):
    categorical_cols = df.select_dtypes(include='object').columns
    numeric_cols = df.select_dtypes(include='number').columns
    if len(categorical_cols) > 0 and len(numeric_cols) > 0:
        data = df[[categorical_cols[0], numeric_cols[0]]].groupby(categorical_cols[0]).sum().reset_index()
        fig = px.pie(data, names=categorical_cols[0], values=numeric_cols[0])
        st.plotly_chart(fig)

# Plot Boxplot
def plot_boxplot(df):
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) >= 2:
        fig = px.box(df, x=numeric_cols[0], y=numeric_cols[1])
        st.plotly_chart(fig)

# Plot Scatter Plot
def plot_scatter(df):
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) >= 2:
        fig = px.scatter(df, x=numeric_cols[0], y=numeric_cols[1], title="Scatter Plot")
        st.plotly_chart(fig)

# Pivot Table
def show_pivot_table(df):
    try:
        categorical_cols = df.select_dtypes(include='object').columns
        numeric_cols = df.select_dtypes(include='number').columns
        if len(categorical_cols) > 0 and len(numeric_cols) > 0:
            pivot_df = pd.pivot_table(df, index=categorical_cols[0], values=numeric_cols[0], aggfunc='sum')
            st.dataframe(pivot_df)
    except Exception:
        st.warning("⚠️ Pivot table could not be created due to memory constraints or incompatible columns.")

# Show Column Info
def show_column_info(df):
    st.subheader("🧾 Data Columns Info")
    st.write("Columns and their types:")
    st.dataframe(pd.DataFrame({'Column': df.columns, 'Type': df.dtypes}))

# Main Dashboard
def show_dashboard(df):
    st.title("Dashboard Overview")

    if df is None or df.empty:
        st.warning("No data available.")
        return

    try:
        show_column_info(df)

        st.subheader("🔍 Preview of Data")
        st.dataframe(df.head(10))

        # Estimate memory usage
        try:
            df_memory = df.memory_usage(deep=True).sum()
        except Exception:
            df_memory = 0

        threshold = 10 * 1024 * 1024  # 10 MB
        large_data = df_memory > threshold or len(df) > 10000

        # Add a loading spinner for large files
        if large_data:
            st.warning("⚠️ Large file detected. Visualizations are based on a 50-row sample.")
            df_sample = df.sample(n=50, random_state=1) if len(df) > 50 else df.copy()
        else:
            df_sample = df.copy()

        with st.spinner('Processing data for visualizations...'):
            # Show Charts & Pivot Table
            plot_pie_chart(df_sample)
            plot_scatter(df_sample)
            plot_tree_map(df_sample)
            plot_boxplot(df_sample)
            show_pivot_table(df_sample)

    except Exception:
        st.error("❌ Error displaying dashboard:")
        st.code("".join(traceback.format_exception(*sys.exc_info())), language="python")

# Main function to run the app
if __name__ == "__main__":
    df = load_data()
    if df is not None:
        show_dashboard(df)



