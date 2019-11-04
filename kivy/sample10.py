from random import random
from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Line
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color
from kivy.uix.label import Label


Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '2000')

class MyPaintWidget(Widget):
    global coor_x, coor_y;
    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            touch.ud['line'] = Line(points=(touch.x, touch.y))
            print(touch.x, " ", touch.y)


    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
        print(touch.x, " ", touch.y)
class SubScreen(GridLayout):
    def __init__(self):
        GridLayout.__init__(self, cols=2, rows=3);
        self.add_widget(Label(text='1st'))
        self.add_widget(Label(text='2nd'))
        self.add_widget(Label(text='3rd'))
        self.add_widget(Label(text='4th'))
        self.add_widget(Label(text='5th'))
        self.add_widget(Label(text='6th'))
class MainScreen(GridLayout):
    def __init__(self,**kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.rows = 2
        self.painter = MyPaintWidget()
        self.add_widget(self.painter)

        # btnlayout = FloatLayout(size=(300, 300))
        # clearbtn = Button(text='Clear')
        # clearbtn.bind(on_release=self.clear_canvas)
        # btnlayout.add_widget(clearbtn)
        self.add_widget(SubScreen())

    def clear_canvas(self, obj):
        self.painter.canvas.clear()

class MyPaintApp(App):
    def build(self):
        # parent = Widget()
        # self.painter = MyPaintWidget()
        # clearbtn = Button(text='Clear')
        # clearbtn.bind(on_release=self.clear_canvas)
        # parent.add_widget(self.painter)
        # parent.add_widget(clearbtn)
        return MainScreen()




if __name__ == '__main__':
    MyPaintApp().run()
