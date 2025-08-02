import streamlit as st
from mathmind_agent.agent_executor import agent_executor
import time

# Configure page settings
st.set_page_config(
    page_title="MathMind AI | Intelligent Mathematics Assistant",
    page_icon="∫",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/yourrepo/mathmind',
        'Report a bug': "https://github.com/yourrepo/mathmind/issues",
        'About': "MathMind AI - Professional mathematics assistant powered by advanced AI"
    }
)

# Enhanced Modern CSS - Optimized & Compact
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    :root {
        --primary: linear-gradient(135deg, #0070f3 0%, #00dfd8 50%, #7c3aed 100%);
        --glass: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
        --shadow-glow: 0 25px 50px -12px rgba(0,112,243,0.25);
        --shadow-xl: 0 20px 25px -5px rgba(0,0,0,0.1);
    }
    
    .stApp {
        background: radial-gradient(ellipse at top, rgba(0,112,243,0.1) 0%, transparent 50%),
                   radial-gradient(ellipse at bottom, rgba(124,58,237,0.1) 0%, transparent 50%),
                   linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: white;
        min-height: 100vh;
    }
    
    /* Animated Background */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle at 25% 25%, rgba(0,112,243,0.1) 0%, transparent 25%),
                   radial-gradient(circle at 75% 75%, rgba(124,58,237,0.08) 0%, transparent 25%);
        background-size: 800px 800px, 600px 600px;
        animation: bgFloat 20s ease-in-out infinite;
        pointer-events: none;
        z-index: 0;
    }
    
    @keyframes bgFloat {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        33% { transform: translateY(-10px) rotate(1deg); }
        66% { transform: translateY(5px) rotate(-0.5deg); }
    }
    
    /* Hero Section */
    .hero-section {
        background: var(--glass);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 32px;
        padding: 4rem 3rem;
        margin: 2rem 0;
        box-shadow: var(--shadow-xl), var(--shadow-glow);
        text-align: center;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    
    .hero-section:hover {
        transform: translateY(-5px);
        box-shadow: var(--shadow-xl), 0 0 30px rgba(124,58,237,0.4);
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%; left: -50%; width: 200%; height: 200%;
        background: conic-gradient(from 0deg, transparent, rgba(0,112,243,0.1), transparent 30%);
        animation: heroRotate 20s linear infinite;
        z-index: 0;
    }
    
    .hero-content { position: relative; z-index: 2; }
    
    @keyframes heroRotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* 3D Hero Icon */
    .hero-icon {
        width: 120px; height: 120px;
        margin: 0 auto 2rem;
        background: var(--primary);
        border-radius: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 3rem;
        color: white;
        font-weight: 300;
        box-shadow: 0 30px 60px rgba(0,0,0,0.2),
                   0 0 0 1px rgba(255,255,255,0.1),
                   inset 0 1px 0 rgba(255,255,255,0.2);
        animation: iconFloat 8s ease-in-out infinite;
        position: relative;
    }
    
    .hero-icon::after {
        content: '';
        position: absolute;
        width: 160px; height: 160px;
        border: 2px solid rgba(255,255,255,0.1);
        border-radius: 40px;
        animation: iconOrbit 12s linear infinite;
        z-index: -1;
    }
    
    @keyframes iconFloat {
        0%, 100% { transform: translateY(0px) rotateY(0deg); }
        25% { transform: translateY(-15px) rotateY(5deg); }
        75% { transform: translateY(-10px) rotateY(-5deg); }
    }
    
    @keyframes iconOrbit {
        0% { transform: rotate(0deg) scale(1); opacity: 0.3; }
        100% { transform: rotate(360deg) scale(1); opacity: 0.3; }
    }
    
    /* Typography */
    .hero-title {
        font-size: 3.5rem;
        font-weight: 900;
        background: var(--primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
        line-height: 1.1;
        animation: titleGlow 4s ease-in-out infinite alternate;
    }
    
    @keyframes titleGlow {
        0% { filter: drop-shadow(0 0 10px rgba(0,112,243,0.5)); }
        100% { filter: drop-shadow(0 0 20px rgba(124,58,237,0.5)); }
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: rgba(255,255,255,0.8);
        font-weight: 400;
        line-height: 1.6;
        max-width: 600px;
        margin: 0 auto;
    }
    
    /* Chat Container */
    .chat-container {
        background: var(--glass);
        backdrop-filter: blur(25px);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 24px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: var(--shadow-xl), 0 0 0 1px rgba(255,255,255,0.05);
        min-height: 500px;
        transition: all 0.3s ease;
    }
    
    .chat-container:hover {
        box-shadow: var(--shadow-xl), 0 0 30px rgba(0,112,243,0.2);
    }
    
    /* Chat Header */
    .chat-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-bottom: 1.5rem;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 1.5rem;
        position: relative;
    }
    
    .chat-header::after {
        content: '';
        position: absolute;
        bottom: -1px; left: 0;
        width: 80px; height: 2px;
        background: var(--primary);
        border-radius: 1px;
        animation: headerLine 3s ease-in-out infinite;
    }
    
    @keyframes headerLine {
        0%, 100% { width: 80px; opacity: 0.7; }
        50% { width: 150px; opacity: 1; }
    }
    
    .chat-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: white;
    }
    
    /* Status Indicator */
    .status-indicator {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 0.9rem;
        font-weight: 600;
        padding: 0.5rem 1rem;
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 50px;
        backdrop-filter: blur(10px);
        color: white;
    }
    
    .status-dot {
        width: 8px; height: 8px;
        border-radius: 50%;
        background: #10b981;
        box-shadow: 0 0 8px rgba(16,185,129,0.5);
        animation: statusPulse 2s ease-in-out infinite;
    }
    
    @keyframes statusPulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.2); opacity: 0.8; }
    }
    
    /* Enhanced Chat Messages */
    .stChatMessage {
        padding: 1.5rem !important;
        margin: 1rem 0 !important;
        border-radius: 18px !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        transition: all 0.3s ease !important;
        position: relative !important;
    }
    
    .stChatMessage:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 15px 30px rgba(0,0,0,0.2) !important;
    }
    
    .stChatMessage[data-testid="user-message"] {
        background: var(--primary) !important;
        color: white !important;
        margin-left: 15% !important;
        box-shadow: 0 8px 25px rgba(0,112,243,0.3) !important;
    }
    
    .stChatMessage[data-testid="assistant-message"] {
        background: var(--glass) !important;
        backdrop-filter: blur(20px) !important;
        margin-right: 15% !important;
        border-left: 3px solid #0070f3 !important;
        color: white !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2) !important;
    }
    
    /* Premium Input */
    .stChatInput > div > div > div > div {
        border-radius: 18px !important;
        border: 2px solid rgba(255,255,255,0.1) !important;
        padding: 1.2rem 1.5rem !important;
        font-size: 1rem !important;
        background: var(--glass) !important;
        backdrop-filter: blur(20px) !important;
        color: white !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2) !important;
        transition: all 0.3s ease !important;
    }
    
    .stChatInput > div > div > div > div::placeholder {
        color: rgba(255,255,255,0.6) !important;
    }
    
    .stChatInput > div > div > div > div:focus {
        border-color: #0070f3 !important;
        box-shadow: 0 0 0 3px rgba(0,112,243,0.2) !important,
                   0 12px 30px rgba(0,112,243,0.3) !important;
        transform: translateY(-1px) !important;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: linear-gradient(135deg, rgba(15,15,35,0.95) 0%, rgba(26,26,46,0.95) 100%) !important;
        border-right: 1px solid rgba(255,255,255,0.1) !important;
        backdrop-filter: blur(20px) !important;
    }
    
    .sidebar-header {
        text-align: center;
        padding: 2rem 1rem;
        background: var(--glass);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 18px;
        margin-bottom: 1.5rem;
        backdrop-filter: blur(15px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        position: relative;
        overflow: hidden;
    }
    
    .sidebar-header::before {
        content: '';
        position: absolute;
        top: -50%; left: -50%; width: 200%; height: 200%;
        background: conic-gradient(from 0deg, transparent, rgba(0,112,243,0.1), transparent 30%);
        animation: sidebarRotate 15s linear infinite;
        z-index: 0;
    }
    
    .sidebar-header > * { position: relative; z-index: 1; }
    
    @keyframes sidebarRotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .sidebar-logo {
        width: 70px; height: 70px;
        background: var(--primary);
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 1rem;
        font-size: 1.8rem;
        color: white;
        box-shadow: 0 12px 30px rgba(0,112,243,0.4);
        animation: logoFloat 6s ease-in-out infinite;
    }
    
    @keyframes logoFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
    }
    
    .sidebar-title {
        font-size: 1.5rem;
        font-weight: 800;
        color: white;
        margin-bottom: 0.5rem;
    }
    
    .sidebar-subtitle {
        font-size: 0.9rem;
        color: rgba(255,255,255,0.7);
        font-weight: 500;
    }
    
    /* Feature Cards */
    .feature-card {
        background: var(--glass);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 14px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        backdrop-filter: blur(15px);
        transition: all 0.3s ease;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .feature-card:hover {
        transform: translateY(-3px) scale(1.01);
        box-shadow: 0 15px 30px rgba(0,112,243,0.2);
        border-color: rgba(0,112,243,0.3);
    }
    
    .feature-icon {
        width: 45px; height: 45px;
        background: var(--primary);
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1rem;
        font-size: 1.3rem;
        color: white;
        box-shadow: 0 6px 15px rgba(0,112,243,0.3);
    }
    
    .feature-title {
        font-size: 1rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.5rem;
    }
    
    .feature-description {
        font-size: 0.85rem;
        color: rgba(255,255,255,0.8);
        line-height: 1.5;
    }
    
    /* Loading Animation */
    .loading-container {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 3rem;
        flex-direction: column;
        gap: 1.5rem;
    }
    
    .loading-spinner {
        width: 50px; height: 50px;
        border: 3px solid rgba(255,255,255,0.1);
        border-top: 3px solid #0070f3;
        border-right: 3px solid #7c3aed;
        border-radius: 50%;
        animation: spin 1.5s linear infinite;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .loading-text {
        color: rgba(255,255,255,0.9);
        font-weight: 600;
        font-size: 1rem;
        animation: textPulse 2s ease-in-out infinite;
    }
    
    @keyframes textPulse {
        0%, 100% { opacity: 0.7; }
        50% { opacity: 1; }
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-section { padding: 2.5rem 2rem; }
        .hero-title { font-size: 2.5rem; }
        .hero-subtitle { font-size: 1.1rem; }
        .hero-icon { width: 90px; height: 90px; font-size: 2.2rem; }
        .chat-container { padding: 1.5rem; }
        .stChatMessage[data-testid="user-message"] { margin-left: 5% !important; }
        .stChatMessage[data-testid="assistant-message"] { margin-right: 5% !important; }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "processing" not in st.session_state:
    st.session_state.processing = False

# Sidebar
with st.sidebar:
    st.markdown("""
    <div class="sidebar-header">
        <div class="sidebar-logo">∫</div>
        <div class="sidebar-title">MathMind</div>
        <div class="sidebar-subtitle">AI Assistant</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature Cards
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🧮</div>
        <div class="feature-title">Advanced Calculations</div>
        <div class="feature-description">Solve complex mathematical problems with step-by-step explanations</div>
    </div>
    
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">Data Visualization</div>
        <div class="feature-description">Generate interactive graphs and mathematical visualizations</div>
    </div>
    
    <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">Problem Solving</div>
        <div class="feature-description">Get detailed solutions for algebra, calculus, and more</div>
    </div>
    
    <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <div class="feature-title">Instant Results</div>
        <div class="feature-description">Fast, accurate mathematical computations powered by AI</div>
    </div>
    """, unsafe_allow_html=True)

# Main content
st.markdown("""
<div class="hero-section">
    <div class="hero-content">
        <div class="hero-icon">∫</div>
        <h1 class="hero-title">MathMind AI</h1>
        <p class="hero-subtitle">Your intelligent mathematics assistant powered by advanced AI. Solve complex problems, visualize data, and explore mathematical concepts with ease.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Chat interface
st.markdown("""
<div class="chat-container">
    <div class="chat-header">
        <div class="chat-title">🤖 Mathematics Assistant</div>
        <div class="status-indicator">
            <div class="status-dot"></div>
            <span>Online</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me any mathematics question..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Process with agent
    with st.chat_message("assistant"):
        with st.spinner("🔄 Processing your mathematical query..."):
            try:
                st.session_state.processing = True
                
                # Simulate processing time for demo
                time.sleep(1)
                
                # Execute agent (replace with actual agent call)
                response = agent_executor.invoke({"input": prompt})
                
                # Extract response
                if isinstance(response, dict) and "output" in response:
                    assistant_response = response["output"]
                else:
                    assistant_response = str(response)
                
                st.markdown(assistant_response)
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
                
            except Exception as e:
                error_message = f"❌ An error occurred: {str(e)}"
                st.error(error_message)
                st.session_state.messages.append({"role": "assistant", "content": error_message})
            
            finally:
                st.session_state.processing = False

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem 0; color: rgba(255,255,255,0.6); font-size: 0.9rem;">
    <p>🔬 Powered by Advanced AI • Built with Streamlit • © 2024 MathMind AI</p>
</div>
""", unsafe_allow_html=True)