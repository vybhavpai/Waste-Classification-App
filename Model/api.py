import urllib.request
import time
import threading
from firebase import firebase
import json
import cv2
import tensorflow as tf
import pyrebase

config = {
    "apiKey": "AIzaSyDbJ0lO5374Cy7OZK6M1e_M2vSv94DCL4E",
    "authDomain": "waste-classifier-e9d77.firebaseapp.com",
    "databaseURL": "https://waste-classifier-e9d77.firebaseio.com",
    "projectId": "waste-classifier-e9d77",
    "storageBucket": "waste-classifier-e9d77.appspot.com",
    "messagingSenderId": "658153954358",
    "appId": "1:658153954358:web:a891d693c73b2b85144c97"
}

firebase_storage = pyrebase.initialize_app(config)
storage = firebase_storage.storage()
CATEGORIES = ["O", "R"]


def prepare(filepath):
    IMG_SIZE = 70  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


model = tf.keras.models.load_model("64x3-CNN.model")


firebase = firebase.FirebaseApplication(
    'https://waste-classifier-e9d77.firebaseio.com/', None)


def fetchImages():
    print(time.ctime())

    # fetch items
    result = firebase.get('/Classification', '')
    for (k, v) in result.items():
        # print(k)
        # print(v)
        # check for the ones that are null and note the urls. fetch the images from those urls
        if v['mCategory'] == '':
            # print(v['mImageUrl'])

            # path_on_cloud = v['mImageUrl']
            b = 'jpg' in v['mImageUrl']
            if b:
                urllib.request.urlretrieve(
                    v['mImageUrl'], v['mID']+"-waste.jpg")
                predict(v['mID']+"-waste.jpg", v['mID'])
            else:
                urllib.request.urlretrieve(
                    v['mImageUrl'], v['mID']+"-waste.png")
                predict(v['mID']+"-waste.png", v['mID'])

        # so the image is downloading and predicting so far. Now need to update the entry in the database
            # time.sleep(5)

    # threading.Timer(10, fetchImages).start()


def predict(filepath, mID):
    # predict the result
    prediction = model.predict([prepare(filepath)])
    print(filepath + '--->' + CATEGORIES[int(prediction[0][0])])
    # update the result in database
    firebase.put('/Classification/' + mID, 'mCategory',
                 CATEGORIES[int(prediction[0][0])])
    print('Record updated')


fetchImages()
