from kivy.app import App
from kivy.uix.label import Label

class KivyTest(App):
    def build(self):
        return Label(text="hello ", font_size='30')


if __name__ == '__main__':
    KivyTest().build()
    KivyTest().run()

