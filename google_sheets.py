# DASHBOARD/google_sheets.py

import pandas as pd
import streamlit as st
from urllib.parse import urlparse, parse_qs

@st.cache_data(ttl=600)
def extract_sheet_id(google_sheet_url):
    """
    Extract the Sheet ID from a Google Sheets URL.
    """
    try:
        parsed = urlparse(google_sheet_url)
        if "spreadsheets" not in parsed.path:
            raise ValueError("Invalid Google Sheets URL.")
        return parsed.path.split("/")[3]
    except Exception as e:
        st.error(f"Error extracting Sheet ID: {e}")
        return None

@st.cache_data(ttl=600)
def get_sheet_names(sheet_id):
    """
    Fetch the names of sheets available in the spreadsheet.
    Requires gspread and Google API for full auth. For public sheets, defaults to Sheet1.
    """
    try:
        # For public sheets we can only assume 'Sheet1' unless using API
        return ["Sheet1"]
    except Exception as e:
        st.error(f"Unable to get sheet names: {e}")
        return []

@st.cache_data(ttl=600)
def load_google_sheet(sheet_id, sheet_name="Sheet1"):
    """
    Load a single Google Sheet as DataFrame.
    """
    try:
        # Construct export CSV URL
        csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
        df = pd.read_csv(csv_url)
        return preprocess_data(df)
    except Exception as e:
        st.error(f"Failed to load Google Sheet: {e}")
        return pd.DataFrame()

def preprocess_data(df):
    """
    Automatically clean and infer column types.
    """
    try:
        df.columns = df.columns.str.strip().str.replace('[^a-zA-Z0-9_ ]', '', regex=True).str.replace(" ", "_")

        for col in df.columns:
            if df[col].dtype == object:
                try:
                    df[col] = pd.to_datetime(df[col], errors='raise')
                except:
                    pass

            try:
                df[col] = pd.to_numeric(df[col], errors='ignore')
            except:
                pass

        df.fillna("-", inplace=True)
        return df

    except Exception as e:
        st.error(f"Preprocessing error: {e}")
        return df
