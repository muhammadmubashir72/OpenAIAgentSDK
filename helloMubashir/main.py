import os
import chainlit as cl
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, RunConfig, OpenAIChatCompletionsModel

load_dotenv()

MODEL_NAME = "gemini-2.0-flash"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# --- Config Setup ---
external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model=MODEL_NAME,
    openai_client=external_client
)

config = RunConfig(model=model, model_provider=external_client, tracing_disabled=True)

# --- Agents Setup ---
agents = {
    "manager": Agent("Manager", "You manage projects and teams."),
    "web": Agent("Web Dev", "You answer web development questions."),
    "app": Agent("App Dev", "You answer mobile app development questions."),
    "marketing": Agent("Marketing", "You help with SEO, ads, and social media."),
}

# --- Start Message ---
@cl.on_chat_start
async def start():
    await cl.Message(
        content=(
            "👋 Welcome! I can help with:\n"
            "- 🧑‍💼 Project Management\n"
            "- 🌐 Web Development\n"
            "- 📱 App Development\n"
            "- 📈 Digital Marketing\n\n"
            "💬 Ask me anything naturally.\n"
            "👨‍💻 *By Muhammad Mubashir*"
        )
    ).send()

# --- Main Handler ---
@cl.on_message
async def handle_message(message: cl.Message):
    try:
        user_input = message.content.strip().lower()

        # Help prompt
        if any(kw in user_input for kw in ["tum kya kar sakte", "help", "services", "what can you do"]):
            await cl.Message(
                content=(
                    "🤖 I can help you with:\n"
                    "- Project Management\n"
                    "- Web Development\n"
                    "- App Development\n"
                    "- Digital Marketing\n\n"
                    "Just ask your question!"
                )
            ).send()
            return

        # Ask model which agent to use
        selector_prompt = (
            f"User asked: '{user_input}'\n"
            "Pick one: manager, web, app, or marketing."
        )
        agent_key = (await Runner.run(Agent("Router", selector_prompt), "", config)).final_output.strip().lower()

        if agent_key not in agents:
            await cl.Message(content="❗ I didn't get that. Try again.").send()
            return

        result = await Runner.run(agents[agent_key], user_input, config)
        await cl.Message(content=result.final_output).send()

    except Exception as e:
        await cl.Message(content=f"❌ Error: {e}").send()



import os 
import chainlit as cl
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, RunConfig, OpenAIChatCompletionsModel

load_dotenv()

MODEL_NAME = "gemini-2.0-flash"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key = GEMINI_API_KEY,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model = MODEL_NAME,
    openai_client = external_client
)

config = RunConfig(
    model = model,
    model_provider = external_client,
    tracing_disabled = True
)

# Single agent
# my_assitant = Agent(
#     name = "AI Assitant",
#     instructions = "You are helpful a assitant",
#     # model = model
# )

# Multiple agent
agents = {
    "manager": Agent(name="Manager", instructions="You are a project manager. Handle tasks, teams, and productivity."),
    "web": Agent(name="Web Developer", instructions="You are a web developer. Answer questions related to HTML, CSS, JavaScript, Nextjs, Reactjs etc and web frameworks."),
    "app": Agent(name="App Developer", instructions="You are a mobile app developer. Provide help on Flutter, React Native Android, and iOS development."),
    "marketing": Agent(name="Digital Marketing", instructions="You are a digital marketing expert. Help with SEO, social media, content marketing, and advertising."),
}


@cl.on_chat_start
async def start():
    await cl.Message(
        content=(
            "👋 Welcome to the Multi-Agent AI Chatbot!\n\n"
            "I can help you with:\n"
            "- 🧑‍💼 Project Management\n"
            "- 🌐 Web Development\n"
            "- 📱 App Development\n"
            "- 📈 Digital Marketing\n\n"
            "💬 Just ask your question naturally, like:\n"
            "→ How to create a responsive navbar?\n"
            "→ How to increase followers on Instagram?\n"
            "→ How to manage a remote development team?\n"
            "→ How to add Firebase to a Flutter app?\n\n"
            "🤖 I’ll automatically route your query to the right expert.\n\n"
            "👨‍💻 *Created by Muhammad Mubashir*"
        )
    ).send()

@cl.on_message
async def handle_message(message: cl.Message):
    try:
        user_input = message.content.strip().lower()

        # 🆘 If user is asking about bot's capabilities
        help_triggers = [
            "help", "tum kya kar sakte ho", "kya kar sakte ho", "kya karte ho", "services", 
            "what can you do", "who are you", "kya tum kya ho"
        ]
        if any(trigger in user_input for trigger in help_triggers):
            await cl.Message(
                content=(
                    "🤖 I can help you with:\n\n"
                    "- 🧑‍💼 Project management (Manager agent)\n"
                    "- 🌐 Web development (Web Developer agent)\n"
                    "- 📱 App development (App Developer agent)\n"
                    "- 📈 Digital marketing (Marketing expert agent)\n\n"
                    "Just ask your question naturally!"
                )
            ).send()
            return

        # 🧠 Use LLM to auto-select agent based on message
        selector_prompt = (
            f"Given the user input: '{user_input}', choose the most suitable category:\n"
            "- manager: for project management, teams, planning\n"
            "- web: for web development (HTML, CSS, JavaScript, Nextjs, Reactjs)\n"
            "- app: for mobile app development (Flutter, React Native)\n"
            "- marketing: for SEO, social media, and marketing\n\n"
            "Respond with ONLY one word: manager, web, app, or marketing."
        )

        selector_result = await Runner.run(
            Agent(name="Router", instructions=selector_prompt),
            input="",
            run_config=config
        )
        selected_agent_key = selector_result.final_output.strip().lower()

        if selected_agent_key not in agents:
            await cl.Message(content="❗ I couldn't understand which expert should reply. Please rephrase.").send()
            return

        selected_agent = agents[selected_agent_key]
        result = await Runner.run(selected_agent, input=message.content, run_config=config)
        await cl.Message(content=result.final_output).send()

    except Exception as e:
        await cl.Message(content=f"❌ Error: {e}").send()

# result = Runner.run_sync(my_assitant,"how are you", run_config = config)
# print(result.final_output)
