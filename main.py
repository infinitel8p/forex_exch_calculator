from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import requests

url_hrktoeur = "https://free.currconv.com/api/v7/convert?q=HRK_EUR&compact=ultra&apiKey=75f83697d28865fde0f4"
url_eurtohrk = "https://free.currconv.com/api/v7/convert?q=EUR_HRK&compact=ultra&apiKey=75f83697d28865fde0f4"

class ForexConvert(App):
    def build(self):
        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # image widget
        #self.window.add_widget(Image(source="logo.png"))

        # label widget
        try:
            response = requests.get(url_hrktoeur)
            print(f"\nStatus code: {int(response.status_code)}")
            global hrktoeur, eurtohrk
            if response.status_code == requests.codes.ok:
                hrktoeur = response.json()["HRK_EUR"]
                eurtohrk = requests.get(url_eurtohrk).json()["EUR_HRK"]
                status = f"Status {int(response.status_code)}: CONNECTED\n1 EUR = {eurtohrk} HRK\n1 HRK = {hrktoeur} EUR"
            else:
                hrktoeur = 0.13
                eurtohrk = 7.51
                status = f"Status {int(response.status_code)}: DISCONNECTED\n1 EUR = {eurtohrk} HRK\n1 HRK = {hrktoeur} EUR"
        except Exception as e:
                hrktoeur = 0.13
                eurtohrk = 7.51
                status = f"Status error: NO INTERNET\n1 EUR = {eurtohrk} HRK\n1 HRK = {hrktoeur} EUR"
        self.display_status = Label(
                        text= status,
                        font_size= 18,
                        color= '#8800FF'
                        )
        self.window.add_widget(self.display_status)

        # text input widget
        self.user = TextInput(
                    multiline= False,
                    padding_y= (20,20),
                    size_hint= (1, 0.25)
                    )
        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
                      text= "Umrechnen",
                      size_hint= (1,0.25),
                      bold= True,
                      background_color ='#8800FF',
                      #remove darker overlay of background colour
                      #background_normal = ""
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        self.display_status.text = f"EUR: {round(float(self.user.text) * hrktoeur, 2)}\nHKR: {round(float(self.user.text) * eurtohrk, 2)}"

# run Forex App calls
if __name__ == "__main__":
    ForexConvert().run()