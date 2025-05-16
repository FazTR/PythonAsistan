from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments
from dataset_pre import tokenized_dataset
import torch

model = AutoModelForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    num_labels=len(set(tokenized_dataset["label"]))
)

training_args = TrainingArguments(
    output_dir="./results",
  #  evaluation_strategy="epoch",  # <-- HATA BURADA OLUYORSA: yukarıdaki çözümleri dene
    num_train_epochs=3,
    per_device_train_batch_size=8,
    save_steps=36,
    save_total_limit=2,
    logging_dir="./logs",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

trainer.train()
model.save_pretrained("./results")

# <-- Tokenizer'ı da kaydet
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
tokenizer.save_pretrained("./results")

