from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("as-cle-bert/clip-vit-finetuned-breastcancer")
processor = CLIPProcessor.from_pretrained("as-cle-bert/clip-vit-finetuned-breastcancer")