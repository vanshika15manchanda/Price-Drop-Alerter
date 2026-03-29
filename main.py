import requests          
from bs4 import BeautifulSoup
import json
import smtplib
import schedule
import time
import os
from dotenv import load_dotenv

load_dotenv()

def save_data(url ,price):
    data = {
        "url"  : url ,
        "price" : price
    }
    with open("data.json" , "w") as file:
        json.dump(data,file)

def load_data():
    try:
        with open("data.json" , "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None  

def send_email(message):
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")

    with smtplib.SMTP("smtp.gmail.com" , 587) as connection:
        connection.starttls()
        connection.login(EMAIL , PASSWORD)

        connection.sendmail(
            from_addr = EMAIL,
            to_addrs = EMAIL,
            msg = f"Subject: Price Alert!\n\n{message}"

        )

def check_price():
       headers = {
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
       "Accept-Language": "en-IN,en;q=0.9"
    }
       
       url =  'https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html'
       
       old_data = load_data()
       
       if old_data:
           old_price = old_data["price"]
           print("Old Price: "  , old_price)
       else:
           print("No previous data found")
       
       
       response = requests.get(url , headers = headers)
       response.encoding = 'utf-8'
       #print(response.status_code)
       soup = BeautifulSoup(response.text , "html.parser")
       #print(soup.title)
       
       price = soup.find("p", class_="price_color")
       
       if price:
           current_price = float(price.text.replace("£", ""))
           print("Current Price : " ,current_price )
       
           
           save_data(url , current_price)
       
           #comparing prices
           if old_data:
               old_price = old_data["price"]
           
               if current_price < old_price:
                   print("Price dropped!!")
                   send_email(f"Price dropped to {current_price} !\n Check: {url}")
               else:
                   print("No price drop")
       
       
       else:
           print("Price not found 😢")
   
if __name__ == "__main__":
    schedule.every(1).hours.do(check_price)

    while True:
       schedule.run_pending()
       time.sleep(1)
