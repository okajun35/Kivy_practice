#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.listview import ListItemButton
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path


# 国立国会図書館サーチ外部提供インタフェース（API）
from pyndlsearch.client import SRUClient
from pyndlsearch.cql import CQL

# デフォルトに使用するフォントを変更する
resource_add_path('./fonts')
#resource_add_path('/storage/emulated/0/kivy/calc/fonts')
LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf') #日本語が使用できるように日本語フォントを指定する


class BookButton(ListItemButton):
    ''' search_results（ListView）の項目をボタンにする '''
    book = ListProperty()

class SearchBookForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()   # kvファイル側のsearch_results（ListView）を監視

    def __init__(self, **kwargs):
        super(SearchBookForm, self).__init__(**kwargs)


    def books_args_converter(index, data_item):
        ''' 検索結果を book名をキーとした辞書型に変換する。
             検索結果のレコード分呼ばれて実行される。
        '''
         
        title, creater , language, publisher = data_item
        return {'book': (title, creater , language, publisher )}

    def search_book(self):
        ''' 検索条件をもとに検索し、結果をListViewに格納する '''
    
        print('search_book')
        
        cql = CQL()
        
        # ★検索条件を入力していく
        cql.title = self.search_input.text

        year  = self.ids['year'].text
        month = self.ids['month'].text
        day = self.ids['day'].text


        cql.fromdate = year + '-' + month + '-' + day # 出版年月日
        #cql.fromdate = '2000-10-10'
        #print(cql.payload())
        #cql.title = 'Python'
        #cql.fromdate = '2000-10-10'
        # NDL Searchクライアントの設定
        
        client = SRUClient(cql)
        client.set_maximum_records(int(self.ids['number'].text))  #最大取得件数
        # ★検索条件入力終了
        
        #client.set_maximum_records(10)  #最大取得件数
        #print(client)

        # get_response()ではxml形式で取得可能
        #res = client.get_response()
        #print(res.text)

        # SRU実行（入力条件を元に検索を実行する）
        srres = client.get_srresponse()

        # 検索結果をbooksリストに格納
        books = [(d.recordData.title, d.recordData.creator, d.recordData.language, d.recordData.publisher) for d in srres.records]
        print(books)
        
        print("----------------")
        # 検索結果に格納する
        
        self.search_results.adapter.data.clear()       # 検索結果をdata（詳細表示用）を消去
        self.search_results.adapter.data.extend(books) # 検索結果をdataに追加
        self.search_results._trigger_reset_populate()  # search_results（list_view）をリフレッシュ
        

class BookInfo(BoxLayout):
    ''' 詳細画面の情報 '''
    book = ListProperty(['', '','',''])

class BookSearchRoot(BoxLayout):

    def __init__(self, **kwargs):
        super(BookSearchRoot, self).__init__(**kwargs)

    def show_book_info(self, book):
        ''' 選択した情報を整形して詳細画面へ移動して表示する '''
        print('BookSearchRoot')
    
        print(book) #Book = BookButton()の値、取れているか確認用
        
        # LabelのTextにNoneが入るとエラーになるために変換を行う
        book_convs = [x if x != None else '' for x in book] # Noneが返ってきた場合は""に変更する

        # 詳細画面に書籍情報を格納
        self.bookinfo.book = book_convs
        
        # 詳細画面に移動
        self.carousel.load_slide(self.bookinfo)

class BookSearchApp(App):

    def __init__(self, **kwargs):
        super(BookSearchApp, self).__init__(**kwargs)

        self.title = '国会図書館検索'
    pass

if __name__ == '__main__':
	BookSearchApp().run()
