from backend.gemini_engine import ask_gemini


def simplify_document(text):

    prompt = f"""
    You are an expert legal assistant.

    Analyze the legal document and provide:

    1. Easy summary.
    2. Important clauses.
    3. User responsibilities.
    4. Financial obligations.
    5. Deadlines.
    6. Hidden risks.
    7. Risk score out of 100.
    8. Recommendations.

    Keep the language simple.

    Document:

    {text}
    """

    return ask_gemini(prompt)