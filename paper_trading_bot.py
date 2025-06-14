
import json
from flask import Flask, request
import requests
import datetime

app = Flask(__name__)

# ✅ Your Telegram credentials
TELEGRAM_BOT_TOKEN = "8001032388:AAE-2k-ixahbRNITX_0sOxId_PLKDJyFNJU"
TELEGRAM_CHAT_ID = "7606414310"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    symbol = data.get("ticker", "Unknown")
    side = data.get("side", "BUY/SELL")
    price = data.get("price", "N/A")
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    message = (
        f"🔔 *Trade Alert* 🔔\n"
        f"Symbol: {symbol}\n"
        f"Side: {side}\n"
        f"Price: {price}\n"
        f"Time: {time}"
    )
    
    send_telegram_message(message)
    return "OK", 200
