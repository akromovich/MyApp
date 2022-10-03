from turtle import update
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.config import Config

Config.set('graphics','resizable',0)
Config.set('graphics','width',400)
Config.set('graphics','height',500)

class MyApp(App):
    def update_number(self):
        self.lbl.text= self.form
        
    def add_number(self,instance):
        self.form= ''
        print(self.form)
        self.form += instance.text
        print(self.form)

        self.update_number()
    def build(self):
        self.form='0'
        bl = BoxLayout(orientation='vertical',padding=10)
        gl = GridLayout(cols=4,rows=4,spacing=1,size_hint=[1,.6])   
        self.lbl= Label(text='0',size_hint=[1,.6],font_size=40,text_size=(400-30,500*.4-10),halign='right',valign='bottom')
        
        gl.add_widget(Button(text='7',on_press=self.add_number))
        gl.add_widget(Button(text='8',on_press=self.add_number))
        gl.add_widget(Button(text='9',on_press=self.add_number))
        gl.add_widget(Button(text='/',on_press=self.add_number))

        gl.add_widget(Button(text='4',on_press=self.add_number))
        gl.add_widget(Button(text='5',on_press=self.add_number))
        gl.add_widget(Button(text='6',on_press=self.add_number))
        gl.add_widget(Button(text='*',on_press=self.add_number))

        gl.add_widget(Button(text='1',on_press=self.add_number))
        gl.add_widget(Button(text='2',on_press=self.add_number))
        gl.add_widget(Button(text='3',on_press=self.add_number))
        gl.add_widget(Button(text='-',on_press=self.add_number))

        gl.add_widget(Button(text='='))
        gl.add_widget(Button(text='0',on_press=self.add_number))
        gl.add_widget(Button(text='.',on_press=self.add_number))
        gl.add_widget(Button(text='+',on_press=self.add_number))
        
        bl.add_widget(self.lbl)
        bl.add_widget(gl)
        
        return bl


MyApp().run()