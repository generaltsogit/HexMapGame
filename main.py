import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.2.1')


class TestButton(BoxLayout):
    state = 0

    def __init__(self, **kwargs):
        super(TestButton, self).__init__(**kwargs)

    def pressed(self):
        if self.state == 0:
            self.button_label.text = "You pressed it!"
            self.state = 1
        else:
            self.button_label.text = "Press me!"
            self.state = 0


class Game(App):
    def build(self):
        return TestButton()  # Create an instance of TestButton


if __name__ == '__main__':
    Game().run()
