from transformers import AutoImageProcessor, AutoModelForImageClassification

processor = AutoImageProcessor.from_pretrained("as-cle-bert/bus-swin")
model = AutoModelForImageClassification.from_pretrained("as-cle-bert/bus-swin")