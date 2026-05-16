import streamlit as st
from my_logic import run_math

# Page styling
st.set_page_config(page_title="Excel Calculator", page_icon="📊", layout="centered")

st.title("📊 Excel Analyzer")
st.caption("Runs completely offline in your local browser")

st.write("---")

# File uploader widget (handles xlsx and xls automatically)
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    st.info("File uploaded successfully! Starting calculations...")
    
    try:
        # Pass the uploaded file directly to your math logic
        output_string = run_math(uploaded_file)
        
        # Display the results in a clean, modern green box
        st.success("Calculation Complete!")
        st.markdown(f"### Results:\n{output_string}")
        
    except Exception as e:
        st.error(f"An error occurred in your math logic: {str(e)}")