import requests
from datetime import datetime, timedelta
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "6A6L233KGBP8R6Y8"
NEWS_API_KEY = "01941b135f914f4eba82ad58b4ea1060"

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
print(news_articles)

stock_response_s = stock_response.raise_for_status()
stock_response_status = stock_response.status_code
stock_data = stock_response.json()
stock_data_times = stock_data["Time Series (Daily)"]
# stock_data_yesterday = stock_data["Time Series (Daily)"]["yesterday"]
# stock_data_before_yesterday = stock_data["Time Series (Daily)"]["day_before_yesterday"]
stock_data_yesterday = stock_data_times.get(yesterday_str)
stock_data_before_yesterday = stock_data_times.get(day_before_yesterday_str)
# print(stock_response_s, stock_response_status, stock_data_times, today, yesterday, day_before_yesterday)
# print(stock_data_yesterday, stock_data_before_yesterday)

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
        print(f"Important Notification: The high price changed by {high_diff_percentage:.2f}% from {stock_data_before_yesterday_high} to {stock_data_yesterday_high}")
    elif high_diff_percentage > 0:
        print(f"Not Important Notification: The high price changed by {high_diff_percentage:.2f}% from {stock_data_before_yesterday_high} to {stock_data_yesterday_high}")
    else:
        print("No Change: The high price did not change.")
        
        
        
    if low_diff_percentage > 5:
        print(f"Important Notification: The low price changed by {low_diff_percentage:.2f}% from {stock_data_before_yesterday_low} to {stock_data_yesterday_low}")
        
    elif low_diff_percentage > 0:
        print(f"Not Important Notification: The low price changed by {low_diff_percentage:.2f}% from {stock_data_before_yesterday_low} to {stock_data_yesterday_low}")
    else:
        print("No Change: The low price did not change.")
else:
    print("Data for the specified dates is not available.")


# print(stock_data_yesterday_high, stock_data_yesterday_low, stock_data_before_yesterday_high, stock_data_before_yesterday_low)

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

