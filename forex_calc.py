import requests
import json
import time

url_hrktoeur = "https://free.currconv.com/api/v7/convert?q=HRK_EUR&compact=ultra&apiKey=75f83697d28865fde0f4"
url_eurtohrk = "https://free.currconv.com/api/v7/convert?q=EUR_HRK&compact=ultra&apiKey=75f83697d28865fde0f4"

user_input = float(input("Insert a value: "))

try:
    response = requests.get(url_hrktoeur)
    print(f"Status code: {int(response.status_code)}")
    if response.status_code == requests.codes.ok:
        hrktoeur = response.json()["HRK_EUR"]
        eurtohrk = requests.get(url_eurtohrk).json()["EUR_HRK"]
        print(f"1 EUR = {eurtohrk} HRK")
        print(f"1 HRK = {hrktoeur} EUR")
        exchange = user_input * hrktoeur, user_input * eurtohrk
    else:
      hrktoeur = 0.13
      eurtohrk = 7.51
      print ("DISCONNECTED")
      exchange = user_input * hrktoeur, user_input * eurtohrk
except Exception as e:
    hrktoeur = 0.13
    eurtohrk = 7.51
    print ("NO INTERNET")
    exchange = user_input * hrktoeur, user_input * eurtohrk

print(exchange)