#-*- coding: utf-8 -*-
from kivy.config import Config
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

# デフォルトに使用するフォントを変更する
resource_add_path('./fonts')
LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf') #日本語が使用できるように日本語フォントを指定する

resource_add_path('./image')


class ImageWidget(Widget):
    source = StringProperty(None)
    
    def __init__(self, **kwargs):
        super(ImageWidget, self).__init__(**kwargs)
        pass
        
    def buttonClicked(self):
        self.source= './image/sample.jpg'

    def buttonClicked2(self):
        self.source = 'sample2.jpg'

    def buttonClicked3(self):
        self.source = 'sample3.jpg'

        
class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = '画像表示'

if __name__ == '__main__':
	TestApp().run()
