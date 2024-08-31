from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color

class DrawingWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 0, 0, 1)  # Red color
            Ellipse(pos=(100, 100), size=(100, 100))

class DrawingApp(App):
    def build(self):
        return DrawingWidget()

if __name__ == '__main__':
    DrawingApp().run()
