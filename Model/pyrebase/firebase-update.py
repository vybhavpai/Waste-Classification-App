from firebase import firebase

firebase = firebase.FirebaseApplication(
    'https://waste-classifier-e9d77.firebaseio.com/', None)

firebase.put('/Classification/-M3BtYFSQm12iF2X-4Fy', 'Category', 'O')
print('Record updated')