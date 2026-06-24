🚀 DocuMind AI

Intelligent Document Question Answering using RAG, Mistral AI & ChromaDB

DocuMind AI is a Retrieval-Augmented Generation (RAG) application that allows users to upload documents and interact with them using natural language.

The system processes documents, generates semantic embeddings, stores them in a vector database, retrieves relevant context, and generates grounded answers using Mistral AI.

⸻

✨ Features

* 📄 Upload PDF, TXT, DOCX, and Markdown files
* 🔍 Semantic Search using Vector Embeddings
* 🧠 Retrieval-Augmented Generation (RAG)
* ⚡ Mistral AI Integration
* 🗂 ChromaDB Vector Database
* 💬 Natural Language Question Answering
* 🎨 Interactive Web Interface
* 🔐 Secure API Key Management using Environment Variables

⸻

🏗 Architecture
Document Upload
      │
      ▼
Document Loader
      │
      ▼
Text Chunking
      │
      ▼
Mistral Embeddings
      │
      ▼
ChromaDB
      │
      ▼
Retriever
      │
      ▼
Mistral LLM
      │
      ▼
Generated Answer
🛠 Tech Stack

Backend

* Python
* LangChain
* ChromaDB

AI

* Mistral AI
* Mistral Embeddings
* Retrieval-Augmented Generation (RAG)

Frontend

* HTML
* CSS
* JavaScript

⸻

📂 Project Structure
DocuMind-AI/
│
├── Main.py
├── app.py
├── create_database.py
├── rag_ui.html
├── requirements.txt
│
├── document_loader/
├── retrievers/
├── vectorstore/
│
├── .gitignore
└── README.md

⚙️ Installation

Clone Repository
git clone https://github.com/Harshittt200/DocuMind-AI.git

cd DocuMind-AI

Create Virtual Environment
python -m venv .venv

Install Dependencies
pip install -r requirements.txt

🔑 Environment Variables

Create a .env file in the project root:
MISTRAL_API_KEY=YOUR_API_KEY

▶️ Running the Application
python Main.py

Open your browser and visit:
http://localhost:8000

💡 Example Questions

* Summarize this document
* What are the key findings?
* Explain the main concepts discussed
* Generate an executive summary
* List important dates and events
* What conclusions are presented?

⸻

📸 Demo

Add screenshots here after running the application.
![Upload Screen](assets/upload.png)

![Chat Interface](assets/chat.png)

🔮 Future Improvements

* Multi-document support
* Source citations
* Streaming responses
* Chat history
* Docker deployment
* FastAPI backend
* Authentication system

⸻

👨‍💻 Author

Harshit Garg

B.Tech Information Technology
Ajay Kumar Garg Engineering College

⸻

⭐ If you found this project useful, consider giving it a star.

