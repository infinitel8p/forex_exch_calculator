from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineIconListItem:
                text: "Screen 1"
                on_release:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

                IconLeftWidget:
                    icon: "language-python"

            OneLineIconListItem:
                text: "Screen 2"
                on_release:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"

                IconLeftWidget:
                    icon: "gitlab"

MDScreen:
    MDBottomAppBar:

        MDToolbar:
            id: toolbar
            title: "Menu"
            icon: "pokeball.png"
            type: "bottom"
            mode: "end"
            elevation: 10
            left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
            on_action_button: app.callback("test")

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"

                MDLabel:
                    text: "Screen 1"
                    halign: "center"

            MDScreen:
                name: "scr 2"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''

class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def callback(self, instance):
        print("working " + instance)

TestNavigationDrawer().run()