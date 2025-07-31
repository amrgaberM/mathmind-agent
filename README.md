# MathMind Agent

**MathMind Agent** is a functional AI assistant that answers math-related questions using a combination of large language models and custom tools. Built with **LangChain**, powered by **Groq**, and wrapped in a simple **Streamlit UI**, it demonstrates how LLM-based agents can be extended with tool-calling capabilities to perform real mathematical reasoning beyond simple text generation.

This project marks the **first version** of a more advanced system under development. The architecture is modular and designed for future extensions like memory, multi-step reasoning, and deployment.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)](https://langchain.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red.svg)](https://streamlit.io)
---

## Tech Stack

| Component | Tool/Library |
|-----------|--------------|
| **Language Model** | Groq (LLM backend) |
| **Agent Framework** | LangChain |
| **Tool Integration** | Custom Python tools (e.g. calculator) |
| **Web Interface** | Streamlit |
| **Environment Management** | python-dotenv |
| **Language** | Python |

---

## Features

- **Math-aware LLM agent** - Intelligent mathematical reasoning and problem solving
- **Custom tool integration** - Extensible tool system via LangChain
- **Web-based UI** - Clean, intuitive interface using Streamlit
- **Secure configuration** - Environment variables for API keys and settings
- **Modular architecture** - Well-structured codebase for easy expansion

---

## Project Structure

```
mathmind-agent/
├── app.py                    # Streamlit application entry point
├── requirements.txt          # Python dependencies
├── .env.example             # Environment configuration template
├── README.md                # Project documentation
├── math-mind_agent/
│   ├── __init__.py
│   ├── agent_executor.py    # Core agent logic and initialization
│   ├── tools.py               # Mathematical computation tools
│   │   
│   ├── prompt.py              # LLM prompt templates
```

---

## Quick Start

### Prerequisites
- Python 3.8 or higher
- Groq API key ([Get yours here](https://groq.com))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/mathmind-agent.git
   cd mathmind-agent
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Access the interface**
   Open your browser to `http://localhost:8501`

---

## Usage Examples

### Basic Mathematical Queries
- "What is the derivative of x² + 3x - 5?"
- "Solve the equation 2x + 7 = 15"
- "Calculate the area of a circle with radius 5"

### Complex Problem Solving
- "A ball is thrown upward with initial velocity 20 m/s from height 1.5m. When will it hit the ground?"
- "Find the intersection points of y = x² and y = 2x + 3"

---

## Development Roadmap

### Version 1.1 (Next Release)
- Add conversational memory for multi-turn interactions
- Expand toolset 
- Improve prompt engineering logic
- Enhanced error handling and user feedback

### Version 1.2 (Future)
- UI enhancements and better visual design
- Graph plotting capabilities
- Export functionality for solutions

### Version 2.0 (Long-term)
- Public deployment to Streamlit Cloud or Hugging Face Spaces
- Advanced multi-step reasoning capabilities
- Integration with additional mathematical computation backends
- Custom tool creation interface

---

## Contact

**Project Maintainer** - Aspiring Machine Learning Engineer  
Focused on practical AI applications with strong interest in AI agents and LLM tooling. Open to feedback and collaboration opportunities.

- **GitHub**: [@amrgaberM](https://github.com/amrgaberM)
- **LinkedIn**: [Amr Hassan](https://www.linkedin.com/in/amrhassangaber/)
- **Email**: amrgabeerr20@gmail.com

For questions, suggestions, or collaboration opportunities, feel free to reach out!
