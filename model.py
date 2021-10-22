import tensorflow as tf
import scipy
import os

from utils import list_file_name

dataset_folder=r'dataset\model_jpg'
train_dir = os.path.join(dataset_folder, 'train')
validation_dir = os.path.join(dataset_folder, 'validation')
train_sig_dir = os.path.join(train_dir, 'signatured')
train_unsig_dir = os.path.join(train_dir, 'unsignatured')
validation_sig_dir = os.path.join(validation_dir, 'signatured')
validation_unsig_dir = os.path.join(validation_dir, 'unsignatured')

train_generator = tf.keras.utils.image_dataset_from_directory(
                    directory = train_dir,
                    image_size = (128,128),
                    color_mode = 'grayscale',
                    batch_size = 32,
                    shuffle = True,
                    seed = 42
                    )
validation_generator = tf.keras.utils.image_dataset_from_directory(
                    directory = validation_dir,
                    image_size = (128,128),
                    color_mode = 'grayscale',
                    batch_size = 32,
                    shuffle = True,
                    seed = 42
                    )

AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_generator.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = validation_generator.cache().prefetch(buffer_size=AUTOTUNE)

from tensorflow.keras import layers, models
num_classes = 2

model = tf.keras.Sequential([
  layers.experimental.preprocessing.Rescaling(1./255, input_shape=(128, 128, 1)),
  layers.Conv2D(16, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Flatten(),
  layers.Dense(128, activation='relu'),
  layers.Dense(num_classes)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(train_ds, validation_data=val_ds, epochs=50, batch_size=32)


model.summary()

import glob
pathtest = r'dataset\test_jpg\*.jpg'
#pathtest=r'C:\Users\atefe\Desktop\b_d\test\*.tif'

def list_path(pathtrain_xml,pathtrain,pathtest):
    list_xml=glob.glob(pathtrain_xml)
    list_train=glob.glob(pathtrain)
    list_test=glob.glob(pathtest)
    return(list_xml,list_train,list_test)


test_images=glob.glob(pathtest)

prediction = []
score = []
for images in test_images:
    img = tf.keras.utils.load_img(images, target_size=(128, 128))
    im = tf.image.rgb_to_grayscale(img)
    img_array = tf.keras.utils.img_to_array(im)
    img_array = tf.expand_dims(img_array, 0)
    predictions = model.predict(img_array)

    score = tf.nn.softmax(predictions[0])
    prediction.append(predictions[0])
signatured_test = []
for predict in prediction:
    if predict[0] > predict[1]:
        signatured_test.append(1)
    if predict[0] < predict[1]:
        signatured_test.append(0)

patht = r'dataset\test_jpg'
d_t={}
Id_test=[]
for i in range(len(test_images)):
    name_file_test=list_file_name(patht)[i][:-4]
    Id_test.append(name_file_test)
    d_t[name_file_test]=signatured_test[i]
df_test=pd.DataFrame(list(d_t.items()),columns=['Id','Expected'])
df_test.to_csv('challange1.csv', index=False)