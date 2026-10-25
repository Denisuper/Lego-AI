"""Fine-tune Qwen2.5-VL-7B on the exported examples with LoRA.
Usage:
  pip install -r training/requirements.txt
  python tools/audit_dataset.py
  python training/pack_data.py
  python training/train_qwen.py --model Qwen/Qwen2.5-VL-7B-Instruct --epochs 3
Needs a GPU with 24+ GB VRAM, or run 4-bit quantized on ~10 GB.
The current JSONL contains text messages. Booklet PDFs are source material;
page images are not currently passed to the trainer.
Output: training/out/<model name>/ (LoRA adapter)."""
import argparse
from datasets import load_dataset
from peft import LoraConfig
from trl import SFTConfig, SFTTrainer

ap = argparse.ArgumentParser()
ap.add_argument("--model", default="Qwen/Qwen2.5-VL-7B-Instruct")
ap.add_argument("--epochs", type=float, default=3)
ap.add_argument("--max_length", type=int, default=8192)
ap.add_argument("--lr", type=float, default=2e-4)
Args = ap.parse_args()

files = {"train": "training/data/train.jsonl"}
import os
if os.path.getsize("training/data/test.jsonl") > 0:
    files["test"] = "training/data/test.jsonl"
data = load_dataset("json", data_files=files)

config = SFTConfig(
    output_dir="training/out/" + args.model.split("/")[-1],
    num_train_epochs=args.epochs,
    learning_rate=args.lr,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=8,
    max_length=args.max_length,
    assistant_only_loss=True,      # learn the answers (thinking + moves), not the prompts
    logging_steps=5,
    save_strategy="epoch",
    bf16=True,
)
# target_modules="all-linear" covers the LLM layers; the ViT encoder is left frozen
lora = LoraConfig(r=32, lora_alpha=64, lora_dropout=0.05, target_modules="all-linear", task_type="CAUSAL_LM")
trainer = SFTTrainer(model=args.model, args=config, train_dataset=data["train"],
                     eval_dataset=data.get("test"), peft_config=lora)
trainer.train()
trainer.save_model()
print("saved to", config.output_dir)
