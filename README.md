# Luxembourg Immigration ChatBot 🤖🇱🇺

<img width="1450" height="861" alt="image" src="https://github.com/user-attachments/assets/5fac0679-232e-47d4-b77a-f0b248dfecb9" />



A Retrieval-Augmented Generation (RAG) powered chatbot designed to provide accurate and up-to-date information about Luxembourg immigration processes, visa applications, residence permits, and authorizations to stay.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Advantages](#advantages)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This chatbot leverages Retrieval-Augmented Generation (RAG) architecture to provide precise, document-based answers about Luxembourg immigration processes. Unlike generic AI assistants, this chatbot is specifically trained on official Luxembourg immigration documents, ensuring accurate and current information.

## ✨ Features

- **Document-Based Responses**: Answers are generated from official Luxembourg immigration PDFs
- **Intelligent Agent System**: Uses OpenAI Agent with specialized tools for different query types
- **Real-time Streaming**: Provides streaming responses for better user experience
- **Dual Query Engines**: 
  - Vector-based search for detailed, specific questions
  - Summary-based responses for high-level overviews
- **Semantic Search**: Uses embedding-based similarity matching for relevant document retrieval
- **Persistent Storage**: Efficient vector index caching for faster responses

## 🏗️ Architecture

### RAG Pipeline
```
Document Loading → Text Chunking → Embeddings → Vector Storage → Retrieval → Generation
```

### Document Processing Pipeline
1. **SimpleDirectoryReader**: Loads PDF documents from specified directory
2. **SentenceSplitter**: Creates manageable text chunks from documents
3. **Node Creation**: Converts text chunks into processable nodes
4. **VectorStoreIndex**: Stores embeddings for semantic similarity search

### Agent Decision Making
The system uses an intelligent agent with two specialized tools:
- **visa_detail_tool**: For detailed, specific immigration questions
- **visa_summary_tool**: For high-level overviews and summaries

## 🛠️ Technologies Used

- **Framework**: Streamlit (Web Interface)
- **LLM**: OpenAI GPT-4o-mini
- **Embeddings**: OpenAI text-embedding-3-small (1536-dimensional vectors)
- **RAG Framework**: LlamaIndex
- **Vector Operations**: Cosine similarity for semantic search
- **Document Processing**: PyPDF for PDF handling
- **Environment Management**: python-dotenv

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/luxembourg-immigration-chatbot.git
   cd luxembourg-immigration-chatbot
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages:**
   ```bash
   pip install streamlit openai llama-index python-dotenv
   ```

4. **Additional dependencies:**
   ```bash
   pip install llama-index-llms-openai llama-index-agent-openai llama-index-embeddings-openai
   ```

## ⚙️ Configuration

### API Key Setup

**Option 1: Using .env file (Recommended for local development)**
1. Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

**Option 2: Using Streamlit Secrets (For deployment)**
1. Create `.streamlit/secrets.toml` file:
   ```toml
   OPENAI_API_KEY = "your_openai_api_key_here"
   ```

### Document Setup
1. Create a directory for your PDF documents
2. Update the `PDF_DIR` variable in `app.py` to point to your documents directory:
   ```python
   PDF_DIR = "path/to/your/pdf/documents"
   ```

**⚠️ Important**: You must provide your own OpenAI API key. Get one from [OpenAI Platform](https://platform.openai.com/api-keys).

## 🚀 Usage

### Running the Application

1. **Start the Streamlit server:**
   ```bash
   streamlit run app.py
   ```

2. **Access the interface:**
   - Open your web browser and navigate to `http://localhost:8501`
   - The chatbot interface will load automatically

3. **Interact with the chatbot:**
   - Type your questions about Luxembourg immigration in the chat input
   - Receive streaming responses with accurate, document-based information
   - Ask about visas, residence permits, authorization to stay, and related topics

### Example Queries
- "What documents do I need for a Luxembourg visa application?"
- "How long does it take to process a residence permit?"
- "What are the requirements for authorization to stay in Luxembourg?"
- "Can you give me an overview of the immigration process?"

## 📁 Project Structure

```
luxembourg-immigration-chatbot/
│
├── app.py                    # Main Streamlit application
├── .env                      # Environment variables (create this)
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
│
├── .streamlit/
│   └── secrets.toml         # Streamlit secrets (for deployment)
│
├── vector_data/             # Generated vector index storage (auto-created)
│   ├── docstore.json
│   ├── index_store.json
│   └── vector_store.json
│
└── updated_pdfs_with_visa/  # Your PDF documents directory
    ├── document1.pdf
    ├── document2.pdf
    └── ...
```

## 🔍 How It Works

### 1. Document Processing
- **Loading**: PDF documents are loaded using SimpleDirectoryReader
- **Chunking**: Documents are split into manageable chunks using SentenceSplitter
- **Embedding**: Text chunks are converted to 1536-dimensional vectors using OpenAI's embedding model

### 2. Vector Operations
- **Storage**: Embeddings are stored in VectorStoreIndex for fast retrieval
- **Query Processing**: User queries are converted to embeddings
- **Similarity Search**: Cosine similarity matching finds relevant document chunks

### 3. Intelligent Response Generation
- **Agent Decision**: OpenAI Agent selects appropriate tool based on query type
- **Context Retrieval**: Relevant document chunks are retrieved
- **Response Generation**: GPT-4o-mini generates structured, contextual responses

### 4. Dual Query System
- **Detailed Queries**: Vector-based search for specific, precise answers
- **Summary Queries**: Summary index for high-level overviews

## 🎯 Advantages

### RAG vs Traditional Chatbots
- ✅ **Accuracy**: Responses based on official documents
- ✅ **Relevance**: Semantic similarity ensures contextually appropriate answers  
- ✅ **Freshness**: Easy updates by adding new PDF documents
- ✅ **Transparency**: Responses traceable to source documents
- ✅ **Domain-Specific**: Specialized knowledge about Luxembourg immigration

### RAG vs Fine-Tuning
- ⚡ **Instant Updates**: Add new documents without retraining
- 💰 **Cost-Effective**: No need for expensive GPU training
- 🔧 **Simple Maintenance**: No need for labeled training data
- 📈 **Scalable**: Easy to extend to new domains

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
