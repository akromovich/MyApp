from cgitb import text
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        l=Label(text='Hello world')

        return l


MyApp().run()