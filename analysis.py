from pdf import read_pdf
import os
import google.generativeai as genai
import streamlit as st

# Configure the key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro") # Initiate the Model

def profile(user_profile, job_desc):
    if user_profile is not None:
        pdf = read_pdf(user_profile)
        st.sidebar.markdown("The Resume has been Uploaded")
    else:
        st.warning("Uplod the Resume")
    # ATS Score
    ats_score = model.generate_content(f'''compare the resume{pdf} with
                                       job description {job_desc} and
                                       suggest the ATS Score 
                                       (in percent) of the resume''')
    # Chances of Selection
    prob_score = model.generate_content(f'''compare the resume{pdf} with
                                       job description {job_desc} and
                                       suggest the Probability 
                                       (in percent) of Getting Selected''')
    # Keyword Analysis
    keyword = model.generate_content(f'''Analyse the Keywords missing in the resume{pdf} with
                                       job description {job_desc} and
                                       mention them in bold and give narratives how to add them in the resume''')
    # Tailored Projects as Per JD
    projects = model.generate_content(f'''compare the resume{pdf} with
                                       job description {job_desc} and
                                       give me the list of projects/hackathons (in bold) with 
                                       problem statement & Probability of Selection 
                                       as per the Job Description''')
    # Swot Analysis
    swot = model.generate_content(f'''compare the resume{pdf} with
                                       job description {job_desc} and
                                       Provide a SWOT Analysis''')
    # Improvement Tips
    improvement = model.generate_content(f'''Suggest Improvements to the resume{pdf} after
                                         comparing with job description {job_desc} so that
                                         the ATS Score of the resume increases and it is 
                                         better aligned and mention the comments in bold.''')
    # Creating a New Resume Narrative..
    resume = model.generate_content(f'''Recreate the New Resume basis the {pdf} to 
                                    highlight the relevant skill, projects and experience
                                    according to the job description {job_desc}''')
    # Display the Results
    return(st.write(ats_score.text),
           st.write(prob_score.text),
           st.write(keyword.text),
           st.write(projects.text),
           st.write(swot.text),
           st.write(improvement.text),
           st.write(resume.text))
    