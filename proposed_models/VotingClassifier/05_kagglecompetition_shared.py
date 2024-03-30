# -*- coding: utf-8 -*-
"""05-kagglecompetition_shared.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1np4I9iKl5qcHdZi7Xl_GvpFgwDGPBCWO
"""

import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
import pandas as pd # for reading and writing tables

import ntpath

from matplotlib import pyplot
from numpy import where
from collections import Counter

data_folder = "../../complete_set/training_set/"
benign_folder = data_folder + "benign/"
malignant_folder = data_folder + "malignant/"

#define function to get image number
def num (image) :
    val = 0

    for i in range(len(image)) :
        if image[i] == '(' :
            while True :
                i += 1
                if image[i] == ')' :
                    break
                val = (val*10) + int(image[i])
            break

    return val

def getCountOfImage():
    max_ben = 0
    max_mal = 0
    classes = ['benign', 'malignant']
    label = 0
    labels = []
    benign = 0
    malignant = 0
    for cname in os.listdir(data_folder):
       # print(cname)
       for filename in sorted (os.listdir(os.path.join(data_folder,cname))):
           if not '_mask' in filename :
               if 'benign' in filename :
                 if num(filename) > max_ben:
                   max_ben = num(filename)
                 benign +=1
               elif 'malignant' in filename:
                 print(str(max_mal) + ' + ' + str(num(filename)))
                 if num(filename) > max_mal:
                   max_mal = num(filename)
                 malignant +=1

    return int(benign), int(malignant), max_ben, max_mal

#get count of images
benign, malignant, n_ben, n_mal = getCountOfImage()

print(benign)
print(malignant)
print(str(n_ben))
print(str(n_mal))

size_x ,size_y = 128,128
#create empty array of zeros to store image inside it
study_benign     = np.zeros((benign,size_x,size_y))
mask_benign      = np.zeros((benign,size_x,size_y))
study_malignant  = np.zeros((malignant,size_x,size_y))
mask_malignant   = np.zeros((malignant,size_x,size_y))

labels_benign    = np.zeros(benign)
labels_malignant = np.zeros(malignant)

correspondence_index_ben = np.zeros((n_ben,1))
correspondence_index_mal = np.zeros((n_mal,1))

#start load image
                #0        #1
classes = ['benign', 'malignant']
label = 0
labels = [] #for classification part
images = [] #for classification part
i_ben = 0
i_mal = 0
for cname in  os.listdir(data_folder):
    for filename in sorted (os.listdir(os.path.join(data_folder,cname))):
        imagePath = data_folder + cname + '/' + filename
        image = cv2.imread(imagePath,cv2.IMREAD_GRAYSCALE)
        if not '_mask' in filename :
            image = cv2.resize(image,(size_x,size_y))
            image = np.array(image)
            images.append(image)
            #image = np.expand_dims(image,axis=-1)
            #load x_benign images
            #print(str(num(filename)-1))
            if 'benign' in filename:
                correspondence_index_ben[num(filename)-1] = i_ben
                study_benign[i_ben]+= np.array(image)
                labels_benign[i_ben] = int(0)
                i_ben +=1
            if 'malignant' in filename:
                #print(str(i_mal))
                #print(str(num(filename)))
                #print('###')
                correspondence_index_mal[num(filename)-1] = i_mal
                study_malignant[i_mal]+= np.array(image)
                labels_malignant[i_mal] = int(1)
                i_mal +=1

    for filename in sorted (os.listdir(os.path.join(data_folder,cname))):
        imagePath = data_folder + cname + '/' + filename
        image = cv2.imread(imagePath,cv2.IMREAD_GRAYSCALE)
        if '_mask' in filename :
            image = cv2.resize(image,(size_x,size_y))
            image = np.array(image)
            #image = np.expand_dims(image,axis=-1)
            if filename[0] == 'b':
                ind_ = int(correspondence_index_ben[num(filename)-1])
                mask_benign[ind_]+= np.array(image)
            if filename[0] == 'm' :
                ind_ = int(correspondence_index_mal[num(filename)-1])
                mask_malignant[ind_]+= np.array(image)

mask_benign[mask_benign > 0] = 1
mask_malignant[mask_malignant > 0] = 1

print(np.shape(study_benign))
print(np.shape(mask_benign))

print(np.shape(study_malignant))
print(np.shape(mask_malignant))

"""#Let's show some Benign cases"""

plt.figure(figsize = (20,12))

for i in range(3) :
    plt.subplot(2,3,i+1)
    plt.imshow(np.squeeze(study_benign[i+1]), 'gray')
    plt.title('Benign')
    plt.axis('off')

for i in range(3) :
    plt.subplot(2,3,i+4)
    plt.imshow(np.squeeze(mask_benign[i+1]), 'gray')
    plt.title('Mask')
    plt.axis('off')
plt.show()

"""#And now some Malignant cases"""

plt.figure(figsize = (20,12))

for i in range(3) :
    plt.subplot(2,3,i+1)
    plt.imshow(np.squeeze(study_malignant[i+1]), 'gray')
    plt.title('Malignant')
    plt.axis('off')

for i in range(3) :
    plt.subplot(2,3,i+4)
    plt.imshow(np.squeeze(mask_malignant[i+1]), 'gray')
    plt.title('Mask')
    plt.axis('off')
plt.show()

"""#Collect all studies together"""

studies = (np.concatenate((study_benign, study_malignant), axis = 0))
masks = (np.concatenate((mask_benign, mask_malignant), axis = 0))
labels = (np.concatenate((labels_benign, labels_malignant), axis = 0))
print(studies.shape)
print(masks.shape)
print(labels.shape)

"""#and plot"""

plt.figure(figsize = (20,12))

for i in range(3) :
    plt.subplot(2,3,i+1)
    plt.imshow(np.squeeze(studies[i+1]), 'gray')
    plt.title('Label = ' + str(labels[i+1]))
    plt.axis('off')

for i in range(3) :
    plt.subplot(2,3,i+4)
    plt.imshow(np.squeeze(masks[i+1]), 'gray')
    plt.title('Masks')
    plt.axis('off')
plt.show()

"""#Let's extract readiomic feature through pyradiomics"""


from radiomics import featureextractor

# special functions for using pyradiomics
from SimpleITK import GetImageFromArray
import radiomics
from radiomics.featureextractor import RadiomicsFeatureExtractor # This module is used for interaction with pyradiomic
import logging
logging.getLogger('radiomics').setLevel(logging.CRITICAL + 1)  # this tool makes a whole TON of log noise

# Commented out IPython magic to ensure Python compatibility.
# Plot Setup Code
# Setup the defaults to make the plots look a bit nicer for the notebook

# %matplotlib inline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
plt.rcParams["figure.figsize"] = (8, 8)
plt.rcParams["figure.dpi"] = 125
plt.rcParams["font.size"] = 14
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.style.use('ggplot')
sns.set_style("whitegrid", {'axes.grid': False})

# Define extractor
extractor = featureextractor.RadiomicsFeatureExtractor(binCount = 128, force2D = True)
extractor.enableFeatureClassByName('shape2D')
extractor.settings

results = extractor.execute(GetImageFromArray(studies[0]),
                            GetImageFromArray((masks[0]).astype(np.uint8)),
                            label = 1)

pd.DataFrame([results]).T

# Extract features from Benign and Malignant studies
for i in range(len(studies)):
  #print(mask[i].min())
  #print(mask[i].max())
  #print(cv2.countNonZero(mask[i]))
  #print(np.sum(mask[i] == 0))

  #print( str(i) + ' of ' + str(len(studies)) )
  features_currentStudy = extractor.execute(GetImageFromArray(studies[i]),
                    GetImageFromArray((masks[i]).astype(np.uint8)),
                    label = 1)

  # Stack DataFrames
  if i == 0:
    extracted_features = pd.DataFrame([features_currentStudy])
  else:
    extracted_features = pd.concat( [extracted_features, pd.DataFrame([features_currentStudy])], ignore_index=True )

"""##What do we have now?"""

print(extracted_features.shape)
print(np.array(labels).shape)

extracted_features.head()

# Let's focus on informative features
value_feature_names = [c_col for c_col in extracted_features.columns if (c_col.startswith('original') and '_shape_' not in c_col)]
print(np.random.choice(value_feature_names, 3), 'of', len(value_feature_names))

dataset = extracted_features[value_feature_names]

dataset.head()

"""#We now have dataset and labels"""

print(dataset.shape)
print(value_feature_names)
print(np.array(labels).shape)

print(np.unique(labels))

"""Remember: here, 0 = benign, 1 = malignant

#Split training-testing subsets
"""

# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split
# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(dataset, labels, test_size = 0.05)

"""|

|

|

#Feature selection (optional)
"""

def compute_fdr(input_data, input_labels, k=5):
  fdr = []
  sorted_fdr = []
  selected_features = input_data
  selection_index = []
#  ...
#  ...
#  ...

  return fdr, sorted_fdr, selected_features, selection_index

pd_train_features = train_features
np_train_features = train_features.to_numpy()
np_train_labels = np.array(train_labels)

print(np_train_features)

features_to_select = 50
fdr_, sorted_fdr_, selected_train_features, selection_train_index = compute_fdr(np_train_features, np_train_labels, features_to_select)
# print(fdr_)

print(selected_train_features[1,:])

"""|

|

|

Remember to replicate feature selection on (internal) testing set!
"""

np_test_features = test_features.to_numpy()
fdr_, sorted_fdr_, selected_test_features, selected_test_index = compute_fdr(np_test_features, np_train_labels, features_to_select)



"""##Plotting"""

# summarize class distribution
counter = Counter(train_labels)
print(counter)

# scatter plot of examples by class label
for label, _ in counter.items():
 row_ix = where(np.array(train_labels) == label)[0]
 pyplot.scatter(selected_train_features[row_ix, 0], selected_train_features[row_ix, 1], label=str(label))
pyplot.legend()
pyplot.show()

"""#Training

##Decision Trees
"""

# https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, VotingClassifier, BaggingClassifier, HistGradientBoostingClassifier, ExtraTreesClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
import joblib
clf1 = AdaBoostClassifier()
clf2 = RandomForestClassifier(n_estimators=50, random_state=1)
clf4 = DecisionTreeClassifier()
clf6 = BaggingClassifier()
clf7 = HistGradientBoostingClassifier()
clf8 = ExtraTreesClassifier()
clf10 = XGBClassifier(n_estimators=2, max_depth=2, learning_rate=1, objective='binary:logistic')
dt_classifier = VotingClassifier([('lr', clf1), ('rf', clf2), ('dt', clf4), ('bc', clf6), ('hgb', clf7), ('etc', clf8), ('xgb', clf10)], voting='soft')
dt_classifier = dt_classifier.fit(selected_train_features, np_train_labels)

joblib.dump(dt_classifier, "VotingModel.joblib")

#tree.plot_tree(dt_classifier);

# """Predict on testing samples"""

dt_classes = dt_classifier.predict(selected_test_features)

from sklearn.metrics import confusion_matrix, classification_report

# Create heatmap from the confusion matrix
def createConfMatrix(class_names, matrix):
    class_names=[0, 1]
    tick_marks = [0.5, 1.5]
    fig, ax = plt.subplots(figsize=(7, 6))
    sns.heatmap(pd.DataFrame(matrix), annot=True, cmap="Blues", fmt='g')
    ax.xaxis.set_label_position("top")
    plt.title('Confusion matrix')
    plt.ylabel('Actual label'); plt.xlabel('Predicted label')
    plt.yticks(tick_marks, class_names); plt.xticks(tick_marks, class_names)

# Create a confusion matrix
cnf_matrix = confusion_matrix(test_labels, dt_classes)
createConfMatrix(matrix=cnf_matrix, class_names=[0, 1])

def print_performance(cnf_matrix):
    TP = cnf_matrix[1][1]
    TN = cnf_matrix[0][0]
    FP = cnf_matrix[0][1]
    FN = cnf_matrix[1][0]
    print('True Positives:', TP)
    print('True Negatives:', TN)
    print('False Positives:', FP)
    print('False Negatives:', FN)

    # calculate accuracy
    conf_accuracy = (float (TP+TN) / float(TP + TN + FP + FN))

    # calculate mis-classification
    conf_misclassification = 1- conf_accuracy

    # calculate the sensitivity
    conf_sensitivity = (TP / float(TP + FN))
    # calculate the specificity
    conf_specificity = (TN / float(TN + FP))

    print('Acc:', conf_accuracy)
    print('Err:', conf_misclassification)
    print('Sen:', conf_sensitivity)
    print('Spe:', conf_specificity)

print_performance(cnf_matrix)

"""|

|

|

#Independent/External Testing
"""

this_classifier = dt_classifier

"""Load testing data samples"""

import pathlib

test_path = "../../complete_set/testing_set/"
test_folder = pathlib.Path(test_path)
study_testset = list(test_folder.glob('P???.png'))

print(study_testset)

# Define tst_images array
tst_studies = np.zeros((100,size_x,size_y))
tst_masks = np.zeros((100,size_x,size_y))

for cname in (study_testset):
    head_, cname_erase = ntpath.split(cname)
    cname_erase = os.path.splitext(cname_erase)[0]
    # print(cname_erase)
    study_id = int(cname_erase[1:])
    # print(study_id)
    tst_imagePath = test_path + '/' + cname_erase + '.png'
    tst_image = cv2.imread(tst_imagePath,cv2.IMREAD_GRAYSCALE)

    tst_image = cv2.resize(tst_image,(size_x,size_y))
    tst_image = np.array(tst_image)
    tst_studies[study_id - 1] = tst_image

    # Load corresponding mask
    msk_imagePath = test_path + cname_erase + '_mask.png'
    msk_image = cv2.imread(msk_imagePath,cv2.IMREAD_GRAYSCALE)
    msk_image = cv2.resize(msk_image,(size_x,size_y))

    msk_image = np.array(msk_image)
    tst_masks[study_id - 1]+= np.array(msk_image)

tst_studies = tst_studies
tst_masks = tst_masks

tst_masks[tst_masks > 0] = 1

"""Show some example"""

plt.figure(figsize = (20,12))

for i in range(10) :
    plt.subplot(2,10,i+1)
    plt.imshow(np.squeeze(tst_studies[i]), 'gray')
    plt.title('P' + str(i+1))
    plt.axis('off')

for i in range(10) :
    plt.subplot(2,10,i+11)
    plt.imshow(np.squeeze(tst_masks[i]), 'gray')
    plt.title('Masks')
    plt.axis('off')
plt.show()

"""Apply feature extraction"""

# Extract features from Benign and Malignant studies
for i in range(len(tst_studies)):
  features_currentStudy = extractor.execute(GetImageFromArray(tst_studies[i]),
                    GetImageFromArray((tst_masks[i]).astype(np.uint8)),
                    label = 1)

  # Stack DataFrames
  if i == 0:
    tst_extracted_features = pd.DataFrame([features_currentStudy])
  else:
    tst_extracted_features = pd.concat( [tst_extracted_features, pd.DataFrame([features_currentStudy])], ignore_index=True )

tst_extracted_features.head()

tst_extracted_features = tst_extracted_features[value_feature_names]

tst_extracted_features.head()

dataset.head()

print(tst_extracted_features)

"""Apply feature selection (optional)"""

np_extst_features = tst_extracted_features.to_numpy()

# Apply feature selection
fdr_, sorted_fdr_, selected_extst_features, selected_extst_index = compute_fdr(np_extst_features, np_train_labels, features_to_select)

print(selected_extst_features[0,:])

print(selected_train_features[0,:])

"""##Plotting"""

extst_labels = [2] * 100
train_labels = train_labels.astype(int)
extst_labels = np.array(extst_labels).astype(int)
counter = Counter(np.concatenate((train_labels, extst_labels)))
print(counter)

all_data = np.concatenate((selected_train_features, selected_extst_features), axis=0)

# scatter plot of examples by class label
for label, _ in counter.items():
 row_ix = where(np.concatenate((train_labels, extst_labels)) == label)[0]
 pyplot.scatter(all_data[row_ix, 0], all_data[row_ix, 1], label=str(label))
pyplot.legend()
pyplot.show()

"""Classify"""

# Use the classifier on the test data
tst_class = this_classifier.predict(selected_extst_features)
tst_predictions = this_classifier.predict_proba(selected_extst_features)

print(tst_class)

print(tst_predictions)

"""Export to csv"""

sample_submission = pd.read_csv("sample_submission_auc.csv")

submission = pd.DataFrame()
submission['Id'] = sample_submission['Id']
submission['Predicted'] = tst_predictions[:,1]
submission.to_csv('submission.csv', index=False)


