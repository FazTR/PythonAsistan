# 🧠 AI-Powered Voice Assistant – Python + IoT

Hi, I'm **Feyzullah Öztürk**.

In this project, we're developing a **locally running voice assistant** using Python, enhanced with **machine learning** and **IoT** capabilities. Our goal is to build an assistant that understands natural speech and can integrate with smart home devices.

---

## 🚀 Features

- ✅ **Speech Recognition**: High-accuracy, offline speech recognition with OpenAI Whisper.
- ✅ **AI Foundations**: Modular design supporting future learning capabilities.
- ✅ **IoT Compatibility**: Built for future integration with smart devices.
- ✅ Fully compatible with **Python 3.9.9**.

---

## 🛠 Technologies and Libraries

| Technology                                                           | Description                                                                 |
|----------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [Python 3.9.9](https://www.python.org/downloads/release/python-399/) | Main programming language                                                   |
| [OpenAI Whisper](https://github.com/openai/whisper)                  | Offline, high-accuracy speech recognition                                  |
| [FFmpeg](https://www.gyan.dev/ffmpeg/builds/)                        | Audio conversion tool required by Whisper                                  |
| [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)     | Captures and processes microphone input                                    |
| [PyAudio](https://pypi.org/project/PyAudio/)                         | Accesses microphone audio                                                  |
| [Transformers](https://huggingface.co/docs/transformers/index)      | Used for intent classification modeling                                    |

---

## 🛆 Installation

1. Install Python 3.9.9
2. Install required libraries:

```bash
pip install openai-whisper
pip install SpeechRecognition
pip install PyAudio
pip install transformers
pip install datasets
pip install torch
```
## 🎯 Project Goal
The aim is to create a Turkish-speaking voice assistant that runs offline, can be extended with machine learning, and controls IoT devices.

🧪 Development Status
 Voice command capture

 Turkish speech recognition (Whisper)

 Text-to-Speech (TTS) response generation

 IoT device control

 Learning-based command optimization

## 📊 Training the Model
Run the training script:

python train_intent_classifier.py
This will generate files in the results/ directory:

pytorch_model.bin: Trained model weights

config.json: Model configuration

tokenizer_config.json and vocab.txt: Tokenizer data

## ⚠️ Tip
To limit checkpoints saved, set parameters like:

training_args = TrainingArguments(
    save_steps=100,
    save_total_limit=2
)
## 🔎 Predicting Intents
Run the prediction script:

python predict_intent.py
Example usage:

text = "Müzik açar mısın?"
print(predict_intent(text))
# Output: muzik_cal

## 🗃 Dataset Format
Example intent dataset (intent_dataset.py):

python
intent_dataset = [
    {"text": "Hava durumu nasıl?", "intent": "hava_durumu"},
    {"text": "Işığı açar mısın?", "intent": "isik_ac"},
    {"text": "Şarkı başlat.", "intent": "muzik_cal"},
    {"text": "Alarmı kur.", "intent": "alarm_kur"},
]
For better results, use a larger and balanced dataset.

## 📈 Training Results Example
{'train_runtime': 208.1, 'train_loss': 1.68, 'epoch': 3.0}
train_loss: Lower means better learning.

train_runtime: Total training duration.

## 📬 Contact
If you have questions or suggestions, please reach out!
Feyzullah Öztürk — LinkedIn • GitHub

## 🧠 Future Plans
Add Text-to-Speech (TTS) using Coqui or gTTS.

Implement IoT device control via MQTT or HTTP.

Build a learning system for command optimization.

Develop a GUI or mobile app for easier interaction.

