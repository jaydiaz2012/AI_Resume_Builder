import streamlit as st
import pandas as pd

def main():
    st.title("AI Resume Builder")
    st.write("Let's create a professional resume step by step!")

    # Step 1: Collect Personal Information
    st.header("Personal Information")
    name = st.text_input("Full Name")
    address = st.text_input("Address")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email Address")

    # Step 2: Collect Educational Background
    st.header("Educational Background")
    education = []
    add_education = st.button("Add Education")

    if "education" not in st.session_state:
        st.session_state.education = []

    if add_education:
        degree = st.text_input("Degree/Qualification", key="degree")
        institution = st.text_input("School/University", key="institution")
        grad_year = st.text_input("Graduation Year", key="grad_year")
        if degree and institution and grad_year:
            st.session_state.education.append({
                "Degree": degree,
                "Institution": institution,
                "Graduation Year": grad_year,
            })

    st.write(pd.DataFrame(st.session_state.education))

    # Step 3: Collect Work Experience
    st.header("Work Experience")
    if "work_experience" not in st.session_state:
        st.session_state.work_experience = []

    add_experience = st.button("Add Work Experience")
    if add_experience:
        company = st.text_input("Company Name", key="company")
        job_title = st.text_input("Job Title", key="job_title")
        start_date = st.text_input("Start Date (MM/YYYY)", key="start_date")
        end_date = st.text_input("End Date (MM/YYYY or Present)", key="end_date")
        responsibilities = st.text_area("Key Responsibilities", key="responsibilities")
        if company and job_title and start_date and responsibilities:
            st.session_state.work_experience.append({
                "Company": company,
                "Job Title": job_title,
                "Start Date": start_date,
                "End Date": end_date,
                "Responsibilities": responsibilities,
            })

    st.write(pd.DataFrame(st.session_state.work_experience))

    # Step 4: Collect Skills
    st.header("Skills")
    if "skills" not in st.session_state:
        st.session_state.skills = []

    skill = st.text_input("Enter a skill")
    add_skill = st.button("Add Skill")
    if add_skill and skill:
        st.session_state.skills.append(skill)

    st.write("Skills:", st.session_state.skills)

    # Step 5: Collect References
    st.header("References")
    if "references" not in st.session_state:
        st.session_state.references = []

    add_reference = st.button("Add Reference")
    if add_reference:
        ref_name = st.text_input("Full Name", key="ref_name")
        ref_job = st.text_input("Job Title", key="ref_job")
        ref_company = st.text_input("Company Name", key="ref_company")
        ref_phone = st.text_input("Contact Number", key="ref_phone")
        if ref_name and ref_job and ref_company and ref_phone:
            st.session_state.references.append({
                "Name": ref_name,
                "Job Title": ref_job,
                "Company": ref_company,
                "Contact": ref_phone,
            })

    st.write(pd.DataFrame(st.session_state.references))

    # Step 6: Display Final Resume
    if st.button("Generate Resume"):
        st.header("Generated Resume")
        st.write(f"**Name:** {name}")
        st.write(f"**Address:** {address}")
        st.write(f"**Phone:** {phone}")
        st.write(f"**Email:** {email}")

        st.subheader("Education")
        for edu in st.session_state.education:
            st.write(f"- {edu['Degree']} from {edu['Institution']} ({edu['Graduation Year']})")

        st.subheader("Work Experience")
        for exp in st.session_state.work_experience:
            st.write(f"- **{exp['Job Title']} at {exp['Company']}** ({exp['Start Date']} - {exp['End Date']})")
            st.write(f"  - {exp['Responsibilities']}")

        st.subheader("Skills")
        st.write(", ".join(st.session_state.skills))

        st.subheader("References")
        for ref in st.session_state.references:
            st.write(f"- {ref['Name']} ({ref['Job Title']}, {ref['Company']}): {ref['Contact']}")

if __name__ == "__main__":
    main()
