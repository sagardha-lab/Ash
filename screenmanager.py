from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
import speech_recognition as sr
from kivy.uix.label import Label



class CustomScreen(Screen):
    hue = NumericProperty(0)
    pass

class VoiceRecognition():
    def __init__(self):
        pass
    def detect_voice(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('say something')
            audio =r.listen(source)
        try:
            audio = r.recognize_google(audio)
        except TypeError:
            print('I did not get you please say again')
            audio =r.listen(source)
            audio = r.recognize_google(audio)
        return Label(text = audio)

class ScreenManagerApp(App):

    def build(self):
        record_voice = VoiceRecognition()
        root = ScreenManager()
        for x in range(4):
            root.add_widget(CustomScreen(name='Screen %d' % x))
  #          root.add_widget(CustomScreen())
        return root


if __name__ == '__main__':
    b = ScreenManagerApp()
    b.run()
