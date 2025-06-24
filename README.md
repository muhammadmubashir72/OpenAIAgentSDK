# Agent Chatbot Variants Overview

## 1️⃣ Simple Agent Chatbot  
- 🔹 **Type:** Single-agent  
- 🧠 **Role:** One “AI Assistant” handles all user queries (general-purpose).  

## 2️⃣ Multi-Agent Chatbot (Web, App, Marketing)  
- 🔹 **Type:** Multi-agent  
- 👥 **Agents:**  
  - **Web Developer Agent** – HTML, CSS, JS, React, Tailwind, etc.  
  - **App Developer Agent** – Flutter, React Native, Android/iOS.  
  - **Marketing Agent** – SEO, social media, ads.  
- 🧭 **Routing:** Manager Agent routes each query to the appropriate expert.  

## 3️⃣ Tool-Calling Multi-Agent Chatbot  
- 🔹 **Type:** Multi-agent + Tool support  
- 👥 **Agents:**  
  - **Greeting Agent** – Responds to greetings (hi/hello → “Salam”).  
  - **Mubashir Info Agent** – Calls `get_mubashir_info()` to return author details.  
  - **Coordinator Agent** – Routes between Greeting and Info agents.  
- 🔧 **Tools:** Uses `@function_tool` to invoke external functions for dynamic data.  
