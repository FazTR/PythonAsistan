# train_model.py

from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments, AutoTokenizer
from datasets import load_from_disk
import json

# 1. Tokenize edilmiş veri kümesini yükle
tokenized_dataset = load_from_disk("tokenized_dataset")

# 2. Label sayısını oku
with open("label_list.json", "r", encoding="utf-8") as f:
    label_list = json.load(f)

# 3. Modeli yükle
model = AutoModelForSequenceClassification.from_pretrained(
    "dbmdz/bert-base-turkish-cased",
    num_labels=len(label_list)
)

# 4. Eğitim ayarları
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=20,
    per_device_train_batch_size=8,
    save_steps=36,
    save_total_limit=2,
    logging_dir="./logs",
)

# 5. Trainer oluştur ve eğit
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

trainer.train()

# 6. Model ve tokenizer kaydet
model.save_pretrained("./results")
tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-turkish-cased")
tokenizer.save_pretrained("./results")
