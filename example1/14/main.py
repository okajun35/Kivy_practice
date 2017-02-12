#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty, ListProperty

class TextWidget(Widget):
    text  = StringProperty()
    color = ListProperty([1,1,1,1])

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = 'start'
        
    def buttonClicked(self):
        self.text = 'Good morning'
        self.color = [1, 0, 0 , 1]

    def buttonClicked2(self):
        self.text = 'Hello'
        self.color = [0, 1, 0 , 1 ]

    def buttonClicked3(self):
        self.text = 'Good evening'
        self.color = [0, 0, 1 , 1 ]

class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'greeting'

if __name__ == '__main__':
	TestApp().run()
