import recognizer
import predict_intent
import time


def aksiyon_uygula(intent):
    if intent == "hava_durumu":
        print("Bugün hava güneşli görünüyor.")
    elif intent == "isik_ac":
        print("Işıkları açıyorum.")
    elif intent == "isik_kapat":
        print("Işıkları kapatıyorum.")
    elif intent == "muzik_cal":
        print("Müziği başlatıyorum.")
    elif intent == "alarm_kur":
        print("Alarm kuruldu.")
    elif intent == "alarm_iptal":
        print("Alarm iptal edildi.")
    else:
        print("Bu komutu anlayamadım.")

if __name__ == "__main__":
    try:
        print("🟢 Asistan başlatıldı. 'çık' dediğinizde kapanacaktır.")
        while True:
            try:
                metin = recognizer.dinleme_cevirme()
                if not metin.strip():
                    continue  # Boşsa atla

                print("📝 Algılanan metin:", metin)

                if "çık" in metin.lower():
                    print("Görüşmek üzere!")
                    break

                niyet = predict_intent.predict_intent(metin)
                print(f"🎯 Tahmin Edilen Niyet: {niyet}")
                aksiyon_uygula(niyet)

            except Exception as e:
                print(f"⚠️ Hata oluştu: {str(e)}")
                time.sleep(1)

    except KeyboardInterrupt:
        print("\n🛑 Dinleme manuel olarak durduruldu.")
