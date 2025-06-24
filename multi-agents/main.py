import os
import asyncio
import chainlit as cl
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig, function_tool

# Load environment variables
load_dotenv()
MODEL_NAME = "gemini-2.0-flash"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# External client setup (Gemini endpoint)
external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Model setup
model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model=MODEL_NAME,
)

# Run config
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Agents setup
agents = {
    "web": Agent(
        name="Web Developer Agent",
        instructions="You are responsible for answering questions related to web development, including HTML, CSS, JavaScript, React, Next.js, TailwindCSS, Bootstrap, and other similar topics."
    ),
    "app": Agent(
        name="App Developer Agent",
        instructions="You handle questions related to mobile app development, including Flutter, React Native, and similar technologies."
    ),
    "marketing": Agent(
        name="Marketing Agent",
        instructions="You help users with digital marketing topics such as SEO, Facebook/Google Ads, social media strategies, and content marketing."
    ),
}

# Manager agent with handoffs
manager_agent = Agent(
    name="Manager Agent",
    instructions=(
        "You are a manager agent. Your job is to understand the user's query and route it to the appropriate agent "
        "depending on whether it's related to web development, app development, or marketing. Delegate the task to the correct agent accordingly."
    ),
    handoffs=list(agents.values())
)

# 🔰 Welcome message when chat starts
@cl.on_chat_start
async def on_start():
    await cl.Message(
        content="👋 Welcome to the Multi-Agent Assistant!\nAsk me anything about:\n- 🌐 Web Development\n- 📱 App Development\n- 📈 Digital Marketing"
    ).send()

# Chainlit message handlerimport asyncio

@cl.on_message
async def handle_message(message: cl.Message):
    query = message.content

    msg = cl.Message(content="🤖 Thinking... Please wait")
    await msg.send()

    result = await Runner.run(manager_agent, query, run_config=config)

    # Step 3: Update that message with the final response
    msg.content = result.final_output
    await msg.update()
