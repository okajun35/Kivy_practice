#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget


class TextWidget(Widget):
    pass

class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'greeting'


if __name__ == '__main__':
	TestApp().run()
