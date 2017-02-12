# -*- coding: utf-8 -*-

import kivy

from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

#from kivy.lang import Builder
#Builder.load_file('buttonlauncher.kv')

class MyWidget(GridLayout):
    def __init__(self):
        super(MyWidget, self).__init__()

class ButtonLauncherApp(App):
    def build(self):
        return MyWidget()
#    def build(self):
#        self.root = MyWidget()
#        root = self.root
#        return root

if __name__ == '__main__':
    ButtonLauncherApp().run()