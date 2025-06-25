## 🤖 Agent Chatbot Variants (Summary)

### 1️⃣ Simple Agent
- 🧠 Handles all user queries as one AI assistant.
- ✅ Best for general-purpose Q&A.

### 2️⃣ Multi-Agent (Web, App, Marketing)
- 👥 Separate agents for each skill:
  - Web Developer (HTML, CSS, JS, React)
  - App Developer (Flutter, Android/iOS)
  - Marketing (SEO, social media, ads)
- 🧭 A **Manager Agent** routes the query to the right expert.

### 3️⃣ Multi-Agent + Tool Calling
- 🛠️ Combines agents with `@function_tool` for dynamic tasks:
  - Greeting Agent (hi/hello → "Salam")
  - Mubashir Info Agent (`get_mubashir_info()` tool)
  - Coordinator Agent handles routing

### 4️⃣ Crypto Price Agent (Tool-Powered)
- 💸 Fetches real-time crypto prices via CoinGecko API
- 🔎 Understands natural & Roman Urdu queries (e.g. `eth to inr`)
- ⚙️ Uses `@function_tool` → `get_crypto_price(coin, currency)`
- 📡 Built using Gemini API + Chainlit + Streamlit versions
