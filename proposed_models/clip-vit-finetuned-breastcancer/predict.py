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

def handle_image(imagepath, model=model, processor=processor):
    image = Image.open(imagepath)
    inputs = processor(text=["bening_breast_cancer", "malignant_breast_cancer"], images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image # this is the image-text similarity score
    probs = logits_per_image.softmax(dim=1) # we can take the softmax to get the label probabilities
    if probs[0][0].item() > probs[0][1].item():
        print(f'{imagepath.split("/")[-1].split(".")[0].replace("P","T")},0.0')
    if probs[0][0].item() < probs[0][1].item():
        print(f'{imagepath.split("/")[-1].split(".")[0].replace("P","T")},1.0')

if __name__ == "__main__":
    handle_image(inf)