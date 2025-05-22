from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
import json

# Etiket listesini yükle
with open("label_list.json", "r", encoding="utf-8") as f:
    label_list = json.load(f)

# Model ve tokenizer
tokenizer = AutoTokenizer.from_pretrained("./results")
model = AutoModelForSequenceClassification.from_pretrained("./results")

def predict_intent(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding='max_length', max_length=64)
    outputs = model(**inputs)
    logits = outputs.logits
    probs = F.softmax(logits, dim=1)
    predicted_class_id = torch.argmax(probs).item()
    return label_list[predicted_class_id]
