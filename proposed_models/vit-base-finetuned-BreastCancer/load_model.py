from transformers import ViTImageProcessor, ViTForImageClassification

model = ViTForImageClassification.from_pretrained("as-cle-bert/vit-base-finetuned-BreastCancer")
processor = ViTImageProcessor.from_pretrained("as-cle-bert/vit-base-finetuned-BreastCancer")