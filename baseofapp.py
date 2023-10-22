# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 09:25:40 2023

@author: amnhw
"""

import kivy
kivy.require('2.2.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import *

'''
class takepill(Widget):
    pressed = ListProperty([0,0])
    
    def touchdown(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            return True
        return super(touchdown, self).touchdown(touch)
    def pressed(self, instance, pos):
        print('pressed at {pos}'.format(pos=pos))
'''
        
class RootWid(FloatLayout):
    
    def __init__(self):
        super(RootWid,self).__init__()
        
        self.add_widget(
            Button(
                background_color = (0.47, 0.03, 0.03),
                text="Take Pill",
                size_hint=(.5,.5),
                pos_hint={'center_x': .5, 'center_y': .5})
            )
class close(FloatLayout):
    def __init__(self):
        super(close, self).__init__()
        
        self.add_widget(
            Button(
                background_color = (1,0,0),
                text="Take Pill",
                size_hint=(.1,.1),
                pos_hint={'center_x': .5, 'center_y': .5})
                )
            
        
class Login(GridLayout):
    def __init__(self):
        super(Login, self).__init__()
        self.cols = 2
        
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        
        self.add_widget(Label(text="Password"))
        self.password = TextInput(multiline=False)
        self.add_widget(self.password)
        
class pillapp(App):
    def build(self):
        self.root = root = RootWid()
        root.bind(size=self._update_rect, pos=self._update_rect)
        
        with root.canvas.before:
            Color(0.99, 0.96, 0.96)
            self.rect = Rectangle(size = root.size, pos=root.pos)
        return root
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    
if __name__ == '__main__':
    pillapp().run()