from firebase import firebase

firebase = firebase.FirebaseApplication(
    'https://waste-classifier-e9d77.firebaseio.com/', None)

data = {
    'ID': '1234',
    'Category': 'O'
}

result = firebase.post('/Classification', data)
print(result)
