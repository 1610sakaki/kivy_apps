# -*- coding: utf-8 -*-

from kivy.app import App

# from kivy.config import Config
from kivy.uix.widget import Widget


class BtnWidget(Widget):
    def on(self):
        print("on!")
        self.ids["btnOn"].background_color = 0.95, 0.30, 0.15, 1.0

    def off(self):
        print("off!")
        self.ids["btnOn"].background_color = 1, 0, 0, 0.4


class GpioApp(App):
    def build(self):
        return BtnWidget()


if __name__ == "__main__":
    GpioApp().run()
