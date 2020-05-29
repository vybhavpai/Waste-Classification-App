from firebase import firebase

firebase = firebase.FirebaseApplication(
    'https://waste-classifier-e9d77.firebaseio.com/', None)

firebase.delete('/Classification', '-M3BtYFSQm12iF2X-4Fy')
print('Record deleted')
