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
    IMG_SIZE = 100  # 50 in txt-based
    img_array = cv2.imread(filepath)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE), 3)
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)


model = tf.keras.models.load_model("128x3-CNN-aug.hdf5")



firebase = firebase.FirebaseApplication(
    'https://waste-classifier-e9d77.firebaseio.com/', None)


def fetchImages():
    print(time.ctime())

    # fetch items
    # waiting because .com url needs to be changed to http url and updated in the firebase db
    time.sleep(4)
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
                # predict(v['mID']+"-waste.jpg", v['mID'])
                # predict the result
                prediction = model.predict([prepare(v['mID']+"-waste.jpg")])
                print(v['mID']+"-waste.jpg" + '--->' +
                      CATEGORIES[int(prediction[0][0])])
                # update the result in database
                firebase.put('/Classification/' + v['mID'], 'mCategory',
                             CATEGORIES[int(prediction[0][0])])
                print('Record updated')
            else:
                urllib.request.urlretrieve(
                    v['mImageUrl'], v['mID']+"-waste.png")
                # predict(v['mID']+"-waste.png", v['mID'])
                # predict the result
                prediction = model.predict([prepare(v['mID']+"-waste.png")])
                print(v['mID']+"-waste.jpg" + '--->' +
                      CATEGORIES[int(prediction[0][0])])
                # update the result in database
                firebase.put('/Classification/' + v['mID'], 'mCategory',
                             CATEGORIES[int(prediction[0][0])])
                print('Record updated')

        # so the image is downloading and predicting so far. Now need to update the entry in the database
            time.sleep(5)

    # threading.Timer(15, fetchImages).start()
    fetchImages()


def predict(filepath, mID):
    # predict the result
    prediction = model.predict([prepare(filepath)])
    print(filepath + '--->' + CATEGORIES[int(prediction[0][0])])
    # update the result in database
    firebase.put('/Classification/' + mID, 'mCategory',
                 CATEGORIES[int(prediction[0][0])])
    print('Record updated')


fetchImages()
