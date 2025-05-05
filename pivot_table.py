import streamlit as st
import pandas as pd

def display_pivot_table(df):
    st.title("📊 Pivot Table and Filtering")

    if df.empty:
        st.warning("The uploaded DataFrame is empty. Please upload valid data.")
        return

    # Initialize filtered data in session
    if 'filtered_df' not in st.session_state:
        st.session_state.filtered_df = df.copy()

    # Reset Filters function
    def reset_filters():
        st.session_state.filtered_df = df.copy()
        for col in df.columns:
            if f"{col}_filter" in st.session_state:
                del st.session_state[f"{col}_filter"]
            if f"{col}_range" in st.session_state:
                del st.session_state[f"{col}_range"]
            keys_to_delete = [k for k in st.session_state if k.startswith(f"{col}_") and k.endswith("_chk")]
            for key in keys_to_delete:
                del st.session_state[key]

    # Reset Filters button
    if st.button("🔄 Reset All Filters"):
        reset_filters()

    st.markdown("### 🔍 Select Column(s) to Filter")
    filter_columns = st.multiselect("Select column(s)", df.columns.tolist(), key="multi_filter_selector")

    # Start filtering
    filtered_df = df.copy()

    for col in filter_columns:
        st.markdown(f"#### ✏️ Filter for: `{col}`")

        if df[col].dtype == 'object' or df[col].dtype.name == 'category':
            unique_vals = sorted(df[col].dropna().unique().tolist())
            default_vals = st.session_state.get(f"{col}_filter", unique_vals)

            search_query = st.text_input(f"🔎 Search in {col}", key=f"{col}_search")
            filtered_vals = [val for val in unique_vals if search_query.lower() in str(val).lower()]

            if st.button("🚫 Unselect All", key=f"{col}_unselect"):
                for val in filtered_vals:
                    st.session_state[f"{col}_{val}_chk"] = False
                st.session_state[f"{col}_filter"] = []

            selected_vals = []
            for val in filtered_vals:
                is_selected = st.checkbox(
                    f"{val}",
                    value=st.session_state.get(f"{col}_{val}_chk", val in default_vals),
                    key=f"{col}_{val}_chk"
                )
                if is_selected:
                    selected_vals.append(val)

            st.session_state[f"{col}_filter"] = selected_vals
            filtered_df = filtered_df[filtered_df[col].isin(selected_vals)]

    # Save filtered data
    st.session_state.filtered_df = filtered_df

    # Display filtered data
    st.markdown("### 📄 Filtered Data")
    st.dataframe(filtered_df)

        # Pivot table controls (based on original df, not filtered)
    st.markdown("### 🔧 Pivot Table Setup")

    rows = st.multiselect("Rows", df.columns.tolist(), key="rows_selector")
    cols = st.multiselect("Columns", df.columns.tolist(), key="cols_selector")
    values = st.multiselect("Values", df.columns.tolist(), key="values_selector")

    aggfunc = st.selectbox("Aggregation", ['sum', 'mean', 'count', 'first', 'last'], key="agg_selector")

# ⚠️ Warning for incompatible aggregation
    if aggfunc in ['sum', 'mean']:
        st.warning("Note: If a user selects a non-numeric column as a 'Value' and chooses 'sum' or 'mean', it may cause errors or return unexpected results.")


    if rows and values:
        try:
            pivot_df = pd.pivot_table(
                filtered_df,
                index=rows,
                columns=cols if cols else None,
                values=values,
                aggfunc=aggfunc,
                fill_value=0,
                margins=True
            )
            st.subheader("📊 Pivot Table")
            st.dataframe(pivot_df)
            st.download_button("Download Pivot Table", pivot_df.to_csv().encode(), "pivot_table.csv", "text/csv")
        except Exception as e:
            st.error(f"❌ Error creating pivot table: {e}")
