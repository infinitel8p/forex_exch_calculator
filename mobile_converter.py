from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar

class ConverterApp(MDApp):
    def flip(self):
        print("working")

    def build(self):
        screen = MDScreen()

        self.toolbar = MDToolbar(title = "HRK to EUR converter")
        self.toolbar.pos_hint = {"top" : 1}
        self.toolbar.right_action_items = [
            ["rotate-3d-variant", lambda x : self.flip()]
            ]
        screen.add_widget(self.toolbar)

        #UI Widgets go here
        return screen

if __name__ == '__main__':
    ConverterApp().run()