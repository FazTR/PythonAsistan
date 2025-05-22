import whisper
import speech_recognition as sr

# Whisper modeli yükleniyor
model = whisper.load_model("medium")
r = sr.Recognizer()

def dinleme_cevirme():
    with sr.Microphone() as source:
        print("🎤 Dinleniyor... Konuşabilirsiniz:")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # WAV dosyasına geçici olarak kaydet
    with open("gecici_kayit.wav", "wb") as f:
        f.write(audio.get_wav_data())

    # Whisper ile yazıya dök
    result = model.transcribe("gecici_kayit.wav", language="tr")
    return result["text"]
