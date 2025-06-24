# 🤖 Simple AI Chatbot using Chainlit + Gemini API

This is a **basic conversational chatbot** powered by the **Gemini 2.0 Flash model** using [Chainlit](https://www.chainlit.io/) for real-time chat interface and the [OpenAI Agents SDK](https://github.com/openai/agents) for agent-based logic.

---

## 🌟 Features

- 🧠 Uses Gemini 2.0 Flash via OpenAI-compatible SDK  
- ⚡ Built with Chainlit – instant interactive frontend  
- 👤 Simple agent logic with modular `Agent`, `Runner`, `RunConfig`  
- 🔐 Secure environment variable loading with `.env`  
- 💬 Chat UI runs locally on browser (`http://localhost:8000`)  

---

## 🛠️ Tech Stack & Tools

| Tool / Library         | Purpose                                           |
|------------------------|---------------------------------------------------|
| 🐍 Python              | Core language                                     |
| 🔐 `python-dotenv`     | Load `.env` file with API key                     |
| ⚡ Chainlit             | Realtime frontend UI                              |
| 🧠 Gemini (via SDK)    | LLM model used for responses                      |
| 🔁 Agents SDK          | Agent-based architecture and runner               |

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/simple-ai-chatbot.git
cd simple-ai-chatbot

2. Create Virtual Environment
bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate       # For Windows

# OR
source .venv/bin/activate    # For macOS/Linux

3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt

4. Setup .env File
Create a .env file in the root folder:

env
Copy
Edit
GEMINI_API_KEY=your_gemini_api_key_here
📌 Get your Gemini API key from https://makersuite.google.com/app/apikey

5. Run the Chat App
bash
Copy
Edit
chainlit run main.py
Then open: http://localhost:8000

🧠 Agent Logic Explained
python
Copy
Edit
my_assistant = Agent(
    name = "AI Assistant",
    instructions = "You are a helpful assistant"
)

➡️ User message → sent to Runner
➡️ Runner executes the agent
➡️ Agent generates output
➡️ Response displayed in Chainlit UI

🖼️ Sample Chat Output
text
Copy
Edit
👋 Welcome to Simple Chatbot! Ask anything.

User: What's HTML?  
AI Assistant: HTML stands for HyperText Markup Language...
🎯 Learning Outcomes
✅ Build a basic LLM chatbot interface with Chainlit
✅ Integrate Gemini via OpenAI-compatible SDK
✅ Use Agent, Runner, RunConfig for agent logic
✅ Load .env securely
✅ Deploy a modular and interactive LLM-based app

🙌 Special Thanks
This chatbot was created as a task for Agentic AI (Quarter 4)
under the Governor’s Initiative for AI & Web 3.0.

👨‍🏫 Mentors:
Sir Ameen Alam | Sir Hamzah Syed | Sir Bilal Muhammad Khan | Sir Aneeq Khatri


## 👨‍💻 Author

**Muhammad Mubashir Saeedi**
🧑‍💼 [LinkedIn](https://www.linkedin.com/in/muhammad-mubashir-saeedi)
🐦 [X (Twitter)](https://x.com/MubashirDev516)
📌 GIAIC Student – Agentic AI Q4


#AgenticAI #Chainlit #GeminiAPI #Python #OpenAI #AIProjects #GIAIC #Quarter4 #GovtInitiative #LLM