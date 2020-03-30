import cv2
import tensorflow as tf

CATEGORIES = ["O", "R"]


def prepare(filepath):
    IMG_SIZE = 70  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


model = tf.keras.models.load_model("64x3-CNN.model")

print('\nPrediction 1: Image 1 of R folder:\n')
prediction = model.predict([prepare('/home/shrinidhi/Desktop/sem6/Waste-Classification-App/Model/TRAIN/R/R_1.jpg')])
# print(prediction)  # will be a list in a list.
print(CATEGORIES[int(prediction[0][0])])

print('\nPrediction 2: Image 1 of O folder:\n')
prediction = model.predict([prepare('/home/shrinidhi/Desktop/sem6/Waste-Classification-App/Model/TRAIN/O/O_1.jpg')])
# print(prediction)  # will be a list in a list.
print(CATEGORIES[int(prediction[0][0])])