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


new_model = load_model('foundation_model/breastcanc_classifier.h5')

import sys
def handle_img(infile):
    # Get the photo file ID
    img = cv2.imread(infile)
    resize = tf.image.resize(img, (256,256))
    yhat = new_model.predict(np.expand_dims(resize/255, 0))
    if 0.5 < yhat: 
        print(f'Score is {yhat[0][0]}', file=sys.stderr)
        print(f'Predicted class is Malignant', file=sys.stderr)
    else: 
        print(f'Score is {yhat[0][0]}', file=sys.stderr)
        print(f'Predicted class is Benign', file=sys.stderr)

if __name__ == "__main__":
    handle_img(inf)

