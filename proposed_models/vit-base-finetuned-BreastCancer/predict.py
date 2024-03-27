from PIL import Image
from transformers import CLIPProcessor, CLIPModel
from load_model import model, processor
from argparse import ArgumentParser

argparse = ArgumentParser()
argparse.add_argument(
    "-i",
    "--input_file",
    help="Path to the input file where all the raw reads are stored (must be fasta)",
    required=True,
)

args = argparse.parse_args()


inf = args.input_file

import sys

def handle_image(imagepath, model=model, processor=processor):
    image = Image.open(imagepath)
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    # model predicts one of the 1000 ImageNet classes
    predicted_class_idx = logits.argmax(-1).item()
    if model.config.id2label[predicted_class_idx] == "benign_breast_cancer":
        print(f'{imagepath.split("/")[-1].split(".")[0].replace("P","T")},0.0')
    elif model.config.id2label[predicted_class_idx] == "malignant_breast_cancer":
        print(f'{imagepath.split("/")[-1].split(".")[0].replace("P","T")},1.0')
    else:
        print(f'Skipping {imagepath.split("/")[-1].split(".")[0].replace("P","T")} as the model did not classify it correctly', file=sys.stderr)



if __name__ == "__main__":
    handle_image(inf)