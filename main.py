from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

class Take(FloatLayout):
    def __init__(self,**kwargs):
    #Form
        super(Take,self).__init__(**kwargs)
        self.text_kg_label = Label(text="Введите свой вес в кг:", size_hint=(.3, .1), pos_hint={'x': .03, 'y': 0.91})
        self.text_kg_input = TextInput(size_hint=(.3, .05),pos_hint={'x':.03, 'y':.89},font_size= "12sp")
        self.text_cm_label = Label(text = "Введите свой рост в см:", size_hint=(.3, .1),pos_hint={'x':.03, 'y':.82})
        self.text_cm_input = TextInput(size_hint=(.3, .05), pos_hint={'x': .03, 'y': .8},font_size= "12sp")
        self.main_label = Label(text="", size_hint=(.4, .1),pos_hint={'x':0, 'y':.7})
    #Button
        self.math_button = Button(text = "Рассчитать", size_hint=(.3, .1),pos_hint={'x':.03, 'y':.2},on_press = self.update)
    #Add_Widgets
        self.add_widget(self.text_kg_label)
        self.add_widget(self.text_kg_input)
        self.add_widget(self.text_cm_label)
        self.add_widget(self.text_cm_input)
        self.add_widget(self.main_label)
        self.add_widget(self.math_button)
    def update(self,button):
        try:
            kg = self.text_kg_input.text
            cm = self.text_cm_input.text
            self.IMT = (float(kg) / ((float(cm) / 100) ** 2))
            if self.IMT <= 16:
                self.main_label.text =(f"Ваш ИМТ составил: {str(round(self.IMT,2))}\n"
                                     "Выраженный дефицит массы тела")
            elif self.IMT <= 18.5:
                self.main_label.text =(f"Ваш ИМТ составил: {str(round(self.IMT, 2))}\n"
                                     "Недостаточная масса тела")
            elif self.IMT <= 24:
                self.main_label.text =(f"Ваш ИМТ составил: {str(round(self.IMT, 2))}\n"
                                     "Все в норме")
            elif self.IMT >= 24:
                self.main_label.text =(f"Ваш ИМТ составил: {str(round(self.IMT, 2))}\n"
                                     "Избыточная масса тела")
        except:
            self.main_label.text = ("Неверно введены параметры!")

class MainApp(App):
    def build(self):
        return Take()
if __name__=="__main__":
     MainApp().run()