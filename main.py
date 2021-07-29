from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from Basic_Tricks import tricklist as basic_tricks
from Grind_Slide_Tricks import tricklist as grind_tricks
import random

done_tricks = []

class ConverterApp(MDApp):
    def flip(self):
        global done_tricks
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "Flatground Tricks"
            self.converted.text = ""
            self.trick_label.text = ""
            self.stance_label.text = ""
            done_tricks = []
        else:
            self.state = 0
            self.toolbar.title = "Grind and Slide Tricks"
            self.converted.text = ""
            self.trick_label.text = ""
            self.stance_label.text = ""
            done_tricks = []

    def convert(self, args):
        if self.state == 0:
            tricks = [i for i in basic_tricks if i not in done_tricks]
            new_trick = (random.choice(tricks))
            done_tricks.append(new_trick)
            self.trick_label.text = new_trick[0]
            self.stance_label.text = f"Stance: {new_trick[1]}"
        if self.state == 1:
            tricks = [i for i in grind_tricks if i not in done_tricks]
            new_trick = (random.choice(tricks))
            done_tricks.append(new_trick)
            self.trick_label.text = new_trick[0]
            self.stance_label.text = f"Stance: {new_trick[1]}"

    def build(self):
        self.state = 0
        self.new_game = 0
        self.theme_cls.primary_palette = "BlueGray"
        screen = MDScreen()


        #top toolbar
        self.toolbar = MDToolbar(title = "Flatground Tricks")
        self.toolbar.pos_hint = {"top" : 1}
        self.toolbar.right_action_items = [
            ["rotate-3d-variant", lambda x : self.flip()]]
        screen.add_widget(self.toolbar)


        #logo
        screen.add_widget(Image
            (source = "logo.png",
            pos_hint = {"center_x" : 0.5, "center_y" : 0.7},
            size_hint = (0.35, 0.35)
            )
        )


        #user input
        self.trick_label = MDLabel(
            #font_size = 22,
            text = "",
            halign = "center",
            pos_hint = {"center_x" : 0.5, "center_y" : 0.5},
            size_hint = (0.8, 1.2),
            font_style = "H4"
        )
        screen.add_widget(self.trick_label)

        #more labels
        self.stance_label = MDLabel(
            text = "",
            halign = "center",
            pos_hint = {"center_x" : 0.5, "center_y" : 0.45},
            theme_text_color = "Secondary"
        )
        screen.add_widget(self.stance_label)

        self.letters_label = MDLabel(
            text = "Letters: None",
            halign = "center",
            pos_hint = {"center_x" : 0.5, "center_y" : 0.3},
            theme_text_color = "Primary",
            font_style = "H5"
        )
        screen.add_widget(self.letters_label)


        #new trick button
        screen.add_widget(MDFillRoundFlatButton(
            text = "New Trick",
            #font_size = 17,
            pos_hint = {"center_x" : 0.5, "center_y" : 0.15},
            on_press = self.convert
            )
        )

        return screen

if __name__ == '__main__':
    ConverterApp().run()