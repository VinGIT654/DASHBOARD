# DASHBOARD
An interactive Streamlit dashboard for dynamic data analysis with advanced filtering, pivot table creation, and download options. Supports any uploaded file, allows multi-column selection, and enables real-time insights. Ideal for supply chain, finance, and reporting workflows with zero-code usability.

# 📊 Custom Dashboard

The **Custom Dashboard** is an interactive, modular web application built using **Streamlit**. It enables users to upload operational data (CSV/Excel/Google Sheets), apply advanced filters, generate pivot tables, visualize insights through various charts, and download customized reports. Designed for real-time analytics and efficient decision-making, it serves as a one-stop tool for data exploration and performance monitoring.

---

## 🧱 Features

✅ Upload data from:
- Local `.csv` / `.xlsx` files  
- Google Sheets (via URL)

✅ Advanced filtering:
- Multi-column dynamic filtering UI
- Keyword search within column filters
- Reset all filters button

✅ Pivot Table:
- Choose any column(s) as Rows, Columns, and Values
- Aggregate using `sum`, `mean`, `count`, `first`, or `last`
- Warning if non-numeric column is used with `sum`/`mean`

✅ Charts & Visuals:
- Generate bar, pie, line, scatter, area charts
- Dynamic updates based on filtered data
- Plot multiple fields on same chart

✅ Export:
- Download filtered data
- Download pivot tables

✅ Modular design:
- Easy to extend, maintain, and reuse components

---

## 📁 Project Structure

fc_script.py ← Main Streamlit app (entry point)
DASHBOARD/
├── theme.py ← Handles theme and custom CSS
├── data_loader.py ← Uploads Excel/CSV and fetches Google Sheets
├── dashboard.py ← Displays top-level KPIs and summaries
├── filtering.py ← Filtering logic and UI for columns
├── pivot_table.py ← Build and display pivot tables
├── charts.py ← Handles chart creation (Bar, Pie, etc.)


---

### 🔹 `fc_script.py` - Main App

- The **entry point** of the application.
- Uses `Streamlit` to render a sidebar menu.
- Dynamically loads and integrates all the dashboard modules (`filtering`, `pivot_table`, `charts`, `theme`, etc.)
- Handles session state and layout switching.
- Calls functions from each dashboard component based on user interaction.

---

### 🔹 `theme.py` - Theme & Styling

- Contains CSS injected using `st.markdown(...)` for:
  - Hiding Streamlit elements (e.g., hamburger, watermark)
  - Custom fonts and background colors
  - Section padding and style tweaks
- Easy customization of dashboard look & feel.

---

### 🔹 `data_loader.py` - Data Upload

- Supports:
  - Uploading `.csv` or `.xlsx` files
  - Fetching data from **Google Sheets** using shared link
- Cleans numeric values (e.g., removes commas) and parses dates.
- Standardizes the dataset for downstream modules to work with.

---

### 🔹 `dashboard.py` - KPI Metrics Display

- Computes and displays high-level insights such as:
  - Total records
  - Counts by category
  - Sum of selected numeric fields
- Uses metric cards and summaries for quick insights.

---

### 🔹 `filtering.py` - Advanced Filtering Logic

- Allows users to filter the dataset using:
  - Multi-column selection
  - Searchable checkbox values
  - Dynamic UI components for string/date/numeric fields
- Maintains filtered data in `st.session_state` to share across all modules.

---

### 🔹 `pivot_table.py` - Pivot Table Generator

- Enables users to:
  - Select rows, columns, and values
  - Choose aggregation methods (`sum`, `mean`, `count`, etc.)
- Displays live pivot table from filtered data.
- Warns users if non-numeric columns are used in `sum` or `mean`.
- Download option for the pivot result as CSV.

---

### 🔹 `charts.py` - Chart Visualizer

- Lets users generate interactive charts including:
  - Bar, Pie, Line, Area, and Scatter plots
- Charts update dynamically with filtered data.
- Built using **Plotly** for interactivity and responsiveness.

---
