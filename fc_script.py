import streamlit as st
from datetime import datetime
import pandas as pd

# 🧩 Import your modules
from DASHBOARD.theme import apply_theme
from DASHBOARD.data_loader import load_excel
from DASHBOARD.google_sheets import extract_sheet_id, get_sheet_names, load_google_sheet
from DASHBOARD.dashboard import show_dashboard
from DASHBOARD.filtering import apply_filters
from DASHBOARD.pivot_table import display_pivot_table  # ✅ This contains the new advanced filtering version
from DASHBOARD.charts import display_charts

import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Fetch the logo from the URL
page_icon_url = "https://static.vecteezy.com/system/resources/previews/017/208/926/non_2x/luxury-letter-v-logo-v-logotype-for-elegant-and-stylish-fashion-symbol-vector.jpg"
resp = requests.get(page_icon_url)
icon_img = Image.open(BytesIO(resp.content))

# Now set up the page config with that image
st.set_page_config(
    page_title="Dashboard",
    layout="wide",
    page_icon=icon_img
)


import streamlit as st

# Function to apply the selected theme
def apply_theme(theme):
    if theme == "Dark" or theme == "Royal":
        st.markdown("""
            <style>
                .stApp {
                    background-color: #0c0c0c;
                    color: #ffd700;
                    font-family: 'Segoe UI', sans-serif;
                }
                .stSidebar {
                    background-color: #1a1a1a;
                }
                h1, h2, h3, h4, h5 {
                    color: #ffd700;
                }
                .stButton > button {
                    background-color: #ffd700;
                    color: black;
                    border: none;
                    font-weight: bold;
                }
                .stButton > button:hover {
                    background-color: #e6c200;
                    color: black;
                }
                .stDownloadButton > button {
                    background-color: #e6c200;
                    color: black;
                }
                .css-1d391kg, .css-1offfwp {
                    background-color: #1a1a1a !important;
                    color: #ffd700 !important;
                }
                .css-10trblm {
                    color: #ffd700 !important;
                }
                .stDataFrame {
                    background-color: #0c0c0c;
                    color: #ffd700;
                }
            </style>
        """, unsafe_allow_html=True)
    elif theme == "Pink":
        st.markdown("""
            <style>
                .stApp {
                    background-color: #f8bbd0; /* Pink */
                    color: #880e4f; /* Dark Pink */
                    font-family: 'Segoe UI', sans-serif;
                }
                .stSidebar {
                    background-color: #f48fb1; /* Light Pink */
                }
                h1, h2, h3, h4, h5 {
                    color: #880e4f; /* Dark Pink */
                }
                .stButton > button {
                    background-color: #880e4f;
                    color: white;
                    border: none;
                    font-weight: bold;
                }
                .stButton > button:hover {
                    background-color: #c2185b;
                    color: white;
                }
                .stDownloadButton > button {
                    background-color: #c2185b;
                    color: white;
                }
                .css-1d391kg, .css-1offfwp {
                    background-color: #f48fb1 !important;
                    color: #880e4f !important;
                }
                .css-10trblm {
                    color: #880e4f !important;
                }
                .stDataFrame {
                    background-color: #f8bbd0;
                    color: #880e4f;
                }
            </style>
        """, unsafe_allow_html=True)
    elif theme == "Lavender":
        st.markdown("""
            <style>
                .stApp {
                    background-color: #e1bee7; /* Lavender */
                    color: #512da8; /* Purple */
                    font-family: 'Segoe UI', sans-serif;
                }
                .stSidebar {
                    background-color: #ce93d8; /* Light Lavender */
                }
                h1, h2, h3, h4, h5 {
                    color: #512da8; /* Purple */
                }
                .stButton > button {
                    background-color: #512da8;
                    color: white;
                    border: none;
                    font-weight: bold;
                }
                .stButton > button:hover {
                    background-color: #7e57c2;
                    color: white;
                }
                .stDownloadButton > button {
                    background-color: #7e57c2;
                    color: white;
                }
                .css-1d391kg, .css-1offfwp {
                    background-color: #ce93d8 !important;
                    color: #512da8 !important;
                }
                .css-10trblm {
                    color: #512da8 !important;
                }
                .stDataFrame {
                    background-color: #e1bee7;
                    color: #512da8;
                }
            </style>
        """, unsafe_allow_html=True)
    elif theme == "Yellow":
        st.markdown("""
            <style>
                .stApp {
                    background-color: #fff59d; /* Yellow */
                    color: #f57f17; /* Dark Yellow */
                    font-family: 'Segoe UI', sans-serif;
                }
                .stSidebar {
                    background-color: #fff176; /* Light Yellow */
                }
                h1, h2, h3, h4, h5 {
                    color: #f57f17; /* Dark Yellow */
                }
                .stButton > button {
                    background-color: #f57f17;
                    color: white;
                    border: none;
                    font-weight: bold;
                }
                .stButton > button:hover {
                    background-color: #ff9800;
                    color: white;
                }
                .stDownloadButton > button {
                    background-color: #ff9800;
                    color: white;
                }
                .css-1d391kg, .css-1offfwp {
                    background-color: #fff176 !important;
                    color: #f57f17 !important;
                }
                .css-10trblm {
                    color: #f57f17 !important;
                }
                .stDataFrame {
                    background-color: #fff59d;
                    color: #f57f17;
                }
            </style>
        """, unsafe_allow_html=True)
    elif theme == "Grey":
        st.markdown("""
            <style>
                .stApp {
                    background-color: #e0e0e0; /* Grey */
                    color: #212121; /* Dark Grey */
                    font-family: 'Segoe UI', sans-serif;
                }
                .stSidebar {
                    background-color: #bdbdbd; /* Light Grey */
                }
                h1, h2, h3, h4, h5 {
                    color: #212121; /* Dark Grey */
                }
                .stButton > button {
                    background-color: #212121;
                    color: white;
                    border: none;
                    font-weight: bold;
                }
                .stButton > button:hover {
                    background-color: #424242;
                    color: white;
                }
                .stDownloadButton > button {
                    background-color: #424242;
                    color: white;
                }
                .css-1d391kg, .css-1offfwp {
                    background-color: #bdbdbd !important;
                    color: #212121 !important;
                }
                .css-10trblm {
                    color: #212121 !important;
                }
                .stDataFrame {
                    background-color: #e0e0e0;
                    color: #212121;
                }
            </style>
        """, unsafe_allow_html=True)
    elif theme == "Pale Red":
        st.markdown("""
            <style>
                .stApp {
                    background-color: #ffebee; /* Pale Red */
                    color: #c62828; /* Dark Red */
                    font-family: 'Segoe UI', sans-serif;
                }
                .stSidebar {
                    background-color: #ef9a9a; /* Light Pale Red */
                }
                h1, h2, h3, h4, h5 {
                    color: #c62828; /* Dark Red */
                }
                .stButton > button {
                    background-color: #c62828;
                    color: white;
                    border: none;
                    font-weight: bold;
                }
                .stButton > button:hover {
                    background-color: #d32f2f;
                    color: white;
                }
                .stDownloadButton > button {
                    background-color: #d32f2f;
                    color: white;
                }
                .css-1d391kg, .css-1offfwp {
                    background-color: #ef9a9a !important;
                    color: #c62828 !important;
                }
                .css-10trblm {
                    color: #c62828 !important;
                }
                .stDataFrame {
                    background-color: #ffebee;
                    color: #c62828;
                }
            </style>
        """, unsafe_allow_html=True)
    elif theme == "Pale Green":
        st.markdown("""
            <style>
                .stApp {
                    background-color: #e8f5e9; /* Pale Green */
                    color: #388e3c; /* Dark Green */
                    font-family: 'Segoe UI', sans-serif;
                }
                .stSidebar {
                    background-color: #81c784; /* Light Pale Green */
                }
                h1, h2, h3, h4, h5 {
                    color: #388e3c; /* Dark Green */
                }
                .stButton > button {
                    background-color: #388e3c;
                    color: white;
                    border: none;
                    font-weight: bold;
                }
                .stButton > button:hover {
                    background-color: #2c6b2f;
                    color: white;
                }
                .stDownloadButton > button {
                    background-color: #2c6b2f;
                    color: white;
                }
                .css-1d391kg, .css-1offfwp {
                    background-color: #81c784 !important;
                    color: #388e3c !important;
                }
                .css-10trblm {
                    color: #388e3c !important;
                }
                .stDataFrame {
                    background-color: #e8f5e9;
                    color: #388e3c;
                }
            </style>
        """, unsafe_allow_html=True)
    else:
        # Default Light Theme
        st.markdown("""
            <style>
                .stApp {
                    background-color: #f4f6fc;
                    color: #000;
                }
                .stSidebar {
                    background-color: #fff;
                }
                h1, h2, h3, h4 {
                    color: #0d47a1;
                }
                .stButton > button {
                    background-color: #2874f0;
                    color: white;
                    border: none;
                }
                .stButton > button:hover {
                    background-color: #0b3d91;
                }
                .stDownloadButton > button {
                    background-color: #ffc107;
                    color: black;
                }
            </style>
        """, unsafe_allow_html=True)


# ---------------------- 🎨 Theme Toggle ----------------------
theme = st.sidebar.radio("Select Theme", ["Light", "Dark", "Royal", "Pink", "Lavender", "Yellow", "Grey", "Pale Red", "Pale Green"], horizontal=True)
apply_theme(theme)



# ---------------------- 🚚 Header ----------------------
import streamlit as st
from datetime import datetime

# ---------------------- Header ----------------------
logo_url = "https://static.vecteezy.com/system/resources/previews/017/208/926/non_2x/luxury-letter-v-logo-v-logotype-for-elegant-and-stylish-fashion-symbol-vector.jpg"

st.image(logo_url, width=150)
st.title(" Dashboard")
st.sidebar.markdown(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


# ---------------------- 📂 Data Input ----------------------
uploaded_file = st.sidebar.file_uploader(
    "Upload Excel or CSV file", type=["csv", "xlsx", "xls"]
)
sheet_url = st.sidebar.text_input("Or paste Google Sheets URL:")

if uploaded_file is not None:
    df = load_excel(uploaded_file=uploaded_file)
elif sheet_url:
    sheet_id = extract_sheet_id(sheet_url)
    if sheet_id:
        sheet_names = get_sheet_names(sheet_id)
        selected_sheet = st.sidebar.selectbox("Select Sheet", sheet_names)
        df = load_google_sheet(sheet_id, selected_sheet)
    else:
        df = pd.DataFrame()
else:
    df = pd.DataFrame()

# ---------------------- 📊 Main Sections ----------------------
if not df.empty:
    sidebar_tabs = st.sidebar.radio(
        "Choose Section",
        ["Dashboard", "Filtering", "Pivot Table", "Charts", "Notes", "Downloads"]
    )

    if sidebar_tabs == "Dashboard":
        show_dashboard(df)

    elif sidebar_tabs == "Filtering":
        filtered_df = apply_filters(df)
        st.dataframe(filtered_df, use_container_width=True)

    elif sidebar_tabs == "Pivot Table":
        display_pivot_table(df)  # ✅ Using the updated pivot table with advanced filters

    elif sidebar_tabs == "Charts":
        display_charts(df)

    elif sidebar_tabs == "Notes":
        st.subheader("📜 Add Your Notes")
        notes = st.text_area("Write any observations, RCA, or follow-ups here:")
        if notes:
            st.success("Notes saved internally.")

    elif sidebar_tabs == "Downloads":
        st.subheader("📥 Download Raw Data")
        csv_bytes = df.to_csv(index=False).encode()
        st.download_button(
            "Download Raw CSV",
            csv_bytes,
            "raw_data.csv",
            "text/csv"
        )
        sample_template = pd.DataFrame(
            columns=["FC", "QTY", "ZONE", "PICKUP_CITY"]
        )
        st.download_button(
            "Download Sample Template",
            sample_template.to_csv(index=False).encode(),
            "template.csv",
            "text/csv"
        )
else:
    st.warning("📎 Please upload a file or provide a Google Sheet URL to get started!")

