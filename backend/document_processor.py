import PyPDF2
from docx import Document


def read_pdf(file):

    text = ""

    reader = PyPDF2.PdfReader(file)

    for page in reader.pages:

        extracted = page.extract_text()

        if extracted:

            text += extracted + "\n"

    return text


def read_docx(file):

    doc = Document(file)

    text = "\n".join(
        para.text for para in doc.paragraphs
    )

    return text