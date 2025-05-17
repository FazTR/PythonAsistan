# predict.py

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
import json

# 1. Label listesini yükle
with open("label_list.json", "r", encoding="utf-8") as f:
    label_list = json.load(f)

# 2. Model ve tokenizer'ı yükle
tokenizer = AutoTokenizer.from_pretrained("./results")
model = AutoModelForSequenceClassification.from_pretrained("./results")

# 3. Tahmin fonksiyonu
def predict_intent(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding='max_length', max_length=64)
    outputs = model(**inputs)
    logits = outputs.logits
    probs = F.softmax(logits, dim=1)
    predicted_class_id = torch.argmax(probs).item()
    return label_list[predicted_class_id]

# 4. Test
if __name__ == "__main__":
    test_text = "müzik ve hava durumu nedir"
    prediction = predict_intent(test_text)
    print(f"'{test_text}' -> Tahmin Edilen Niyet: {prediction}")
