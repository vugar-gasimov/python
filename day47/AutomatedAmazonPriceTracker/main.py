
import os
import lxml
import smtplib
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')  
load_dotenv(dotenv_path)

target_price = 71.00

PRODUCT_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
MY_ACCEPT_LANGUAGE = "en-US,en;q=0.9,de-DE;q=0.8,de;q=0.7,uk;q=0.6"
MY_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASS = os.getenv("MY_PASS")

headers = {
    'User-Agent' : MY_USER_AGENT,
    'Accept-Language' : MY_ACCEPT_LANGUAGE
}
response = requests.get(url=PRODUCT_URL, headers=headers)

webpage = response.text

soup = BeautifulSoup(webpage, 'lxml')

product_price = soup.select_one(selector='td span span')
price_text = product_price.text.strip()
numeric_price = price_text.replace('$', '')

product_title = soup.select_one(selector='div h1 span')
full_title = product_title.text.strip()
short_title = full_title.split(',')[0]

if float(numeric_price) <= target_price:
    message = f"Product '{short_title}' is now {price_text}"
    print(message)
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Amazon Price Alert!\n\n{message}\n{PRODUCT_URL}".encode("utf-8")
        )
        