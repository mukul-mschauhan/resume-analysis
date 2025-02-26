# Import the Libraries and Set up the Local Environment
import streamlit as st
from dotenv import load_dotenv
load_dotenv() 
import google.generativeai as genai
from pdf import read_pdf
from analysis import profile

# Lets create the Front End
st.header("📝Resume Analysis: :blue[Your LLM-Powered Resume Analyzer]🎯👩🏻‍💻✅", 
          divider="green")
st.subheader("📌Tips for Using the Application")
notes = f'''
* **Upload the Resume(PDF):** The first step is to upload the resume for analysis.
* **Paste the Target JD:** Share the Details of the Job Description in the Text Area Below
* **Unleash the Power of LLMs:** Here, the Gemini Model will analyze the Job Description 
supplied with the Resume uploaded and will provide insights such as **ATS Score**, 
**Probability of Getting Selected** and so on.'''
st.markdown(notes)

# Sidebar
st.sidebar.header("👉Upload the Resume")
user_profile = st.sidebar.file_uploader("Please Upload the Resume here", type = ["pdf"])
st.sidebar.markdown("Created by Mukul Chauhan")
st.sidebar.markdown("🌐Linkedin: www.linkedin.com/mukulchauhan")

# Job Description Box
st.subheader("Enter the Job Description✍", divider = True)
jd = st.text_area(label="📢Copy Paste the Job Desc from Linkedin or any Job Portal", 
                        max_chars=10000)

submit = st.button("🎯Get AI Powered Insights🎯")
if submit:
    st.markdown(profile(user_profile = user_profile, job_desc = jd))
    