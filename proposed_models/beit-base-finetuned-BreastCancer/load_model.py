from transformers import BeitImageProcessor, BeitForImageClassification

model = BeitForImageClassification.from_pretrained("as-cle-bert/beit-base-finetuned-BreastCancer")
processor = BeitImageProcessor.from_pretrained("as-cle-bert/beit-base-finetuned-BreastCancer")