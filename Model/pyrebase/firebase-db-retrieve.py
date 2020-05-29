from firebase import firebase

firebase = firebase.FirebaseApplication(
    'https://waste-classifier-e9d77.firebaseio.com/', None)
result = firebase.get('/Classification', '')
print(result)
