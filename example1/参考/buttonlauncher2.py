# -*- coding: utf-8 -*-

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.label import Label

from kivy.lang import Builder
Builder.load_file('buttonlauncher2.kv')

class MyWidget(Widget):
    def __init__(self ,**kwargs):
        super(MyWidget, self).__init__()

class ButtonLauncher2App(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    ButtonLauncher2App().run()