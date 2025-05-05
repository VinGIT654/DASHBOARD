# DASHBOARD/theme.py

import streamlit as st

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
    elif theme == "Rainbow":
        st.markdown("""
            <style>
                .stApp {
                    background-color: #f1c40f; /* Yellow */
                    color: #2c3e50; /* Dark Blue */
                    font-family: 'Segoe UI', sans-serif;
                }
                .stSidebar {
                    background-color: #9b59b6; /* Purple */
                }
                h1, h2, h3, h4, h5 {
                    color: #3498db; /* Blue */
                }
                .stButton > button {
                    background-color: #3498db;
                    color: white;
                    border: none;
                    font-weight: bold;
                }
                .stButton > button:hover {
                    background-color: #2980b9;
                    color: white;
                }
                .stDownloadButton > button {
                    background-color: #e74c3c; /* Red */
                    color: white;
                }
                .css-1d391kg, .css-1offfwp {
                    background-color: #9b59b6 !important;
                    color: #f1c40f !important;
                }
                .css-10trblm {
                    color: #f1c40f !important;
                }
                .stDataFrame {
                    background-color: #f1c40f;
                    color: #2c3e50;
                }
            </style>
        """, unsafe_allow_html=True)
    elif theme == "Blue":
        st.markdown("""
            <style>
                .stApp {
                    background-color: #3498db;
                    color: #ffffff;
                    font-family: 'Segoe UI', sans-serif;
                }
                .stSidebar {
                    background-color: #2980b9;
                }
                h1, h2, h3, h4, h5 {
                    color: #ffffff;
                }
                .stButton > button {
                    background-color: #2980b9;
                    color: white;
                    border: none;
                    font-weight: bold;
                }
                .stButton > button:hover {
                    background-color: #1c638c;
                    color: white;
                }
                .stDownloadButton > button {
                    background-color: #e74c3c;
                    color: white;
                }
                .css-1d391kg, .css-1offfwp {
                    background-color: #2980b9 !important;
                    color: #ffffff !important;
                }
                .css-10trblm {
                    color: #ffffff !important;
                }
                .stDataFrame {
                    background-color: #3498db;
                    color: #ffffff;
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
