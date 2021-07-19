import requests
import json
import time
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Label


url_hrktoeur = "https://free.currconv.com/api/v7/convert?q=HRK_EUR&compact=ultra&apiKey=75f83697d28865fde0f4"
url_eurtohrk = "https://free.currconv.com/api/v7/convert?q=EUR_HRK&compact=ultra&apiKey=75f83697d28865fde0f4"

user_input = float(input("Insert a value: "))

try:
    response = requests.get(url_hrktoeur)
    print(f"\nStatus code: {int(response.status_code)}")
    if response.status_code == requests.codes.ok:
        hrktoeur = response.json()["HRK_EUR"]
        eurtohrk = requests.get(url_eurtohrk).json()["EUR_HRK"]
        print(f"1 EUR = {eurtohrk} HRK")
        print(f"1 HRK = {hrktoeur} EUR\n")
        exchange = f"EUR: {round(user_input * hrktoeur, 2)}\nHKR: {round(user_input * eurtohrk, 2)}"
    else:
      hrktoeur = 0.13
      eurtohrk = 7.51
      print ("DISCONNECTED")
      exchange = f"EUR: {round(user_input * hrktoeur, 2)}\nHKR: {round(user_input * eurtohrk, 2)}"
except Exception as e:
    hrktoeur = 0.13
    eurtohrk = 7.51
    print ("NO INTERNET")
    print(e)
    exchange = f"EUR: {round(user_input * hrktoeur, 2)}\nHKR: {round(user_input * eurtohrk, 2)}"

print(exchange)


class Exchange(Widget):
    pass


class ExchangeApp(App):
    def build(self):
        return Exchange()

if __name__ == '__main__':
    ExchangeApp().run()