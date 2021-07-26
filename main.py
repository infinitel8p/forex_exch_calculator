from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
import requests

url_hrktoeur = "https://free.currconv.com/api/v7/convert?q=HRK_EUR&compact=ultra&apiKey=75f83697d28865fde0f4"
url_eurtohrk = "https://free.currconv.com/api/v7/convert?q=EUR_HRK&compact=ultra&apiKey=75f83697d28865fde0f4"
hrktoeur = 0.13
eurtohrk = 7.51
class ConverterApp(MDApp):
    def flip(self):
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "EUR to HRK converter"
            self.input.hint_text = "Enter the value in EUR"
            self.input.text = ""
            self.label.text = ""
            self.converted.text = ""
        else:
            self.state = 0
            self.toolbar.title = "HRK to EUR converter"
            self.input.hint_text = "Enter the value in HRK"
            self.input.text = ""
            self.label.text = ""
            self.converted.text = ""

    def convert(self, args):
        if self.state == 0:
            val = round(float(self.input.text) * hrktoeur, 2)
            self.label.text = "is in EUR:"
            self.converted.text = str(val)
        if self.state == 1:
            val = round(float(self.input.text) * eurtohrk, 2)
            self.label.text = "is in HRK:"
            self.converted.text = str(val)

    def build(self):
        self.state = 0
        self.theme_cls.primary_palette = "DeepPurple"
        screen = MDScreen()


        #top toolbar
        self.toolbar = MDToolbar(title = "HRK to EUR converter")
        self.toolbar.pos_hint = {"top" : 1}
        self.toolbar.right_action_items = [
            ["rotate-3d-variant", lambda x : self.flip()]]
        screen.add_widget(self.toolbar)


        #connection status label
        self.status_label = MDLabel(
            halign="right",
            pos_hint = {"center_x": 0.485, "center_y":0.84},
            theme_text_color = "Hint",
            text = "Checking connection...",
            #font_size = 12,
            font_style = "Caption"
            )
        screen.add_widget(self.status_label)

        try:
            response = requests.get(url_hrktoeur)
            print(f"\nStatus code: {int(response.status_code)}")
            global hrktoeur, eurtohrk
            if response.status_code == requests.codes.ok:
                global hrktoeur, eurtohrk
                hrktoeur = response.json()["HRK_EUR"]
                eurtohrk = requests.get(url_eurtohrk).json()["EUR_HRK"]
                self.status_label.text = f"Status {int(response.status_code)}: CONNECTED\n1 EUR = {eurtohrk} HRK\n1 HRK = {hrktoeur} EUR"
            else:
                self.status_label.theme_text_color = "Error"
                self.status_label.text = f"Status {int(response.status_code)}: DISCONNECTED\n1 EUR = {eurtohrk} HRK\n1 HRK = {hrktoeur} EUR"
        except Exception as e:
                self.status_label.theme_text_color = "Error"
                self.status_label.text = f"Status error: NO INTERNET\n1 EUR = {eurtohrk} HRK\n1 HRK = {hrktoeur} EUR"


        #logo
        screen.add_widget(Image
            (source = "logo.png",
            pos_hint = {"center_x" : 0.5, "center_y" : 0.7},
            size_hint = (0.35, 0.35)
            )
        )


        #user input
        self.input = MDTextField(
            #font_size = 22,
            hint_text = "Enter the value in HRK",
            helper_text = "Please use . insted of , for cents",
            helper_text_mode = "on_focus",
            halign = "center",
            icon_right = "calculator",
            multiline = False,
            on_text_validate = self.convert,
            pos_hint = {"center_x" : 0.5, "center_y" : 0.45},
            size_hint = (0.8, 1)
        )
        screen.add_widget(self.input)


        #convert button
        screen.add_widget(MDFillRoundFlatButton(
            text = "CONVERT",
            #font_size = 17,
            pos_hint = {"center_x" : 0.5, "center_y" : 0.15},
            on_press = self.convert
            )
        )

        #more labels
        self.label = MDLabel(
            halign = "center",
            pos_hint = {"center_x" : 0.5, "center_y" : 0.35},
            theme_text_color = "Secondary"
        )
        screen.add_widget(self.label)
        self.converted = MDLabel(
            halign = "center",
            pos_hint = {"center_x" : 0.5, "center_y" : 0.3},
            theme_text_color = "Primary",
            font_style = "H5"
        )
        screen.add_widget(self.converted)


        return screen

if __name__ == '__main__':
    ConverterApp().run()