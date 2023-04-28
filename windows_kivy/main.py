# -*- coding: utf-8 -*
import os

import japanize_kivy
import kivy
from kivy.app import App

# 日本語フォント表示対応
from kivy.core.text import DEFAULT_FONT, LabelBase
from kivy.core.window import Window
from kivy.factory import Factory

# 画面ごとに分離してバラで読み込む
from kivy.lang import Builder
from kivy.resources import resource_add_path
from kivy.uix.boxlayout import BoxLayout

from window1 import Window1  # 追加
from window2 import Window2  # 追加

# resource_add_path("{}\\{}".format(os.environ["SYSTEMROOT"], "Fonts"))
# LabelBase.register(DEFAULT_FONT, "MSGOTHIC.ttc")

Builder.load_file("window1.kv")
Builder.load_file("window2.kv")


class MainRoot(BoxLayout):
    window1 = None
    window2 = None

    def __init__(self, **kwargs):
        # 起動時に各画面を作成して使い回す
        self.window1 = Factory.Window1()
        self.window2 = Factory.Window2()
        super().__init__(**kwargs)
        # super(MainRoot, self).__init__(**kwargs)
        self.change_disp()  # 追加

    def change_disp(self):
        self.clear_widgets()
        self.add_widget(self.window1)

    def change_disp2(self):
        self.clear_widgets()
        self.add_widget(self.window2)


class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.title = "画面切り替えテスト"

    pass


if __name__ == "__main__":
    MainApp().run()
