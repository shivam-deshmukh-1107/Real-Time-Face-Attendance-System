import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://faceattendencerealtime-d1917-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')

data = {
    "123456": {
        'name': "Shivam Deshmukh",
        'major': "Mechanical",
        'starting_year': 2019,
        'total_attendance': 8,
        'standing': "G",
        'year': 4,
        'last_attendance_time': "2023-07-11 00:54:34"
    },
    "852741": {
        'name': "Emly Blunt",
        'major': "Computer Science",
        'starting_year': 2018,
        'total_attendance': 3,
        'standing': "F",
        'year': 2,
        'last_attendance_time': "2023-08-11 00:54:34"
    },
    "963852": {
        'name': "Elon Musk",
        'major': "Aero Space",
        'starting_year': 2020,
        'total_attendance': 6,
        'standing': "VG",
        'year': 4,
        'last_attendance_time': "2023-07-11 00:54:34"
    }
}

for key, value in data.items():
    ref.child(key).set(value)
