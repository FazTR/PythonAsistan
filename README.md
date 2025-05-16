## 🧠 Yapay Zeka Destekli Sesli Asistan – Python + IoT

Merhaba, ben **Feyzullah Öztürk**.

Bu projede Python programlama dili kullanılarak, **makine öğrenmesi** ve **IoT** teknolojileriyle entegre çalışabilen, **yerel olarak çalışan bir sesli asistan** geliştiriyoruz. Amacımız, hem yapay zeka temelli hem de ev otomasyonu sistemleriyle uyumlu bir asistan tasarlamak.

---

### 🚀 Özellikler

* ✅ **Ses Tanıma**: OpenAI'nin Whisper modeli ile internet bağlantısı olmadan çalışabilen yüksek doğruluklu ses tanıma.
* ✅ **Yapay Zeka Temelleri**: Öğrenebilir yapıya zemin hazırlayan modüler sistem.
* ✅ **IoT Uyumlu**: Gelecekte akıllı ev cihazları ile entegre edilebilir altyapı.
* ✅ **Python 3.9.9** ile tam uyumlu.

---

### 🛠 Kullanılan Teknolojiler ve Kütüphaneler

| Teknoloji                                                            | Açıklama                                                                    |
| -------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| [Python 3.9.9](https://www.python.org/downloads/release/python-399/) | Projenin temel programlama dili.                                            |
| [OpenAI Whisper](https://github.com/openai/whisper)                  | Yüksek doğruluklu, çevrimdışı ses tanıma modeli.                            |
| [FFmpeg](https://www.gyan.dev/ffmpeg/builds/)                        | Whisper'ın ses dosyalarını işleyebilmesi için gerekli ses dönüştürme aracı. |
| [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)     | Mikrofon verisini yakalamak ve işlemek için kullanılır.                     |
| [PyAudio](https://pypi.org/project/PyAudio/)                         | Mikrofon üzerinden ses almak için kullanılır.                               |

---

### 🛆 Kurulum

1. Python 3.9.9'u kurun.
2. Gerekli kütüphaneleri yükleyin:

```bash
pip install openai-whisper
pip install SpeechRecognition
pip install PyAudio
```

3. [FFmpeg](https://www.gyan.dev/ffmpeg/builds/) aracını indirip sistem PATH'ine ekleyin.

---

### 🎯 Amaç

Bu projenin amacı, Türkçe konuşmaları algılayabilen ve geliştirilebilir bir sesli asistan altyapısı oluşturmaktır. İlerleyen aşamalarda makine öğrenmesi ile karar verebilen ve IoT cihazları kontrol edebilen bir sisteme dönüşmesi hedeflenmektedir.

---

### 🧪 Geliştirme Durumu

* [x] Sesli komut alma
* [x] Türkçe ses tanıma (Whisper ile)
* [ ] Yanıt üretebilme (TTS)
* [ ] Cihaz kontrolü (IoT)
* [ ] Öğrenen yapı / komut optimizasyonu

---
