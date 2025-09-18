
import os
import streamlit as st
from dotenv import load_dotenv

from llama_index.llms.openai import OpenAI
from llama_index.agent.openai import OpenAIAgent
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, SummaryIndex
from llama_index.core import load_index_from_storage, StorageContext

# Load environment variables from .env
load_dotenv()

# Streamlit page config
st.set_page_config(page_title="Luxembourg Immigration Chatbot", layout="wide")

# API key setup: try secrets.toml first, then .env
try:
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
except Exception:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.error("OpenAI API key not found. Please add it to Streamlit secrets or your .env file.")
    st.stop()

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Constants
EMBEDDING_MODEL = "text-embedding-3-small"
LLM_MODEL       = "gpt-4o-mini"

DATA_DIR = os.path.join(os.path.dirname(__file__), "vector_data")
PDF_DIR  = "/Users/omkar/Documents/Projects/2nd semester/Immigration_chatbot_RAG/updated_pdfs_with_visa"

# Title
st.title("Luxembourg Immigration Chatbot 🤖🇱🇺")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Load and prepare agent (cached)
@st.cache_resource
def load_agent():
    # Load documents
    documents = SimpleDirectoryReader(input_dir=PDF_DIR).load_data()
    # Parse into nodes
    parser = SentenceSplitter()
    nodes = parser.get_nodes_from_documents(documents)

    # Build or load vector index
    if not os.path.exists(DATA_DIR):
        vector_index = VectorStoreIndex(nodes)
        vector_index.storage_context.persist(persist_dir=DATA_DIR)
    else:
        storage_context = StorageContext.from_defaults(persist_dir=DATA_DIR)
        vector_index = load_index_from_storage(storage_context)

    # Summary index
    summary_index = SummaryIndex(nodes)

    # Query engines
    vector_qe = vector_index.as_query_engine(
        llm=OpenAI(model=LLM_MODEL, streaming=True),
        embedding_model=OpenAI(model=EMBEDDING_MODEL)
    )
    summary_qe = summary_index.as_query_engine(
        llm=OpenAI(model=LLM_MODEL, streaming=True)
    )

    # Tools
    tools = [
        QueryEngineTool(
            query_engine=vector_qe,
            metadata=ToolMetadata(
                name="visa_detail_tool",
                description="For detailed and specific questions related to Luxembourg immigration, authorisation to stay, visa and residence-permit process and give precise answers."
            )
        ),
        QueryEngineTool(
            query_engine=summary_qe,
            metadata=ToolMetadata(
                name="visa_summary_tool",
                description="For high-level overviews of the immigration, authorisation to stay, visa and residence-permit process."
            )
        ),
    ]

    # Agent
    system_prompt = (
        """ You are Luxembourg-ImmigrationBot. Answer only questions about Next steps after getting admitted in Luxembourg Institutions, Authorizations to stay, Visas, Residence permit, luxembourg immigration and Ministry of Luxembourg. 
        Always understand the question, see what is actually asked try to give precise answer. If question requires just 1-2 line answer of specific information then give specific
        answer in 1-2 lines only, stick to the question and give relevant answer.
        use the provided tools for retrieval. If you are asked off-topic, politely decline.
        """
    )
    agent = OpenAIAgent.from_tools(
        tools,
        llm=OpenAI(model=LLM_MODEL, streaming=True),
        system_prompt=system_prompt,
        verbose=False
    )
    return agent

agent = load_agent()

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Ask me about Luxembourg immigration..."):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate streaming response
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_resp = ""
        stream = agent.stream_chat(prompt)
        for chunk in stream.response_gen:
            full_resp += chunk
            placeholder.markdown(full_resp + "▌")
        placeholder.markdown(full_resp)

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": full_resp})
