import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

# -------------------- CONFIG -------------------- #
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

# -------------------- STEP 1: STOCK DATA -------------------- #
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

try:
    stock_response = requests.get(STOCK_ENDPOINT, params=stock_params, timeout=10)
    stock_response.raise_for_status()
    data = stock_response.json()["Time Series (Daily)"]

    data_list = [value for (key, value) in data.items()]

    yesterday_close = float(data_list[0]["4. close"])
    day_before_close = float(data_list[1]["4. close"])

except Exception as e:
    print("Error fetching stock data:", e)
    exit()

# -------------------- CALCULATE DIFFERENCE -------------------- #
difference = abs(yesterday_close - day_before_close)
diff_percent = (difference / day_before_close) * 100

# Direction symbol
symbol = "🔺" if yesterday_close > day_before_close else "🔻"

# -------------------- STEP 2: GET NEWS -------------------- #
if diff_percent > 0:   # ✅ Correct threshold
    
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
        "sortBy": "publishedAt",
        "language": "en"
    }

    try:
        news_response = requests.get(NEWS_ENDPOINT, params=news_params, timeout=10)
        news_response.raise_for_status()
        articles = news_response.json()["articles"][:3]

    except Exception as e:
        print("Error fetching news:", e)
        exit()

    # -------------------- FORMAT ARTICLES -------------------- #
    formatted_articles = [
    f"{STOCK_NAME}: {symbol}{round(diff_percent, 2)}%\n"
    f"Headline: {article['title']}\n"
    f"Brief: {article['description'] or article['content'] or 'No description available'}"
    for article in articles
    ]

    # -------------------- STEP 3: SEND SMS -------------------- #
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

        for article in formatted_articles:
            message = client.messages.create(
                body=article,
                from_="+12294584364",
                to="+918936820475",
            )
            print("Message sent:", message.sid)

    except Exception as e:
        print("Error sending SMS:", e)

else:
    print("No significant stock change. No news sent.")