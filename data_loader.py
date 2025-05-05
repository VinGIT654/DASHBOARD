import pandas as pd
import streamlit as st
import os

@st.cache_data(ttl=600)
def load_excel(file_path=None, uploaded_file=None):
    """
    Load and clean Excel data from a local path or Streamlit upload.

    Args:
        file_path (str): Path to Excel file.
        uploaded_file (UploadedFile): File uploaded via Streamlit.

    Returns:
        pd.DataFrame: Cleaned and type-converted dataframe.
    """
    try:
        if uploaded_file is not None:
            # Check if the uploaded file is an Excel or CSV file
            if uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                # If it's an Excel file
                df = pd.read_excel(uploaded_file, engine="openpyxl")
            elif uploaded_file.type == "text/csv":
                # If it's a CSV file
                df = pd.read_csv(uploaded_file)
            else:
                st.error("Unsupported file type! Please upload an Excel or CSV file.")
                return pd.DataFrame()

        elif file_path and os.path.exists(file_path):
            # Load the file from the local path if specified
            if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                df = pd.read_excel(file_path, engine="openpyxl")
            elif file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            else:
                st.error("Unsupported file format. Please upload a CSV or Excel file.")
                return pd.DataFrame()

        else:
            st.warning("Please provide a valid file.")
            return pd.DataFrame()

        return preprocess_data(df)

    except Exception as e:
        st.error(f"Error loading file: {e}")
        return pd.DataFrame()

def preprocess_data(df):
    """
    Automatically detect and convert data types in the dataframe.

    Args:
        df (pd.DataFrame): Raw dataframe.

    Returns:
        pd.DataFrame: Cleaned dataframe with inferred types.
    """
    try:
        # Strip column names
        df.columns = df.columns.str.strip()
        df.columns = df.columns.str.replace('[^a-zA-Z0-9_ ]', '', regex=True).str.replace(" ", "_")

        for col in df.columns:
            # Try to convert to datetime
            if df[col].dtype == object:
                try:
                    df[col] = pd.to_datetime(df[col], errors='raise')
                except:
                    pass

            # Try to convert to numeric
            try:
                df[col] = pd.to_numeric(df[col], errors='ignore')
            except:
                pass

        # Fill NaNs for consistency
        df.fillna("-", inplace=True)

        return df

    except Exception as e:
        st.error(f"Error processing data: {e}")
        return df

