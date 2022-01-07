import os
from kivy.core.window import Window
from kaki.app import App
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.properties import NumericProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.utils import get_color_from_hex
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.toolbar import MDToolbar
from manager_screens import ManagerScreens
from kivy.clock import Clock 
Window.size=(350,600)

class Content1(BoxLayout):
    pass
class Content2(BoxLayout):
    pass
class Content3(BoxLayout):
    pass
class Content4(BoxLayout):
    pass
class HotReloadApp(App, MDApp):
    dialog = None
    KV_FILES = {
        os.path.join(os.getcwd(), 'hotreloadd', 'manager_screens.kv'),
        os.path.join(os.getcwd(), 'hotreloadd', 'hotreload.kv'),
    }

    CLASSES = {
        "ManagerScreens": 'screenmanager',
        "HotReload": 'hotreload',
    }
    AUTORELOADER_PATHS = [(os.getcwd(), {"recursive": True})]

    DEBUG = 1
    score = NumericProperty(0) 
    
    def build_app(self):
        Window.bind(on_keyboard=self._rebuild)
        self.manager_screens = ManagerScreens()
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "600"
        self.theme_cls.accent_palette = "DeepOrange"
        self.theme_cls.accent_hue = "600"
        return self.manager_screens

    def on_start(self):
        Clock.schedule_once(self.callback, 60)
    def callback(self, dt):
        self.manager_screens.get_screen('hotreload').ids.earn_btn.disabled = False


    def withdraw_paypal(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="PayPal",
                type="custom",
                content_cls=Content1(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog.open()

    def withdraw_payoneer(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Payoneer",
                type="custom",
                content_cls=Content2(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog.open()

    def withdraw_orange(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Orange",
                type="custom",
                content_cls=Content3(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog.open()

    def withdraw_iam(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Iam",
                type="custom",
                content_cls=Content4(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog.open()
    
    def _rebuild(self, *args):
        if args[1] == 32:
            self.rebuild()


HotReloadApp().run()
