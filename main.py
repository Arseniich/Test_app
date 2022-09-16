

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar


class TestApp(App):


    def build(self):

        main_loyout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.inputuser = TextInput(multiline=False, readonly=False, halign="right", font_size=55, input_filter="float")
        main_loyout.add_widget(self.inputuser)
        # pb = ProgressBar(max=1000)
        # main_loyout.add_widget(pb)

        buttons = [
            ["C", "()", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["+/-", "0", ",", "="]
        ]
        for btn in buttons:
            button_layout = GridLayout(cols=4)
            for items in btn:
                if items == "=":

                    button_layout.add_widget(Button(text=items, size_hint_x=None, width=100, on_press=self.sum))
                else:
                    button_layout.add_widget(Button(text=items, size_hint_x=None, width=100, on_press=self.press_button))

            main_loyout.add_widget(button_layout)

        return main_loyout

    def press_button(self, instance):
        if instance.text == "C":
            self.inputuser.text = ""

        else:
            self.inputuser.text += instance.text

    def sum(self, instance):
        if self.inputuser.text:

            try:
                print(self.inputuser.text)
                self.inputuser.text = str(eval(self.inputuser.text))
                print(self.inputuser.text)
            except:
                self.inputuser.text = "Error"


if __name__ == '__main__':
    TestApp().run()
    print(12)
