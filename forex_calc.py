import requests
import json

url_hrktoeur = "https://free.currconv.com/api/v7/convert?q=HRK_EUR&compact=ultra&apiKey=75f83697d28865fde0f4"
url_eurtohrk = "https://free.currconv.com/api/v7/convert?q=EUR_HRK&compact=ultra&apiKey=75f83697d28865fde0f4"
hrktoeur = 0.13
eurtohrk = 7.51

response = requests.get(url_hrktoeur)
print(response.json()["HRK_EUR"])
response = requests.get(url_eurtohrk)
print(response.json()["EUR_HRK"])



user_input = float(input("Wie viele Kuna? "))

exchange = user_input * hrktoeur

print(exchange)

import requests
import time

while True:
    try:
        response = requests.get(url_hrktoeur)
        print(int(response.status_code))
        if response.status_code == requests.codes.ok:
            hrktoeur = 0.13
        else:
                print ("DISCONNECTED")
        time.sleep(1)
    except Exception as e:
        print ("NO INTERNET")
        print (str(e))