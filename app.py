import streamlit as st

from backend.document_processor import (
    read_pdf,
    read_docx
)

from backend.legal_analyzer import (
    simplify_document
)

from backend.qa_system import (
    ask_question
)

from utils.pdf_generator import (
    generate_pdf
)


st.set_page_config(
    page_title="LegalEase AI",
    layout="wide"
)

with st.sidebar:

    st.header("About")

    st.write(
        """
        LegalEase AI uses Google Gemini to simplify legal documents and answer user questions.
        """
    )

    st.info(
        "This tool provides informational guidance and is not legal advice."
    )


st.title("⚖️ LegalEase AI")

st.markdown("""
### Simplify Legal Documents with AI

Upload:

- Rental Agreements
- Loan Contracts
- Terms and Conditions
- Employment Contracts
- Privacy Policies

Get instant explanations and risk analysis.
""")


uploaded_file = st.file_uploader(
    "Upload a legal document",
    type=["pdf", "docx"]
)

if uploaded_file:

    if uploaded_file.name.endswith(".pdf"):

        document_text = read_pdf(
            uploaded_file
        )

    else:

        document_text = read_docx(
            uploaded_file
        )

    st.success(
        "Document uploaded successfully!"
    )

    if st.button(
        "Simplify Document"
    ):

        with st.spinner(
            "Analyzing document..."
        ):

            result = simplify_document(
                document_text
            )

        st.subheader(
            "Document Analysis"
        )

        st.write(
            result
        )

        pdf_file = generate_pdf(
            result
        )

        with open(
            pdf_file,
            "rb"
        ) as file:

            st.download_button(
                label="📥 Download Report",
                data=file,
                file_name="legal_report.pdf",
                mime="application/pdf"
            )

    st.subheader(
        "Ask Questions"
    )

    question = st.text_input(
        "Ask a question about the document"
    )

    if st.button(
        "Get Answer"
    ):

        if question:

            answer = ask_question(
                document_text,
                question
            )

            st.write(
                answer
            )

        else:

            st.warning(
                "Please enter a question."
            )