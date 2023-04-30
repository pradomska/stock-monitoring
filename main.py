import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "3ZGZQGDVSC8BOLLM"
NEWS_API_KEY = "370ba7b785404b09876fdabc3f7b444d"

ACCOUNT_SID = "ACed99dee86823f4e65269e783a7604e42"
AUTH_TOKEN = "your_auth_token"
TWILIO_NUMBER = "+16205268968"

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params).json()["Time Series (Daily)"]
data = [value for (key, value) in stock_response.items()]
yesterday_data = data[0]
yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)

day_before_yesterday_data = data[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
# print(day_before_yesterday_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
# print(difference)

diff_percent = round((abs(difference) / float(yesterday_closing_price)) * 100)
# print(diff_percent)
if diff_percent > 2.5:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params).json()["articles"]
    three_articles = news_response[:3]
    # print(three_articles)

    formatted_articles = [f"{STOCK_NAME}: {up_down} {difference} %\nHeadline: {item['title']}.\nBrief: {item['description']}" for item in three_articles]
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=TWILIO_NUMBER,
            to="+48*********")
        print(message.status)