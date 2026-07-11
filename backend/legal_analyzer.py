from backend.gemini_engine import ask_gemini


def simplify_document(text):

    prompt = f"""
    You are an expert legal assistant.

    Analyze the document and provide:

    1. Easy Summary
    2. Payment Clauses
    3. Privacy Clauses
    4. Termination Clauses
    5. Liability Clauses
    6. User Responsibilities
    7. Financial Obligations
    8. Hidden Risks
    9. Risk Score (0-100)
    10. Final Recommendation

    Explain everything in simple language.

    Document:

    {text}
    """

    return ask_gemini(prompt)