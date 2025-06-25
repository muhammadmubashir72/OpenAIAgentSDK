import os
from dotenv import load_dotenv
from agents import Runner, Agent, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from agents.run import RunConfig
import requests

load_dotenv()

MODEL_NAME = "gemini-2.0-flash"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
     raise RuntimeError ("API key not found")
@function_tool
async def get_crypto_price(coin: str = "bitcoin", currency: str = "usd") -> str:
    """
     Get crypto Price from API
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price = data.get(coin, {}).get(currency)
        return f"The current price of {coin.capitalize()} is {price} {currency.upper()}." if price else "Invalid coin or currency."

    
    
external_client =  AsyncOpenAI(
    api_key =  GEMINI_API_KEY,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    openai_client = external_client,
    model = MODEL_NAME
)

config = RunConfig(
    model= model,
    model_provider = external_client,
    tracing_disabled = True
)

crypto_agent = Agent(
    name = "Crypto Agent",
    instructions = "You are a helpful assistant",
    tools = [get_crypto_price]
)

query = input("Enter a question to crpto price: ")
result = Runner.run_sync(crypto_agent, query, run_config = config)
print(result.final_output)