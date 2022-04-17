from kivy.uix.label import Label
from kivy.app import App
import datetime
from kivy.clock import Clock
from kivy.metrics import *
class main(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.change, 1)
        self.font_size = dp(100)
    def change(self,b):
        now = datetime.datetime.now()
        self.text = str(now.hour)+":"+str(now.minute)+":"+str(now.second)
class app(App):
    def build(self):
        return main()
if __name__ == "__main__":
    app = app()
    app.run()
