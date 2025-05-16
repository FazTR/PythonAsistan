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
pip install transformers
pip install datasets
pip install torch
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

## 📊 Modeli Eğitme

```bash
python train_intent_classifier.py
```

Bu adım sonunda `results/` klasöründe aşağıdaki dosyalar oluşur:

* `pytorch_model.bin`: eğitilen ağırlıklar
* `config.json`: model konfigürasyonu
* `tokenizer_config.json`, `vocab.txt`: tokenizer bilgileri

### ❗ Önemli:

Eğer `save_steps` çok düşükse, çok sayıda `checkpoint-*` klasörü oluşur. `save_total_limit` ile sınırlandırılabilir.

```python
training_args = TrainingArguments(
    save_steps=100,  # 100 adımda bir kayıt
    save_total_limit=2  # En fazla 2 kayıt sakla
)
```

---

## 🔎 Model ile Tahmin

```bash
python predict_intent.py
```

```python
# predict_intent.py örneği
text = "Müzik açar mısın?"
print(predict_intent(text))
# Çıktı: muzik_cal
```

---

## 🗃 Veri Kümesi

`intent_dataset.py` içinde örnek veri kümesi:

```python
intent_dataset = [
    {"text": "Hava durumu nasıl?", "intent": "hava_durumu"},
    {"text": "Işığı açar mısın?", "intent": "isik_ac"},
    {"text": "Şarkı başlat.", "intent": "muzik_cal"},
    {"text": "Alarmı kur.", "intent": "alarm_kur"},
    ...
]
```

> Veri seti küçükse model başarımı düşük olabilir. Geniş ve dengeli veri seti kullanılması önerilir.

---

## 🧠 Eğitimin Sonuçları

```bash
{'train_runtime': 208.1, 'train_loss': 1.68, 'epoch': 3.0}
```

* `train_loss`: Eğitim kaybı, ne kadar düşükse model o kadar iyi öğrenmiş demektir.
* `train_runtime`: Toplam eğitim süresi.
