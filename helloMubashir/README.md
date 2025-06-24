Here’s a complete and clear `README.md` in Markdown format for your project based on all your code and multi-agent logic:

---

````markdown
# 🤖 Multi-Agent Chatbot using Chainlit + Gemini API (Agentic AI Task)

This project is a **smart AI chatbot** built with **Chainlit**, powered by **Google's Gemini 2.0 Flash model**, and designed using the **OpenAI-compatible Agents SDK**. It intelligently routes queries to specialized agents based on user input — just like a real team of experts! 🚀

---

## 🌟 Features

- 🔀 **Multi-Agent Architecture**: Web, App, Marketing & Manager agents
- ⚙️ **Automatic Agent Routing** using a Coordinator/Router agent
- 🧠 **Gemini LLM via AsyncOpenAI** for powerful responses
- 💬 **Real-time Chat UI** with Chainlit
- 🧩 **Tool Calling Support** via `@function_tool` (e.g., Mubashir Info)
- 🔐 API Key secured using `.env`
- ✅ Modular, readable code structure

---

## 🛠️ Tech Stack

| Tool / Library         | Role                                              |
|------------------------|---------------------------------------------------|
| 🐍 Python              | Core programming language                         |
| 🧠 Gemini API          | LLM backend via Google                             |
| ⚡ Chainlit             | Real-time chat interface                          |
| 🔁 OpenAI Agents SDK   | Agent routing, logic & tools                      |
| 🔐 python-dotenv       | Secure .env file for secrets                      |
| 🔧 asyncio             | Async programming in Python                       |

---

## 👥 Agents Overview

| Agent               | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| 🌐 **Web Developer** | Handles HTML, CSS, JS, React, Next.js, Tailwind, etc.                      |
| 📱 **App Developer** | Answers queries about Flutter, React Native, Android/iOS dev               |
| 📈 **Marketing**     | Assists with SEO, social media, Google/Facebook Ads                        |
| 🧑‍💼 **Manager**       | Handles team, project, and task management queries                        |
| 🤖 **Router/Coordinator** | Selects correct agent automatically based on user input              |
| 🧾 **Mubashir Info Agent** | Uses tool `get_mubashir_info()` to answer questions about the author  |
| 👋 **Greeting Agent** | Responds with Salam when greeted with "hi", "hello", etc.                |

---

## 🚀 How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/multi-agent-chatbot.git
cd multi-agent-chatbot
````

### 2. Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate      # For Windows
# or
source .venv/bin/activate  # For macOS/Linux
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Add `.env` File

```env
GEMINI_API_KEY=your_api_key_here
```

📌 Get your key from [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

---

## 💡 Sample Usage

### Chat-based (Chainlit UI)

```bash
chainlit run main.py
```

Then open: [http://localhost:8000](http://localhost:8000)

### Terminal-based (Multi-Agent Coordination)

```bash
python app.py
```

---

## 🔍 Agent Logic (How It Works)

```text
User Message → Coordinator Agent → Correct Sub-Agent →
Tool (if needed) → Final Response → UI
```

If user asks:

> "How to boost Instagram followers?"

🔁 Coordinator will route to 👉 **Marketing Agent**

---

## 📘 Example Prompts

* `How to center a div using TailwindCSS?` → Web Agent
* `What is the best strategy for Google Ads?` → Marketing Agent
* `How do I manage a remote software team?` → Manager Agent
* `Who is Muhammad Mubashir Saeedi?` → Mubashir Info Agent (Tool Calling)
* `Hello` or `Hi` → Greeting Agent (says Salam)

---

## ✨ What I Learned

* ✅ Created modular agents for real-world domains
* ✅ Auto-agent routing using prompts and logic
* ✅ Connected external APIs as tools
* ✅ Built a full Chainlit UI experience with Gemini
* ✅ Used Agentic AI principles in practice!

---

## 🙌 Acknowledgment

Built as part of the **Agentic AI (Quarter 4)** course at **Governor House**.

**Special thanks to:**

Sir Ameen Alam | Sir Hamzah Syed | Sir Bilal Khan | Sir Aneeq Khatri

---

## 👨‍💻 Author

**Muhammad Mubashir Saeedi**
🧑‍💼 [LinkedIn](https://www.linkedin.com/in/muhammad-mubashir-saeedi)
🐦 [X (Twitter)](https://x.com/MubashirDev516)
📌 GIAIC Student – Agentic AI Q4



#AgenticAI #Chainlit #GeminiAPI #Python #LLM #MultiAgent #OpenAI #WebDev #AppDev #Marketing #GIAIC #GovernorHouse #Quarter4
