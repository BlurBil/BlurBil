from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import openpyxl

class Screen1(GridLayout):

    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)
        self.cols = 1

        self.add_widget(Label(text='File Path'))
        self.path = TextInput(font_size=32)
        self.add_widget(self.path)

        self.add_widget(Label(text='Info'))
        self.info = TextInput(font_size=32,multiline=False)
        self.add_widget(self.info)


        self.add_widget(Label(text='Amount of Money'))
        self.amt = TextInput(password=False, multiline=False)
        self.add_widget(self.amt)

        self.submit = Button(text="Submit")
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
        
    def press(self,instance):
    	path = self.path.text
    	info = self.info.text
    	amt = self.amt.text

    	wb = openpyxl.load_workbook(path)
    	page1 = wb['Sheet1']
    	row = (info , amt)
    	page1.append(row)
    	wb.save(path)





class MyApp(App):

    def build(self):
        return Screen1()


if __name__ == '__main__':
    MyApp().run()
