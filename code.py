import streamlit as st
import requests

# Streamlit App Title
st.title("📄 Resume Uploader")

# Input Fields
name = st.text_input("Full Name")
email = st.text_input("Email")

# File Uploader
uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

# On Submit Button
if st.button("Submit"):
    if uploaded_file is not None and name and email:
        try:
            # Prepare the file and form data
            files = {
                'resume': (uploaded_file.name, uploaded_file, 'application/pdf')
            }
            data = {
                'name': name,
                'email': email
            }

            # Your Make.com Webhook URL
            webhook_url = 'https://hook.eu2.make.com/dettuhgmc604z4k5yf5emswvm3i92f3g'

            # Send POST request to Make.com
            response = requests.post(webhook_url, data=data, files=files)

            # Check response
            if response.status_code == 200:
                st.success("✅ Resume uploaded and sent successfully!")
            else:
                st.error(f"❌ Failed to send. Error code: {response.status_code}")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please fill all the fields and upload a PDF.")
