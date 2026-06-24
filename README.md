# 🧠 DocuMind AI

<div align="center">

# 🚀 AI-Powered Document Intelligence Platform

### Chat with Your Documents Using RAG, LangChain, Mistral AI & ChromaDB

Transform static documents into an interactive knowledge base powered by Retrieval-Augmented Generation (RAG).

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green?style=for-the-badge)
![Mistral AI](https://img.shields.io/badge/Mistral-AI-orange?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Database-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</div>

---

## 🌟 Overview

DocuMind AI is an intelligent document question-answering system built using **Retrieval-Augmented Generation (RAG)**.

Instead of relying solely on a Large Language Model's pre-trained knowledge, DocuMind AI retrieves relevant information directly from uploaded documents and uses that context to generate accurate, grounded, and context-aware responses.

This project demonstrates practical implementation of:

- 🔍 Semantic Search
- 🧠 Retrieval-Augmented Generation (RAG)
- 📚 Vector Databases
- 🤖 Large Language Models
- 📄 Document Intelligence Systems

---

# ✨ Features

### 📄 Document Processing

- Upload and process documents
- Extract textual information
- Intelligent document chunking

### 🔍 Semantic Retrieval

- Generate vector embeddings
- Store embeddings in ChromaDB
- Similarity-based context retrieval

### 🧠 AI-Powered Question Answering

- Context-aware responses
- Grounded answers from source documents
- Reduced hallucinations through retrieval

### 🎨 Interactive User Experience

- Simple web interface
- Real-time document interaction
- Fast question answering workflow

### 🔐 Secure Development

- Environment-based configuration
- API key protection using `.env`
- Sensitive files excluded using `.gitignore`

---

# 🏗️ System Architecture

```text
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
```

---

# 🛠️ Technology Stack

## Backend

- Python
- LangChain
- ChromaDB

## AI Stack

- Mistral AI
- Mistral Embeddings
- Retrieval-Augmented Generation (RAG)

## Frontend

- HTML
- CSS
- JavaScript

## Development Tools

- Git
- GitHub
- Virtual Environments
- Environment Variables

---

# 📂 Project Structure

```text
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
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Harshittt200/DocuMind-AI.git
cd DocuMind-AI
```

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

## 3️⃣ Activate Virtual Environment

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 5️⃣ Configure Environment Variables

Create a `.env` file:

```env
MISTRAL_API_KEY=YOUR_API_KEY
```

## 6️⃣ Run Application

```bash
python Main.py
```

---

# 💬 Example Queries

### Document Summarization

```text
Summarize this document.
```

### Information Extraction

```text
What are the key findings?
```

### Concept Explanation

```text
Explain the main concepts discussed in the document.
```

### Executive Summary

```text
Generate an executive summary.
```

---

# 📸 Demo

Add screenshots after running the application.

```markdown
![Home Screen](assets/home.png)

![Document Upload](assets/upload.png)

![Question Answering](assets/chat.png)
```

---

# 🎯 Learning Outcomes

This project helped me gain practical experience with:

- LangChain Framework
- Vector Databases
- Embedding Models
- Retrieval-Augmented Generation
- Prompt Engineering
- Document Processing Pipelines
- End-to-End AI Application Development

---

# 🔮 Future Enhancements

- [ ] Multi-document chat
- [ ] Source citations
- [ ] Streaming responses
- [ ] FastAPI backend
- [ ] Docker deployment
- [ ] Authentication system
- [ ] Cloud deployment
- [ ] Conversation memory

---

# 👨‍💻 Author

## Harshit Garg

**B.Tech – Information Technology**  
Ajay Kumar Garg Engineering College

Interested in AI Engineering, Agentic AI, RAG Systems, Backend Development, and Intelligent Applications.

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

Built with ❤️ using Python, LangChain, Mistral AI, and ChromaDB.

</div>