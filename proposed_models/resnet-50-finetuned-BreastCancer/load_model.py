from transformers import AutoImageProcessor, ResNetForImageClassification

processor = AutoImageProcessor.from_pretrained("as-cle-bert/resnet-50-finetuned-BreastCancer")
model = ResNetForImageClassification.from_pretrained("as-cle-bert/resnet-50-finetuned-BreastCancer")
