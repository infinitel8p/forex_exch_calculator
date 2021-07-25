from kivy.lang import Builder

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp

KV = '''
MDBoxLayout:

    ScreenManager:

        MDScreen:

            # Will always be at the bottom of the screen.
            MDBottomAppBar:

                MDToolbar:
                    title: "Title"
                    icon: "git"
                    type: "bottom"
                    mode: "end"
                    left_action_items: [["menu", lambda x: x]]
                    on_action_button: app.callback(self.icon)
'''

class ContentNavigationDrawer(MDBoxLayout):
    pass

class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()