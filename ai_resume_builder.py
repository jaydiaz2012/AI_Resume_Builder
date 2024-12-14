import os 
from io import BytesIO
import streamlit as st

# Configure API Keys
OPENAI_API_KEY = "" 
openai.api_key = OPENAI_API_KEY

def generate_resume(data):
    """Generate a plain text resume based on collected data."""
    resume = f"""
    {data['name']}
    {data['address']} | {data['contact']} | {data['email']}

    Objective:
    {data['objective']}

    Education:
    {data['education']}

    Work Experience:
    {data['work_experience']}

    Skills:
    {data['skills']}

    References:
    {data['references']}
    """
    return resume

# Streamlit App
st.title("AI Resume Builder")
st.write("Answer the questions below to build your resume step by step.")

# Personal Information
st.header("Personal Information")
name = st.text_input("Full Name")
address = st.text_input("Address")
contact = st.text_input("Contact Number")
email = st.text_input("Email Address")

# Career Objective
st.header("Career Objective")
objective = st.text_area("Briefly describe your career objective (Optional)", "")

# Education
st.header("Educational Background")
education_entries = []
number_of_education = st.number_input("Number of educational qualifications:", min_value=1, step=1)
for i in range(number_of_education):
    st.subheader(f"Education {i+1}")
    degree = st.text_input(f"Degree for Education {i+1}")
    school = st.text_input(f"School/University for Education {i+1}")
    year = st.text_input(f"Graduation Year for Education {i+1}")
    education_entries.append(f"{degree}, {school} - {year}")
education = "\n".join(education_entries)

# Work Experience
st.header("Work Experience")
work_entries = []
number_of_jobs = st.number_input("Number of previous jobs:", min_value=1, step=1)
for i in range(number_of_jobs):
    st.subheader(f"Job {i+1}")
    job_title = st.text_input(f"Job Title for Job {i+1}")
    company = st.text_input(f"Company Name for Job {i+1}")
    dates = st.text_input(f"Dates of Employment for Job {i+1}")
    responsibilities = st.text_area(f"Key Responsibilities for Job {i+1}")
    work_entries.append(f"{job_title} at {company} ({dates})\n- {responsibilities}")
work_experience = "\n".join(work_entries)

# Skills
st.header("Skills")
skills = st.text_area("List your skills (comma-separated)", "")

# References
st.header("References")
reference_entries = []
number_of_references = st.number_input("Number of references:", min_value=1, step=1)
for i in range(number_of_references):
    st.subheader(f"Reference {i+1}")
    ref_name = st.text_input(f"Name of Reference {i+1}")
    ref_contact = st.text_input(f"Contact Number of Reference {i+1}")
    ref_email = st.text_input(f"Email of Reference {i+1}")
    reference_entries.append(f"{ref_name}, {ref_contact}, {ref_email}")
references = "\n".join(reference_entries)

# Generate Resume
if st.button("Generate Resume"):
    user_data = {
        "name": name,
        "address": address,
        "contact": contact,
        "email": email,
        "objective": objective,
        "education": education,
        "work_experience": work_experience,
        "skills": skills,
        "references": references
    }

    resume_text = generate_resume(user_data)

    st.header("Your Resume")
    st.text(resume_text)

    # Download Option
    buffer = BytesIO()
    buffer.write(resume_text.encode("utf-8"))
    buffer.seek(0)

    st.download_button(
        label="Download Resume as Text File",
        data=buffer,
        file_name="resume.txt",
        mime="text/plain"
    )
