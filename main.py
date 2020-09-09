from webScraper import WebScr
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class TutorialApp(App):
    def build(self):
        cashbuy = 0.000000
        target_rate = 29.75
        value = ""
        a = WebScr("https://rate.bot.com.tw/xrt?Lang=en-US")
        df = a.get_data_frame()
        df_usd = df.query('DOLLAR.str.contains("USD")')
        cashbuy = float(df_usd.iloc[0]['CASH_BUY'])
        if cashbuy >= target_rate:
            value = str(cashbuy)

        mylayout = BoxLayout(orientation="vertical")
        mylabel = Label(text=value)
        mybutton = Button(text="Click me!")
        mylayout.add_widget(mylabel)
        mybutton.bind(on_press=lambda a: print(mylabel.text))
        mylayout.add_widget(mybutton)
        return mylayout


TutorialApp().run()
