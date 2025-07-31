import streamlit as st
from mathmind_agent.agent_executor import agent_executor


# Configure page settings
st.set_page_config(
    page_title="MathMind AI | Intelligent Mathematics Assistant",
    page_icon="🧮",
    layout="centered",
    menu_items={
        'Get Help': 'https://github.com/yourrepo/mathmind',
        'Report a bug': "https://github.com/yourrepo/mathmind/issues",
        'About': "MathMind AI - Your intelligent mathematics assistant"
    }
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .header-text {
        font-size: 2.5rem;
        font-weight: 600;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .subheader {
        font-size: 1.1rem;
        color: #7f8c8d;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sidebar-title {
        font-size: 1.3rem;
        font-weight: 500;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    .sidebar-section {
        margin-bottom: 2rem;
    }
    .error-message {
        color: #e74c3c;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# Header section
st.markdown('<p class="header-text">🧮 MathMind AI Assistant</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">Expert mathematical problem solving with step-by-step explanations</p>', unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Enter your mathematical query...")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Process and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing problem..."):
            try:
                response = agent_executor.invoke({"input": user_input})
                output = response.get("output", "I couldn't generate a response for this query.")
                
                # Format the output with better spacing
                formatted_output = output.replace('\n', '\n\n')
                st.markdown(formatted_output)
                
                st.session_state.messages.append({"role": "assistant", "content": output})
                
            except Exception as e:
                error_message = f"<span class='error-message'>⚠️ System error: {str(e)}</span>"
                st.markdown(error_message, unsafe_allow_html=True)
                st.session_state.messages.append({"role": "assistant", "content": error_message})

# Sidebar - Information panel
with st.sidebar:
    st.markdown('<p class="sidebar-title">About MathMind AI</p>', unsafe_allow_html=True)
    
    with st.expander("ℹ️ System Information", expanded=True):
        st.markdown("""
        MathMind AI is a specialized artificial intelligence system designed for:
        - Mathematical problem solving
        - Step-by-step solution explanations
        - Educational support for learners
        - Advanced computational mathematics
        """)
    
    with st.expander("🛠️ Technical Details", expanded=False):
        st.markdown("""
        **System Architecture:**
        - LangChain framework
        - Groq API inference
        - Streamlit interface
        
        **Model:** LLaMA3 70B (quantized)
        """)
    
    with st.expander("📚 Use Cases", expanded=False):
        st.markdown("""
        - Homework assistance
        - Mathematical concept explanation
        - Problem solving strategies
        - Research calculations
        - Competitive exam preparation
        """)
    
    st.markdown("---")
    st.markdown("""
    <div style="font-size: 0.8rem; color: #95a5a6;">
        © 2023 MathMind AI | Version 1.0.0<br>
        For support: support@mathmind.ai
    </div>
    """, unsafe_allow_html=True)