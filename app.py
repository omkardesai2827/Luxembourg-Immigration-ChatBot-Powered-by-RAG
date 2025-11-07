import os
import warnings
import streamlit as st
from dotenv import load_dotenv

# Suppress deprecation warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

from llama_index.llms.openai import OpenAI
from llama_index.agent.openai import OpenAIAgent
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core import VectorStoreIndex, SummaryIndex
from llama_index.core import load_index_from_storage, StorageContext

# Load environment variables from .env
load_dotenv()

# Streamlit page config
st.set_page_config(page_title="Luxembourg Immigration Chatbot", layout="wide")

# API key setup: try environment variable first, then secrets, then .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    try:
        OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    except Exception:
        pass

if not OPENAI_API_KEY:
    st.error("⚠️ OpenAI API key not found. Please set OPENAI_API_KEY environment variable.")
    st.stop()

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Constants
LLM_MODEL = "gpt-4o-mini"

# Flexible paths for Docker and local development
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "vector_data")

# Title
st.title("Luxembourg Immigration Chatbot 🤖🇱🇺")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Load and prepare agent (cached)
@st.cache_resource
def load_agent():
    # Load pre-generated vector index
    storage_context = StorageContext.from_defaults(persist_dir=DATA_DIR)
    vector_index = load_index_from_storage(storage_context)

    # Create summary index from the same storage
    summary_index = SummaryIndex.from_documents(
        vector_index.docstore.docs.values()
    )

    # Initialize LLM
    llm = OpenAI(model=LLM_MODEL, temperature=0.1)

    # Query engines
    vector_qe = vector_index.as_query_engine(
        llm=llm,
        similarity_top_k=3
    )
    summary_qe = summary_index.as_query_engine(
        llm=llm
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

    # System prompt
    system_prompt = (
        """You are Luxembourg-ImmigrationBot. Answer only questions about Next steps after getting admitted in Luxembourg Institutions, Authorizations to stay, Visas, Residence permit, luxembourg immigration and Ministry of Luxembourg. 
        Always understand the question, see what is actually asked try to give precise answer. If question requires just 1-2 line answer of specific information then give specific
        answer in 1-2 lines only, stick to the question and give relevant answer.
        use the provided tools for retrieval. If you are asked off-topic, politely decline.
        """
    )

    # Using OpenAIAgent with warnings suppressed
    agent = OpenAIAgent.from_tools(
        tools,
        llm=llm,
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