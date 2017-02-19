# -*- coding: utf-8 -*
from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '800')


import kivy
kivy.require('1.9.1')

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.core.window import Window
from kivy.properties import BooleanProperty
from kivy.utils import get_color_from_hex
from kivy.resources import resource_add_path

from kivy.factory import Factory

#from kivy.core.window import Window
#Window.size = (450, 600)

# デフォルトに使用するフォントを変更する
resource_add_path('fonts')
LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf') #日本語が使用できるように日本語フォントを指定する


class Calculator1(BoxLayout):

    clear_bool = BooleanProperty(False)

    def print_number(self, number):
        '''入力された値が入る'''
        if self.clear_bool:
            self.clear_display()

        text = "{}{}".format(self.display.text, number) # 今までの入力された文字列と入力された値が表示される
        self.display.text = text

        print("数字「{0}」が押されました".format(number))

    def print_operator(self, operator):
        if self.clear_bool:
            self.clear_bool = False

        text = "{} {} ".format(self.display.text, operator)
        self.display.text = text

        print("演算子「{0}」が押されました".format(operator))

    def print_point(self, operator):
        # 「.」が押されれた場合の処理

        print("（未実装）演算子「{0}」が押されました".format(operator))

    def clear_display(self):
        self.display.text = ""
        self.clear_bool = False

        print("「c」が押されました")
    def del_char(self):
        ''' "<x"を押された場合の計算結果を表示  '''

        self.display.text = self.display.text[:-1]

        print("「<x」が押されました")

    def calculate(self):
        ''' "="を押された場合の計算結果を表示  '''
        try:
            self.display.text = str(eval(self.display.text)) # 単一の式を評価  例：eval("5 + 10")　は15になる
            self.clear_bool = True

            print('計算完了')
        except:
            # 数字を入力せずに　'=’を押した場合などのエラー対策
            print('error　入力ミス')


#class Calculator2(BoxLayout):
#    def __init__(self, **kwargs):
#        super(Calculator2, self).__init__(**kwargs)




class CalculatorRoot(BoxLayout):
    def __init__(self, **kwargs):
        super(CalculatorRoot, self).__init__(**kwargs)

    def change_calc(self):   
        self.clear_widgets()
        self.add_widget(Calculator1())

    def change_calc2(self):   
        self.clear_widgets()
        calc2 = Factory.Calculator2()
        #calc2 = Calculator2()

        self.add_widget(calc2)



class CalculatorApp(App): 
    def __init__(self, **kwargs):
        super(CalculatorApp, self).__init__(**kwargs)

        self.title = '電卓'
    pass


if __name__ == "__main__":
    Window.clearcolor = get_color_from_hex('#FFFFFF')
    CalculatorApp().run()
