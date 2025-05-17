import whisper
import speech_recognition as sr

r = sr.Recognizer()
model = whisper.load_model("medium")


def dinleme_cevirme():
    
    with sr.Microphone() as source:
         print("Hazır, konuşabilirsiniz...")
         audio = r.listen(source)
         
    with open("gecici_kayit.wav", "wb") as f:
         f.write(audio.get_wav_data())

# Whisper ile çözümle
    result = model.transcribe("gecici_kayit.wav", language="tr")
    return result["text"]
