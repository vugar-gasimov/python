import requests

from twilio.rest import Client



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "6A6L233KGBP8R6Y8"

NEWS_API_KEY = ""

TWILIO_SID = ''
TWILIO_AUTH_TOKEN = ''

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# N1

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY   
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)

data = stock_response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

#  N2
before_yesterday_data = data_list[1]
before_yesterday_closing_price = before_yesterday_data["4. close"]


# N3
difference = float(yesterday_closing_price) - float(before_yesterday_closing_price)
# befpre abs-4.460000000000008  after 4.460000000000008
up_down = None
if difference > 0:
    up_down = '🔺'
else:
    up_down = '🔻'
# N4
diff_percent = round((difference / float(yesterday_closing_price)) * 100)


#  N5
if abs(diff_percent) > 2:
    
    # N6
    
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "searchIn": "title,content",
        # "from": day_before_yesterday_str,
        # "to": yesterday_str,
        "sortBy": "publishedAt",
        "pageSize": "3",
        "page": 1,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    
    articles = news_response.json()["articles"]
    
    # N7
    three_articles = articles[:3] 
   
    # N8
    formatted_articles = [f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}." for article in three_articles]
    # N9
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    
    # N10
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+180386',
            to='+38063',
        )
