# This is a sample Python script.
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.2.1')


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Game(App):
    def build(self):
        return BoxLayout()
game = Game()
game.run()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
