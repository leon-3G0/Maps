import streamlit as st
from io import BytesIO
import pandas as pd
from core.route import process, new_download_file

st.set_page_config(page_title="Distance Calculator", layout="wide")

st.title("🚗 Distance Calculator")

# File uploader
uploaded_file = st.file_uploader(
    "Choose an excel file: ",
    type='xlsx',
    help="Make sure the file's A & B columns have your origin and destination."

)

if uploaded_file != None:
    try:
        xlsx_file = pd.ExcelFile(uploaded_file)
        sheet_names = xlsx_file.sheet_names
        selected_sheets = st.multiselect("Choose sheets", sheet_names)

        if st.button(label="Calculate"):
            all_res = {}
            for sheet in selected_sheets:
                df = pd.read_excel(uploaded_file, sheet_name=sheet)
                result = process(df)
                all_res[sheet] = result
                file = new_download_file(all_res)
                # Download Button...

    except Exception as e:
        st.error(f"❌ Failed processing file: {str(e)}")

