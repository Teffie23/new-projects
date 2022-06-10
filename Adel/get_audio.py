import pyttsx3
tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice', 'ru')
def speak(what):
    #print(what)
    tts.say(what)
    tts.runAndWait()
    tts.stop()

#for voice in voices:
#    if voice.name == 'Anna':
#        tts.setProperty('voice', voice.id)
tts.setProperty('voice', voices[1].id)
tts.setProperty('rate', 150)
#speak('Это я компьютер')