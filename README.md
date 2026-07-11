# ⚖️ LegalEase AI

An AI-powered legal document simplification platform that transforms complex legal documents into simple, understandable language using Google's Gemini model.

## 📌 Problem Statement

Legal documents such as rental agreements, loan contracts, privacy policies, and terms of service often contain difficult legal language that is hard for ordinary users to understand.

LegalEase AI bridges this gap by analyzing legal documents and providing:

- Plain-English summaries
- Risk analysis
- Important clauses
- User obligations
- Financial implications
- Interactive question answering

## 🚀 Features

✅ Upload legal documents (PDF and DOCX)

✅ AI-generated document summaries

✅ Identify important clauses

✅ Highlight legal and financial risks

✅ Ask questions about the document

✅ User-friendly Streamlit interface

## 🛠️ Tech Stack

| Category | Technology |
|----------|-------------|
| Frontend | Streamlit |
| Backend | Python |
| AI Model | Google Gemini |
| Document Processing | PyPDF2, python-docx |
| Environment Management | python-dotenv |
| Version Control | Git & GitHub |

## 📂 Project Structure

```text
LegalEase-AI/
│
├── app.py
├── README.md
├── requirements.txt
├── .env
│
├── backend/
│   ├── gemini_engine.py
│   ├── document_processor.py
│   ├── legal_analyzer.py
│   └── qa_system.py
│
├── database/
│   └── db.py
│
├── utils/
│   └── helpers.py
│
├── assets/
├── data/
└── screenshots/
```

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Harshitmehan2866/LegalEase-AI.git

cd LegalEase-AI
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure API key

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

### Run the application

```bash
streamlit run app.py
```

## 🖼️ Screenshots

Add your screenshots inside the `screenshots` folder.

Example:

- Home page
- Document upload
- AI-generated summary
- Question answering

## 🎯 Sample Questions

- What are my responsibilities?
- Are there any hidden charges?
- Can this agreement be terminated?
- What legal risks should I know about?
- Summarize this document in simple language.

## 🔮 Future Enhancements

- Clause highlighting
- Risk scoring
- PDF report generation
- Multilingual support
- User authentication
- Cloud deployment

## 👨‍💻 Author

**Harshit Mehan**

B.Tech Data Science Student

Manav Rachna International Institute of Research and Studies

GitHub: https://github.com/Harshitmehan2866