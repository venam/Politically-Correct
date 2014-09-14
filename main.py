#!/usr/bin/python

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.listview import ListView
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.carousel import Carousel

import politically_correct


class TitleBar(BoxLayout):

    def __init__(self, **kwargs):
        super(TitleBar, self).__init__(**kwargs)

class Prompt(Label):

    def __init__(self, **kwargs):
        super(Prompt, self).__init__(**kwargs)
        
class MainMenu(BoxLayout):

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)

class TextEntry(BoxLayout):

    def __init__(self, **kwargs):
        super(TextEntry, self).__init__(**kwargs)

class ResultEntry(BoxLayout):

    def __init__(self, **kwargs):
        super(ResultEntry, self).__init__(**kwargs)


class Dictionary(BoxLayout):

    def __init__(self, **kwargs):
        super(Dictionary, self).__init__(**kwargs)

        inf = ""
        for word in politically_correct.word_list:
            inf+=word

        txts = TextInput(text = inf, background_color = (0.15, 0.15, 0.15, 1),
            foreground_color = (1, 1, 1, 1), multiline = True, readonly = True,
            size_hint = (1.0, None))
        txts.bind(minimum_height=txts.setter('height'))
        scroll = ScrollView(size_hint = (1, 1), size = (self.width, self.height))
        scroll.add_widget(txts)
        self.add_widget(scroll)


class MainScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        title = TitleBar()

        self.carousel = Carousel(direction='right', loop=False)
        self.spacing=10

        dico = Dictionary()
        self.carousel.add_widget(dico)

        self.m = MainMenu()
        self.m.convert_button.bind(on_release=self.convert)
        self.m.dictionary_button.bind(on_release=self.dictionary)
        self.carousel.add_widget(self.m)
        self.carousel.load_slide(self.m)

        self.textEntry = TextEntry()
        self.textEntry.paragraph_button.bind(on_press=self.convert_paragraph)
        self.carousel.add_widget(self.textEntry)

        self.result = ResultEntry()
        self.result.back.bind(on_press=self.back)
        self.carousel.add_widget(self.result)

        self.add_widget(title)
        self.add_widget(self.carousel)


    def convert(self, object):
        self.carousel.load_next()

    def dictionary(self, object):
        self.carousel.load_previous()

    def back(self, object):
        self.carousel.load_slide(self.m)

    def convert_paragraph(self, object):
        old_text = self.textEntry.paragraph.text
        new_text = politically_correct.polit_changer(old_text)
        self.result.paragraph.text = new_text
        self.carousel.load_next()


class PoliticallyCorrecterApp(App):

    def build(self):
        win = MainScreen()
        Window.clearcolor = (0.15, 0.15, 0.15, 1)
        return win


if __name__ == '__main__':
  PoliticallyCorrecterApp().run()

