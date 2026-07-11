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
            "Analyzing..."
        ):

            result = simplify_document(
                document_text
            )

        st.write(result)

    question = st.text_input(
        "Ask a question about the document"
    )

    if st.button(
        "Get Answer"
    ):

        answer = ask_question(
            document_text,
            question
        )

        st.write(answer)