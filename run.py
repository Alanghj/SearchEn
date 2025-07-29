from gui.screens import Window_manager
from kivy.lang import Builder
from kivy.app import App


kv = Builder.load_file('style/main.kv')


class MyApp(App):
    def build(self):
        return Window_manager()


if __name__ == "__main__":
    MyApp().run()
    