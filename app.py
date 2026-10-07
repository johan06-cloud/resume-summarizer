import streamlit as st
from pypdf import PdfReader
from extractor import extract_skills


st.set_page_config(
    page_title="Resume Summarizer",
    page_icon="📄",
    layout="wide"
)


st.title("📄 Resume Summarizer")

st.write("Upload a PDF resume and extract useful information.")


uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)


if uploaded_file is not None:

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"


    # Clean and combine broken PDF lines
    lines = text.splitlines()

    cleaned_lines = []

    for line in lines:
        line = line.strip()

        if line:
            cleaned_lines.append(line)


    # Combine lines that were broken by the PDF layout
    text = " ".join(cleaned_lines)


    # Add spacing after common section headings
    sections = [
        "EDUCATION",
        "SKILLS",
        "EXPERIENCE",
        "WORK EXPERIENCE",
        "PROJECTS",
        "CERTIFICATIONS",
        "ACHIEVEMENTS",
        "LEADERSHIP",
        "SUMMARY",
    ]


    for section in sections:
        text = text.replace(
            section,
            f"\n\n{section}\n"
        )


    text = text.strip()


    st.success("Resume uploaded successfully!")


    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume content",
        text,
        height=400
    )


    skills = extract_skills(text)


    st.subheader("Skills")


    if skills:

        for skill in skills:
            st.write(f"• {skill.title()}")

    else:

        st.write("No skills found.")