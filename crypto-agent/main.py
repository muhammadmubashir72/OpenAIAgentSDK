import streamlit as st
import requests
import re

# Page setup
st.set_page_config(page_title="🪙 Mubashir's Crypto Checker", layout="centered")

# ----- STYLISH HEADER -----
st.markdown("""
    <h1 style="text-align:center; color:black;">🚀 Mubashir's Smart Crypto Price Checker</h1>
    <p style="text-align:center; font-size:18px;">Use dropdowns or ask in your own style — even Roman Urdu 💬</p>
""", unsafe_allow_html=True)

# ---------- COIN ID MAP ----------
COIN_MAP = {
    "btc": "bitcoin",
    "eth": "ethereum",
    "ether": "ethereum",
    "etherem": "ethereum",
    "doge": "dogecoin",
    "bnb": "binancecoin",
    "sol": "solana",
    "usdt": "tether",
    "xrp": "ripple",
    "ada": "cardano"
}

# ---------- UTILITY FUNCTIONS ----------
def clean_input(text: str) -> str:
    return re.sub(r'[^a-zA-Z0-9\-]', '', text.lower())

def parse_query(query: str):
    """Extract coin and currency from natural language query"""
    query = query.lower()
    coin = None
    currency = None

    for key in COIN_MAP:
        if key in query:
            coin = COIN_MAP[key]
            break

    for curr in ["usd", "inr", "eur", "pkr", "gbp"]:
        if curr in query:
            currency = curr
            break

    return coin, currency

def get_price(coin: str, currency: str) -> str:
    coin = clean_input(COIN_MAP.get(coin, coin))
    currency = clean_input(currency)

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"
    try:
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            price = data.get(coin, {}).get(currency)
            if price:
                return f"💰 **{coin.capitalize()}** is trading at **{price} {currency.upper()}**"
            else:
                return "❌ Invalid coin or currency."
        return "⚠️ API error."
    except:
        return "❌ Something went wrong."

# ---------- TABS ----------
tab1, tab2 = st.tabs(["🧭 Smart Search", "🔘 Manual Select"])

# ---------- Tab 1: Smart Search ----------
with tab1:
    st.subheader("🗣️ Ask anything...")
    user_query = st.text_input("Type your question:", placeholder="e.g. What is the price of btc in usd?")
    if st.button("Get Price", key="smart"):
        coin, currency = parse_query(user_query)
        if coin and currency:
            st.success(get_price(coin, currency))
        else:
            st.error("Could not understand your input. Try like: `eth to usd` or `bitcoin in inr`.")

# ---------- Tab 2: Manual Mode ----------
with tab2:
    st.subheader("🎯 Choose coin & currency")
    col1, col2 = st.columns(2)
    with col1:
        coin = st.selectbox("Select Coin", list(COIN_MAP.values()), index=0)
    with col2:
        currency = st.selectbox("Select Currency", ["usd", "inr", "eur", "gbp", "pkr"], index=0)

    if st.button("Get Price", key="manual"):
        st.success(get_price(coin, currency))

# ---------- Footer ----------
st.markdown("""
    <hr>
    <p style="text-align:center;">Made with ❤️ by <b>Mubashir Saeedi</b> | Powered by CoinGecko</p>
""", unsafe_allow_html=True)


