# dataset_pre.py

from datasets import Dataset
from intent_dataset import intent_dataset
from transformers import AutoTokenizer
import json

# 1. Veri kümesini Dataset formatına çevir
dataset = Dataset.from_list(intent_dataset)

# 2. Tokenizer yükle
tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-turkish-cased")

# 3. Tokenize et
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=64)

tokenized_dataset = dataset.map(tokenize_function, batched=True)

# 4. Label'ları numaralandır
label_list = sorted(list(set([item["intent"] for item in intent_dataset])))  # Sıralı ve sabit!
label_to_id = {label: i for i, label in enumerate(label_list)}

# 5. Etiketleri integer'a dönüştür
def label_to_int(example):
    example["label"] = label_to_id[example["intent"]]
    return example

tokenized_dataset = tokenized_dataset.map(label_to_int)
tokenized_dataset = tokenized_dataset.remove_columns(["text", "intent"])

# 6. Label listesi JSON olarak kaydet
with open("label_list.json", "w", encoding="utf-8") as f:
    json.dump(label_list, f, ensure_ascii=False)

# 7. Export için
tokenized_dataset.save_to_disk("tokenized_dataset")
