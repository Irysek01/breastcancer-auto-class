import tensorflow as tf 
from tensorflow.keras.models import load_model
import cv2
import numpy as np
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


new_model = load_model('models/breastcanc_classifier.h5')


def handle_img(infile):
    # Get the photo file ID
    img = cv2.imread(infile)
    resize = tf.image.resize(img, (256,256))
    yhat = new_model.predict(np.expand_dims(resize/255, 0))
    if 0.5 > yhat: 
        print(f'Score is {yhat}')
        print(f'Predicted class is Malignant')
    else: 
        print(f'Score is {yhat}')
        print(f'Predicted class is Benign')

if __name__ == "__main__":
    handle_img(inf)

