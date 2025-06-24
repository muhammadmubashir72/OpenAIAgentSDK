
import os
from dotenv import load_dotenv 
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner, RunConfig, function_tool
import chainlit as cl
import asyncio

load_dotenv()

MODEL_NAME = "gemini-2.0-flash"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

@function_tool
def get_mubashir_info():
    return "Mubashir Saeedi is a Software Engineer and learn Agentic AI"

async def main():
    # Create a External Client
    external_client = AsyncOpenAI(
        api_key = GEMINI_API_KEY,
        base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
    ) 

    # Create a Model
    model = OpenAIChatCompletionsModel(
        openai_client = external_client,
        model = MODEL_NAME
    )

    # Create a Config
    config = RunConfig(
        model = model,
        model_provider = external_client,
        tracing_disabled = True
    )

    my_assistant = Agent(
        name = "My Assistant",
        instructions = "You are a helpful assistant. Solve the user's queries in a clear and concise way."
        # model = model
    )

    greeting_agent = Agent(
    name = "Greeting Agent",
    instructions = "you are a greeting agent, your task is to say Salam, when someone says hello, hi, or anything similar"
    )

    mubashir_info_agent = Agent(
        name = "Mubashir Info Agent",
        instructions = 
        "you are a helpful assistant for Muhammad Mubashir Saeedi"
        "Your task is help to users understand about him"
        "you ALWAYS use get_mubashir_info tools to get the information about mubashir",
        tools=[get_mubashir_info]   
    )

    coordinator_agent = Agent(
        name = "Coordinator Agent",
        instructions = 
        "you are routing/Coordinator Agent"
        "your task is to use the given agents to answer the users quetions",
        handoffs=[greeting_agent, mubashir_info_agent]
    )
    
    query = input("Enter a prompt: ")
    result = await Runner.run(
        coordinator_agent, query, run_config=config
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
