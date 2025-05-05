# DASHBOARD/filtering.py

import streamlit as st
import pandas as pd
import io
import base64

def apply_filters(df):
    st.markdown("## 🔍 Advanced Data Filtering")
    st.markdown("---")

    # Add subtle CSS for hover and smooth animations
    st.markdown("""
        <style>
            .stDataFrame:hover { transition: 0.3s ease-in-out; box-shadow: 0 0 15px #f5b94288; }
            .filter-box:hover { background-color: #33333322; transition: background 0.3s ease; }
            .filter-label { font-weight: bold; color: gold; margin-top: 0.5em; }
        </style>
    """, unsafe_allow_html=True)

    filter_container = st.container()
    filtered_df = df.copy()

    with filter_container:
        cols = df.columns.tolist()
        selected_cols = st.multiselect("Select columns to filter", cols, default=[])

        for col in selected_cols:
            unique_vals = df[col].dropna().unique().tolist()
            if len(unique_vals) <= 100:
                options = st.multiselect(f"Filter `{col}`", unique_vals, default=unique_vals, key=f"filter_{col}")
                filtered_df = filtered_df[filtered_df[col].isin(options)]

        # Search functionality (for all text columns)
        with st.expander("🔎 Text Search"):
            search_col = st.selectbox("Column to search", df.select_dtypes(include='object').columns.tolist(), key="search_col")
            query = st.text_input("Search term (case-insensitive)", key="search_term")
            if query:
                filtered_df = filtered_df[filtered_df[search_col].str.contains(query, case=False, na=False)]

        # Reset button
        if st.button("🔄 Reset Filters"):
            st.experimental_rerun()

    st.markdown("---")
    st.success(f"Filtered rows: {len(filtered_df)} / {len(df)}")

    return filtered_df

def download_data(df, filename="filtered_data.csv"):
    """
    Creates a download link for a dataframe.
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # encode to base64
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">📥 Download CSV</a>'
    st.markdown(href, unsafe_allow_html=True)

def share_file_button(uploaded_file):
    """
    Simulates a share link if file was uploaded by user.
    """
    if uploaded_file:
        st.info(f"🔗 Share this file manually: `{uploaded_file.name}`")
