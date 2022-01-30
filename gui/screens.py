from gui.interfaces import Engine_search, Result_search, Menu_app
from kivy.uix.screenmanager import ScreenManager, Screen
from gui.popup import show_popup, show_popup_cleaned
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from bots.bot_scraper import search_item
from kivy.core.window import Window


class Window_manager(ScreenManager):
    def __init__(self, **kwargs):
        super(Window_manager, self).__init__(**kwargs)
        self.window = Window
        self.window.size = (480, 600)

    def get_window(self):
        self.window.minimum_width, self.window.minimum_height = self.window.size
        return self.window

  
class Menu_screen(Screen):
    window_view = Window_manager()
    window_view.get_window()
    menu = Menu_app()

    
class Second_window(Screen):
    intel = Engine_search()

    def __init__(self, **kwargs):
        super(Second_window, self).__init__(**kwargs)
        self.term_search = ObjectProperty(None)

    def search_term(self):
        if self.term_search.text == '' or self.term_search.text == 'What do you want search for?':
            show_popup()
        else:
            open("content/content.txt", "w").close()
            self.manager.get_screen('screen_result').show_search.text = ''
            self.manager.get_screen('screen_result').labelText = ''

            self.search_items = search_item
            self.search_items(self.term_search.text)
            
            self.term_search.text = 'What do you want search for?'
            self.manager.current = 'screen_result'
            self.manager.transition.direction = "left"


    def show_search(self):
        with open('content/content.txt', 'r', encoding='utf-8') as f:
            self.contents = f.read()
        self.manager.get_screen('screen_result').labelText = self.contents
        
     
class Third_window(Screen):
    result_sr = Result_search()
    labelText = StringProperty('')

    def __init__(self, **kwargs):
        super(Third_window, self).__init__(**kwargs)
        self.show_search = ObjectProperty(None)

    def clean_search(self):
        if self.ids.show_search.text != '':
            open("content/content.txt", "w").close()
            self.ids.show_search.text = ''
            self.labelText = ''
        else:
            show_popup_cleaned()


