import tensorflow as tf 
import os
import cv2
import imghdr
from matplotlib import pyplot as plt
from keras.models import load_model

tf.config.threading.set_inter_op_parallelism_threads(6)

pretrained_model = load_model('foundation_model/breastcanc_classifier_enriched.h5')


# Optionally freeze layers
for layer in pretrained_model.layers:
    layer.trainable = False  # Freeze all layers

# Compile the model
pretrained_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

pretrained_model.trainable = True

data_dir = 'complete_set/training3'
image_exts = ['jpeg','jpg', 'bmp', 'png']

for image_class in os.listdir(data_dir): 
    for image in os.listdir(os.path.join(data_dir, image_class)):
        image_path = os.path.join(data_dir, image_class, image)
        try: 
            img = cv2.imread(image_path)
            tip = imghdr.what(image_path)
            if tip not in image_exts: 
                print('Image not in ext list {}'.format(image_path))
                os.remove(image_path)
        except Exception as e: 
            print('Issue with image {}'.format(image_path))
            # os.remove(image_path)

data = tf.keras.utils.image_dataset_from_directory(data_dir)

data_iterator = data.as_numpy_iterator()

batch = data_iterator.next()

fig, ax = plt.subplots(ncols=4, figsize=(20,20))
for idx, img in enumerate(batch[0][:4]):
    ax[idx].imshow(img.astype(int))
    ax[idx].title.set_text(batch[1][idx])

fig.savefig("valdata.png")

data = data.map(lambda x,y: (x/255, y))
data.as_numpy_iterator().next()

train_size = int(len(data)*.7)
val_size = int(len(data)*.2)
test_size = int(len(data)*.1)
train = data.take(train_size)
val = data.skip(train_size).take(val_size)
test = data.skip(train_size+val_size).take(test_size)

logdir='logs'

tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=logdir)

# Train the model on new data
pretrained_model.fit(train, epochs=20, validation_data=val, callbacks=[tensorboard_callback])

pretrained_model.save(os.path.join('foundation_model','breastcanc_classifier_enriched2.keras'))
