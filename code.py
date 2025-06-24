import streamlit as st

st.title("📄 PDF Uploader")

# Upload PDF
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Save the uploaded PDF
    with open(f"uploaded_{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ {uploaded_file.name} has been uploaded successfully!")
