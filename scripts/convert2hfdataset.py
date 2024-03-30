from datasets import load_dataset

dataset = load_dataset("imagefolder", data_dir="hf_dataset", split="train")

dataset.push_to_hub("as-cle-bert/breastcanc-ultrasound-class", private=True)