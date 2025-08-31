import streamlit as st
from ai_researcher2 import INITIAL_PROMPT, graph, config
from pathlib import Path
import logging
from langchain_core.messages import AIMessage,ToolMessage

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Basic app config
st.set_page_config(page_title="Research AI Agent", page_icon="📄")
st.title("📄 Research AI Agent")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    logger.info("Initialized chat history")

if "pdf_path" not in st.session_state:
    st.session_state.pdf_path = None

# Chat interface
user_input = st.chat_input("What research topic would you like to explore?")

if user_input:
    # Log and display user input
    logger.info(f"User input: {user_input}")
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Prepare input for the agent
    chat_input = {"messages": [{"role": "system", "content": INITIAL_PROMPT}] + st.session_state.chat_history}
    logger.info("Starting agent processing...")

    # Stream agent response
    full_response = ""
    pdf_path = None
    with st.chat_message("assistant").empty() as asst_msg:
        for s in graph.stream(chat_input, config, stream_mode="values"):
            message = s["messages"][-1]

            # Check for tool output that contains the PDF path
            if isinstance(message, ToolMessage) and "paper_" in message.content and ".pdf" in message.content:
                pdf_path = message.content.strip()
                logger.info(f"PDF generated at path: {pdf_path}")

            # Handle assistant response
            if isinstance(message, AIMessage) and message.content:
                full_response = message.content
                asst_msg.write(full_response)
    
    # Add final response to history
    st.session_state.chat_history.append({"role": "assistant", "content": full_response})

    # If a PDF was generated, show the download button
    if pdf_path:
        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="Download Research Paper (PDF)",
                data=pdf_file,
                file_name=Path(pdf_path).name,
                mime="application/pdf"
            )