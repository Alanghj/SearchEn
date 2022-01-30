from gui.interfaces import Pop_up, Pop_up_cleaned
from kivy.uix.popup import Popup


def show_popup():
    show = Pop_up()
    popup_window = Popup(title="Warning", content=show, size_hint=(None,None),size=(400,400), title_size=20)
    popup_window.open()


def show_popup_cleaned():
    show = Pop_up_cleaned()
    popup_window = Popup(title="Warning", content=show, size_hint=(None,None),size=(400,400), title_size=20)
    popup_window.open()