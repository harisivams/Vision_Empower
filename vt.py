from gtts import gTTS
from playsound import playsound
mytext = 'Welcome to geeksforgeeks!'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.wav")
playsound('H:\emotion and face identification\emotion and face identification\welcome.mp3')
#verified