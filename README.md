# Luxembourg Immigration ChatBot 🤖🇱🇺

<img width="1450" height="861" alt="image" src="https://github.com/user-attachments/assets/5fac0679-232e-47d4-b77a-f0b248dfecb9" />

A Retrieval-Augmented Generation (RAG) powered chatbot designed to provide accurate and up-to-date information about Luxembourg immigration processes, visa applications, residence permits, and authorizations to stay.

## 🎓 Quick Start with Docker (Recommended for Reproducibility)

### Prerequisites
- Docker installed ([Install Docker](https://docs.docker.com/get-docker/))
- OpenAI API Key ([Get API Key](https://platform.openai.com/api-keys))

### One-Command Setup
```bash
git clone Luxembourg-Immigration-ChatBot-Powered-by-RAG && \
cd Luxembourg-Immigration-ChatBot-Powered-by-RAG && \
docker build -t luxembourg-chatbot . && \
docker run -d --name luxembourg-chatbot -p 8501:8501 \
  -e OPENAI_API_KEY=your_openai_api_key_here \
  luxembourg-chatbot
```

**Then access:** http://localhost:8501

### Step-by-Step Docker Setup

**1. Clone the repository:**
```bash
git@github.com:omkardesai2827/Luxembourg-Immigration-ChatBot-Powered-by-RAG.git
cd Luxembourg-Immigration-ChatBot-Powered-by-RAG
```

**2. Build the Docker image:**
```bash
docker build -t luxembourg-chatbot .
```
*This takes 2-5 minutes on first build*

**3. Run the container:**

**for macbook terminal**
```bash
docker run -d \
  --name luxembourg-chatbot \
  -p 8501:8501 \
  -e OPENAI_API_KEY=your_openai_api_key_here \
  luxembourg-chatbot
```

**for windows**
```bash
docker run -d --name luxembourg-chatbot -p 8501:8501 -e OPENAI_API_KEY="your_api_key_here" luxembourg-chatbot
```

*Replace `your_openai_api_key_here` with your actual OpenAI API key*

**4. Access the application:**
- Open your browser: http://localhost:8501
- The chatbot interface will load automatically

**5. Stop the container when done:**
```bash
docker stop luxembourg-chatbot
docker rm luxembourg-chatbot
```

### Docker Commands Reference
```bash
# View running containers
docker ps

# View logs
docker logs luxembourg-chatbot

# Follow logs in real-time
docker logs -f luxembourg-chatbot

# Restart container
docker restart luxembourg-chatbot

# Remove container
docker rm -f luxembourg-chatbot

# Remove image
docker rmi luxembourg-chatbot
```

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
  - [Docker Setup (Recommended)](#quick-start-with-docker-recommended-for-reproducibility)
  - [Local Setup](#local-installation-without-docker)
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
- **Docker Support**: Fully containerized for reproducible deployment across any system

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
- **Containerization**: Docker (Python 3.13.5)

## 📦 Installation

### Docker Setup (Recommended)

See [Quick Start with Docker](#quick-start-with-docker-recommended-for-reproducibility) section above.

### Local Installation (Without Docker)

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
   pip install -r requirements.txt
```

## ⚙️ Configuration

### API Key Setup

**For Docker (Recommended):**
- Pass API key directly when running container:
```bash
  docker run -e OPENAI_API_KEY=your_key ...
```

**For Local Development:**

**Option 1: Using .env file**
1. Create a `.env` file in the project root:
```
   OPENAI_API_KEY=your_openai_api_key_here
```

**Option 2: Using Streamlit Secrets**
1. Create `.streamlit/secrets.toml` file:
```toml
   OPENAI_API_KEY = "your_openai_api_key_here"
```

**⚠️ Important**: You must provide your own OpenAI API key. Get one from [OpenAI Platform](https://platform.openai.com/api-keys).

## 🚀 Usage

### Using Docker (Recommended)
```bash
docker run -d --name luxembourg-chatbot -p 8501:8501 \
  -e OPENAI_API_KEY=your_key luxembourg-chatbot
```

Access at: http://localhost:8501

### Using Local Installation

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
├── requirements.txt          # Python dependencies
├── Dockerfile               # Docker image configuration
├── .dockerignore            # Docker build exclusions
├── docker-compose.yml       # Docker Compose configuration (optional)
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
├── README.md                # Project documentation
├── LICENSE                  # Project license
│
├── updated_pdfs_with_visa/  # PDF documents directory
│   ├── document1.pdf
│   ├── document2.pdf
│   └── ...
│
└── vector_data/             # Generated vector index (auto-created)
    ├── docstore.json
    ├── index_store.json
    └── vector_store.json
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

### 5. Pre-Generated Embeddings (Optimized Startup)
- **Vector embeddings are pre-generated and included in the Docker image**
- Benefits:
  - ⚡ **Fast startup**: 5-10 seconds (vs 1-2 minutes if generating on first run)
  - 💰 **Cost-effective**: No API calls for embeddings during startup
  - ✅ **Consistent**: Everyone gets identical embeddings
  - 🚀 **Production-ready**: Immediate availability after container starts
- The `vector_data/` directory contains pre-computed embeddings from all PDFs
- **API key is only used for**: Generating chat responses (not for embeddings)
- **To update embeddings**: Regenerate locally and rebuild Docker image when PDFs change

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

### Docker Benefits
- 🐳 **Reproducibility**: Works identically on any system
- 🔒 **Isolation**: No conflicts with system packages
- 📦 **Easy Deployment**: Single command to run
- 🔄 **Version Control**: Dockerfile ensures consistent environment

## 🐛 Troubleshooting

### Docker Issues

**Port already in use:**
```bash
# Use a different port
docker run -d -p 8080:8501 -e OPENAI_API_KEY=your_key luxembourg-chatbot
# Access at http://localhost:8080
```

**Container won't start:**
```bash
# Check logs for errors
docker logs luxembourg-chatbot
```

**Build fails:**
```bash
# Try building without cache
docker build --no-cache -t luxembourg-chatbot .
```

**API key not working:**
```bash
# Ensure you're passing it correctly
docker run -e OPENAI_API_KEY=sk-your-actual-key ...
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support

For issues or questions:
- Open an issue on GitHub
- Contact: desaiomkar767@gmail.com

## 👥 Authors

- Omkar Sanjay Desai - [GitHub]([https://github.com/yourusername](https://github.com/omkardesai2827))

## 🙏 Acknowledgments

- Built with [LlamaIndex](https://www.llamaindex.ai/)
- Powered by [OpenAI GPT-4o-mini](https://openai.com/)
- UI with [Streamlit](https://streamlit.io/)
- Containerized with [Docker](https://www.docker.com/)

---

**Last Updated**: October 2025
