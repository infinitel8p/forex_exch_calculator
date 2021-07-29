from kivymd.uix import screen
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton, MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from Basic_Tricks import tricklist as basic_tricks
from Grind_Slide_Tricks import tricklist as grind_tricks
import random

done_tricks = []

class SkateApp(MDApp):
    def flip(self):
        global done_tricks
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "Flatground Tricks"
            self.stance_label.text = ""
            self.letters_label.text = ""
            done_tricks = []
        else:
            self.state = 0
            self.toolbar.title = "Grind and Slide Tricks"
            self.trick_label.text = ""
            self.stance_label.text = ""
            done_tricks = []

    def display_trick(self, args):
        if self.new_game == 0:
            self.landed_trick_button = MDFloatingActionButton(
                icon = "check",
                md_bg_color = [11/255,156/255,49/255,1],
                pos_hint = {"center_x" : 0.75, "center_y" : 0.15},
                on_press = self.landed_trick
            )
            self.screen.add_widget(self.landed_trick_button)

            self.failed_trick_button = MDFloatingActionButton(
                icon = "window-close",
                md_bg_color = "red",
                pos_hint = {"center_x" : 0.25, "center_y" : 0.15},
                on_press = self.failed_trick
            )
            self.screen.add_widget(self.failed_trick_button)

            self.letters_label.text = "Letters: None"
            self.new_game = 1

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

    def landed_trick(self, args):
        self.trick_count += 1
        self.display_trick(args)

    def reset_app(self, args):
        global done_tricks
        self.screen.remove_widget(self.new_game_button)
        self.screen.add_widget(self.new_trick_button)
        self.state = 0
        self.new_game = 0
        self.letters = 0
        self.trick_count = 0
        done_tricks = []
        self.letters_label.text = ""
        self.stance_label.text = ""
        self.trick_label.text = ""
        self.trick_label.theme_text_color = "Primary"

    def failed_trick(self, args):
        self.trick_count += 1
        self.letters += 1
        if self.letters == 1:
            self.letters_label.text = "Letters: S."
            self.display_trick(args)
        if self.letters == 2:
            self.letters_label.text = "Letters: S.K."
            self.display_trick(args)
        if self.letters == 3:
            self.letters_label.text = "Letters: S.K.A"
            self.display_trick(args)
        if self.letters == 4:
            self.letters_label.text = "Letters: S.K.A.T."
            self.display_trick(args)
        if self.letters == 5:
            self.trick_label.theme_text_color = "Custom"
            self.trick_label.text_color = [207/255,0/255,13/255,1]
            self.trick_label.text = "Letters: S.K.A.T.E"
            self.stance_label.text = f"Stats: You landed {self.trick_count - 5} of {self.trick_count} Tricks! (Skipped: {len(done_tricks) - self.trick_count})"
            self.letters_label.text = "Start a new game!"
            self.screen.remove_widget(self.landed_trick_button)
            self.screen.remove_widget(self.failed_trick_button)
            self.screen.remove_widget(self.new_trick_button)
            self.screen.add_widget(self.new_game_button)

    def build(self):
        self.state = 0
        self.new_game = 0
        self.letters = 0
        self.trick_count = 0
        self.theme_cls.primary_palette = "BlueGray"
        self.screen = MDScreen()


        #top toolbar
        self.toolbar = MDToolbar(title = "Flatground Tricks")
        self.toolbar.pos_hint = {"top" : 1}
        self.toolbar.right_action_items = [
            ["rotate-3d-variant", lambda x : self.flip()]]
        self.screen.add_widget(self.toolbar)


        #logo
        self.screen.add_widget(Image
            (source = "logo.png",
            pos_hint = {"center_x" : 0.5, "center_y" : 0.7},
            size_hint = (0.35, 0.35)
            )
        )


        #trick name
        self.trick_label = MDLabel(
            theme_text_color = "Primary",
            font_style = "H5",
            font_size = 15,
            text = "",
            halign = "center",
            pos_hint = {"center_x" : 0.5, "center_y" : 0.5},
            size_hint = (0.8, 1.2)
        )
        self.screen.add_widget(self.trick_label)


        #more labels
        self.stance_label = MDLabel(
            text = "",
            halign = "center",
            pos_hint = {"center_x" : 0.5, "center_y" : 0.45},
            theme_text_color = "Secondary"
        )
        self.screen.add_widget(self.stance_label)

        self.letters_label = MDLabel(
            text = "",
            halign = "center",
            pos_hint = {"center_x" : 0.5, "center_y" : 0.3},
            theme_text_color = "Primary",
            font_style = "H6"
        )
        self.screen.add_widget(self.letters_label)


        #new trick button
        self.new_trick_button = MDFillRoundFlatButton(
            text = "New Trick",
            #font_size = 17,
            pos_hint = {"center_x" : 0.5, "center_y" : 0.15},
            on_press = self.display_trick
        )
        self.screen.add_widget(self.new_trick_button)

        #new game button
        self.new_game_button = MDFillRoundFlatButton(
            text = "New Game",
            #font_size = 17,
            pos_hint = {"center_x" : 0.5, "center_y" : 0.15},
            on_press = self.reset_app)

        return self.screen

if __name__ == '__main__':
    SkateApp().run()