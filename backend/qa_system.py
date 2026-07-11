from backend.gemini_engine import ask_gemini


def ask_question(document_text, question):

    prompt = f"""
    You are a legal assistant.

    Legal document:

    {document_text}

    User question:

    {question}

    Answer in simple language.
    """

    return ask_gemini(prompt)