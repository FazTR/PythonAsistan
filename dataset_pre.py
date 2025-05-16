from datasets import Dataset
from intent_dataset import intent_dataset
from transformers import AutoTokenizer

dataset = Dataset.from_list(intent_dataset)

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

tokenized_dataset = dataset.map(tokenize_function, batched=True)

label_list = list(set([item["intent"] for item in intent_dataset]))
label_to_id = {label: i for i, label in enumerate(label_list)}

def label_to_int(example):
    example["label"] = label_to_id[example["intent"]]
    return example

tokenized_dataset = tokenized_dataset.map(label_to_int)
tokenized_dataset = tokenized_dataset.remove_columns(["text", "intent"])
