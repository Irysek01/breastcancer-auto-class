from load_model import model, feature_extractor
import torch 
from PIL import Image
from argparse import ArgumentParser
import sys

argparse = ArgumentParser()
argparse.add_argument(
    "-i",
    "--input_file",
    help="Path to the input file where all the raw reads are stored (must be fasta)",
    required=True,
)

args = argparse.parse_args()


inf = args.input_file

def handle_image(imagepath, model=model, processor=feature_extractor):
    image = Image.open(imagepath)
    inputs = processor(image, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits

    # model predicts one of the 1000 ImageNet classes
    predicted_label = logits.argmax(-1).item()
    if model.config.id2label[predicted_label] == "benign_breast_cancer":
        print(f'{imagepath.split("/")[-1].split(".")[0].replace("P","T")},0.0')
    elif model.config.id2label[predicted_label] == "malignant_breast_cancer":
        print(f'{imagepath.split("/")[-1].split(".")[0].replace("P","T")},1.0')
    else:
        print(f'Skipping {imagepath.split("/")[-1].split(".")[0].replace("P","T")} as the model did not classify it correctly', file=sys.stderr)

if __name__ == "__main__":
    handle_image(inf)