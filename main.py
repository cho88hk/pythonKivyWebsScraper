from webScraper import WebScr
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class TutorialApp(App):
    def build(self):

        a = WebScr("https://rate.bot.com.tw/xrt?Lang=zh-TW")
        value = a.getvalue()
        if not value:
            value = "NO VALUE"
        mylayout = BoxLayout(orientation="vertical")
        mylabel = Label(text=value)
        mybutton = Button(text="Click me!")
        mylayout.add_widget(mylabel)
        mybutton.bind(on_press=lambda a: print(mylabel.text))
        mylayout.add_widget(mybutton)
        return mylayout


TutorialApp().run()
