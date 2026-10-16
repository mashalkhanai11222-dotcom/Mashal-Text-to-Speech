from gtts import gTTS

text="hey i am mashal khan form pakistan kpk python deveplor and future ai engineer thank you!"

tss=gTTS(text=text,lang="en")

tss.save("voice.mp3")

print("Audio saved successfully..thank you ")