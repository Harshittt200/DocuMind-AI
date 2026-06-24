🧠 DocuMind AI

<div align="center">

🚀 AI-Powered Document Intelligence Platform

Chat with Your Documents Using RAG, LangChain, Mistral AI & ChromaDB

Transform static documents into an interactive knowledge base powered by Retrieval-Augmented Generation (RAG).

</div>

⸻

🌟 Overview

DocuMind AI is an intelligent document question-answering system built using Retrieval-Augmented Generation (RAG).

Instead of relying solely on a Large Language Model’s pre-trained knowledge, DocuMind AI retrieves relevant information directly from uploaded documents and uses that context to generate accurate, grounded, and context-aware responses.

This project demonstrates practical implementation of:

* 🔍 Semantic Search
* 🧠 Retrieval-Augmented Generation (RAG)
* 📚 Vector Databases
* 🤖 Large Language Models
* 📄 Document Intelligence Systems

⸻

✨ Features

📄 Document Processing

* Upload and process documents
* Extract textual information
* Intelligent document chunking

🔍 Semantic Retrieval

* Generate vector embeddings
* Store embeddings in ChromaDB
* Similarity-based context retrieval

🧠 AI-Powered Question Answering

* Context-aware responses
* Grounded answers from source documents
* Reduced hallucinations through retrieval

🎨 Interactive User Experience

* Simple web interface
* Real-time document interaction
* Fast question answering workflow

🔐 Secure Development

* Environment-based configuration
* API key protection using .env
* Sensitive files excluded using .gitignore

⸻

🏗️ System Architecture

                ┌────────────────────┐
                │  User Documents    │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Document Loader    │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Text Chunking      │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Mistral            │
                │ Embeddings         │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ ChromaDB           │
                │ Vector Store       │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Retriever          │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Mistral LLM        │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Generated Answer   │
                └────────────────────┘

⸻

🛠️ Technology Stack

Backend

* Python
* LangChain
* ChromaDB

AI Stack

* Mistral AI
* Mistral Embeddings
* Retrieval-Augmented Generation (RAG)

Frontend

* HTML
* CSS
* JavaScript

Development Tools

* Git
* GitHub
* Virtual Environments
* Environment Variables

⸻

📂 Project Structure

DocuMind-AI
│
├── Main.py
├── app.py
├── create_database.py
├── rag_ui.html
├── requirements.txt
│
├── document_loader/
│   ├── pdf.py
│   └── text.py
│
├── retrievers/
│   └── mmx.py
│
├── vectorstore/
│   └── db.py
│
├── .gitignore
└── README.md

⸻

⚙️ Installation

1️⃣ Clone Repository

git clone https://github.com/Harshittt200/DocuMind-AI.git
cd DocuMind-AI

2️⃣ Create Virtual Environment

python -m venv .venv

3️⃣ Activate Virtual Environment

macOS / Linux

source .venv/bin/activate

Windows

.venv\Scripts\activate

4️⃣ Install Dependencies

pip install -r requirements.txt

5️⃣ Configure Environment Variables

Create a .env file:

MISTRAL_API_KEY=YOUR_API_KEY

6️⃣ Run Application

python Main.py

⸻

💬 Example Queries

Document Summarization

Summarize this document.

Information Extraction

What are the key findings?

Concept Explanation

Explain the main concepts discussed in the document.

Executive Summary

Generate an executive summary.

⸻

📸 Demo

Add screenshots after running the application.

![Home Screen](assets/home.png)
![Document Upload](assets/upload.png)
![Question Answering](assets/chat.png)

⸻

🎯 Learning Outcomes

This project helped me gain practical experience with:

* LangChain Framework
* Vector Databases
* Embedding Models
* Retrieval-Augmented Generation
* Prompt Engineering
* Document Processing Pipelines
* End-to-End AI Application Development

⸻

🔮 Future Enhancements

* Multi-document chat
* Source citations
* Streaming responses
* FastAPI backend
* Docker deployment
* Authentication system
* Cloud deployment
* Conversation memory

⸻

👨‍💻 Author

Harshit Garg

B.Tech – Information Technology
Ajay Kumar Garg Engineering College

Interested in AI Engineering, Agentic AI, RAG Systems, Backend Development, and Intelligent Applications.

⸻

<div align="center">

⭐ If you found this project useful, consider giving it a star!

Built with ❤️ using Python, LangChain, Mistral AI, and ChromaDB.

</div>