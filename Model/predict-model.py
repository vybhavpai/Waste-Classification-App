import cv2
import tensorflow as tf

CATEGORIES = ["O", "R"]


def prepare(filepath):
    IMG_SIZE = 80  # 50 in txt-based
    img_array = cv2.imread(filepath)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE), 3)
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)


model = tf.keras.models.load_model("64x3-CNN.model") # here you can use 64 or 128

print('\nPrediction 1: Image from R folder:\n')
prediction = model.predict([prepare('/home/shrinidhi/Desktop/sem6/Waste-Classification-App/Model/TEST/R/R_10005.jpg')])
# print(prediction)  # will be a list in a list.
print(CATEGORIES[int(prediction[0][0])])

print('\nPrediction 2: Image from O folder:\n')
prediction = model.predict([prepare('/home/shrinidhi/Desktop/sem6/Waste-Classification-App/Model/TEST/O/O_12588.jpg')])
# print(prediction)  # will be a list in a list.
print(CATEGORIES[int(prediction[0][0])])