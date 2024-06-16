import requests
from datetime import datetime, timedelta
from twilio.rest import Client


account_sid = ''
auth_token = ''
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "VD0WQNRCFHKCF7MS"
NEWS_API_KEY = ""

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

now = datetime.now()
today = now.date()
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=2)

yesterday_str = yesterday.strftime("%Y-%m-%d")
day_before_yesterday_str = day_before_yesterday.strftime("%Y-%m-%d")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY   
}

news_parameters = {
    "q": COMPANY_NAME,
    "searchIn": "title,content",
    "from": day_before_yesterday_str,
    "to": yesterday_str,
    "sortBy": "publishedAt",
    "pageSize": "2",
    "page": 1,
    "apiKey": NEWS_API_KEY
    
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)

news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_response_s = news_response.raise_for_status()
news_response_status = news_response.status_code
news_data = news_response.json()
news_articles = news_data["articles"]
notification_msg = []
for article in news_articles:
    notification_msg.append(f"\nHeadline: {article['title']}\nBrief: {article['description']}\n")

    # notification_msg.append(title = f"\n  Headline: {article['title']}\n")
    # notification_msg.append(desc = f"  Brief: {article['description']}\n")
    # notification_msg.append(content = f"Content: {article['content']}\n")

stock_response_s = stock_response.raise_for_status()
stock_response_status = stock_response.status_code
stock_data = stock_response.json()
stock_data_times = stock_data["Time Series (Daily)"]

stock_data_yesterday = stock_data_times.get(yesterday_str)
stock_data_before_yesterday = stock_data_times.get(day_before_yesterday_str)

if stock_data_yesterday and stock_data_yesterday:
    stock_data_yesterday_high = float(stock_data_yesterday["2. high"])
    stock_data_yesterday_low = float(stock_data_yesterday["3. low"])
    stock_data_before_yesterday_high = float(stock_data_before_yesterday["2. high"])
    stock_data_before_yesterday_low = float(stock_data_before_yesterday["3. low"])
    print(f"Yesterday's High: {stock_data_yesterday_high}")
    print(f"Yesterday's Low: {stock_data_yesterday_low}")
    print(f"Day Before Yesterday's High: {stock_data_before_yesterday_high}")
    print(f"Day Before Yesterday's Low: {stock_data_before_yesterday_low}")
    
    high_diff_percentage = abs((stock_data_yesterday_high - stock_data_before_yesterday_high) / stock_data_before_yesterday_high) * 100
    low_diff_percentage = abs((stock_data_yesterday_low - stock_data_before_yesterday_low) / stock_data_before_yesterday_low) * 100
    
    if high_diff_percentage > 5:
     
        client = Client(account_sid, auth_token)
       
        message = client.messages.create(
        from_='whatsapp:+14155',
        body=f"TSLA:🔺5% The high price changed by {high_diff_percentage:.2f}% from {stock_data_before_yesterday_high} to {stock_data_yesterday_high}, {notification_msg[0]}, {notification_msg[1]}.",
        to='whatsapp:+38063'
        )

        
    elif high_diff_percentage > 0:
        client = Client(account_sid, auth_token)
       
        message = client.messages.create(
        from_='whatsapp:+14155',
        body=f"TSLA:🔺0% The high price changed by {high_diff_percentage:.2f}% from {stock_data_before_yesterday_high} to {stock_data_yesterday_high}, {notification_msg[0]}, {notification_msg[1]}.",
        to='whatsapp:+38063'
        )
    
    else:
        print("No Change: The high price did not change.")
        

    if low_diff_percentage > 5:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        from_='whatsapp:+14155',
        body=f"TSLA:🔻5% The low price changed by {low_diff_percentage:.2f}% from {stock_data_before_yesterday_low} to {stock_data_yesterday_low}, {notification_msg[0]}, {notification_msg[1]}.",
        to='whatsapp:+38063'
        )
    
    elif low_diff_percentage > 0:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        from_='whatsapp:+141552',
        body=f"TSLA:🔻>0% The low price changed by {low_diff_percentage:.2f}% from {stock_data_before_yesterday_low} to {stock_data_yesterday_low}, {notification_msg[0]}, {notification_msg[1]}.",
        to='whatsapp:+38063'
        )
   
    else:
        print("No Change: The low price did not change.")
else:
    print("Data for the specified dates is not available.")


