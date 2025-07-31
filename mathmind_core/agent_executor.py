# mathmind_agent/agent_executor.py

import os
import logging
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import AgentExecutor, create_tool_calling_agent
from mathmind_agent.tools import get_enhanced_math_tools  # ✅ You must define this
from mathmind_agent.prompts import enhanced_prompt         # ✅ You must define this

# Load env vars
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set in your .env file")

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize LLM
llm = ChatGroq(
    api_key=groq_api_key,
    model_name="llama3-70b-8192"
)

# Load tools and prompt
tools = get_enhanced_math_tools()   # ⬅ must return a list of LangChain tools
prompt = enhanced_prompt            # ⬅ must be a ChatPromptTemplate

# Create agent + executor
agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
