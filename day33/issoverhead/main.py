import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 50.450100 
MY_LONG = 30.523399

MY_EMAIL = "getostur@gmail.com"
MY_PASS = "demedimgetostur"


#Your position is within +5 or -5 degrees of the ISS position.
def iss_is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    
def it_is_dark():
    
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    
    if time_now > sunset and time_now < sunrise:
        return True
    else:
        return False



# print(iss_latitude, iss_longitude, sunrise, sunset, time_now )

# run the code every 60 seconds.
while True:
    time.sleep(60)
    if iss_is_close() and it_is_dark():
        message = "ISS is over our head look the sky."
        with smtplib.SMTP("smtp.gmail.com",) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASS)
                connection.sendmail(
                    from_addr=MY_EMAIL, 
                    to_addrs=MY_EMAIL, 
                    msg=f"Subject:ISS is close!\n\n{message}"
                    )
                print("Email sent successfully!")
    else:
        print("ISS is not close.")
    


