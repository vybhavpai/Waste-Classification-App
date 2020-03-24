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

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

# for uploading an image
# path_on_cloud = "images/foo.jpg"

# storage.child(path_on_cloud).put(path_local)
import os

# directory = '/home/shrinidhi/Desktop/sem6/Waste-Classification-App/Model'
# for filename in os.listdir(directory):
#     if filename.endswith(".jpg") or filename.endswith(".png"):
#         print(os.path.join(directory, filename))
#         path_on_cloud = "images/" + filename
#         storage.child(path_on_cloud).put(filename)
#     else:
#         continue

# download an image

path_on_cloud = "<path-of-the-image-in-firebase-storage>"
storage.child(path_on_cloud).download("classify-waste.jpg")
