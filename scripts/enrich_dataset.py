import pandas as pd
import shutil
csv = pd.read_csv("BrEaST-Lesions-USG-clinical-data-Dec-15-2023.csv")
filenames = list(csv["Image_filename"])
classifications = list(csv["Classification"])

for i in range(len(filenames)):
    if classifications[i] == "benign":
        shutil.copy(src=f"BrEaST-Lesions_USG-images_and_masks/{filenames[i]}", dst="training2/benign")
    elif classifications[i] == "malignant":
        shutil.copy(src=f"BrEaST-Lesions_USG-images_and_masks/{filenames[i]}", dst="training2/malignant")
    else:
        continue
