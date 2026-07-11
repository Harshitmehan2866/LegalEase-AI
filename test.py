from backend.gemini_engine import ask_gemini

response = ask_gemini(
    "Explain what a rental agreement is in simple words."
)

print(response)