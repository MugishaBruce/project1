from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
Builder.load_file('./main.kv')
Window.size = (280, 520)



class CalculatorWidget(Widget):
    def clear(self):
        self.ids.input.text = "0"

    def button_value(self, number):
            prev_value = self.ids.input.text

            if prev_value == '0':
                self.ids.input.text = ""
                self.ids.input.text = f"{number}"
            else:
                self.ids.input.text = f"{prev_value}{number}"

    def deleteone(self):
            prev_value = self.ids.input.text
            prev_value = prev_value[: -1]
            self.ids.input.text = prev_value

##
    def signes(self, signe):
            prev_value = self.ids.input.text
            self.ids.input.text = f"{prev_value}{signe}"

    def results(self):
            prev_value = self.ids.input.text
            result = eval(prev_value)
            self.ids.input.text = str(result)


class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()

if __name__ == "__main__":
    CalculatorApp().run()

