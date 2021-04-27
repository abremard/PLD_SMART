import firebase_admin
from firebase_admin import credentials, firestore

# ----------- Initialize Firebase connexion
# Use a service account
cred = credentials.Certificate("./cred.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def addGenre(genre: str, file_ref: str):
    genre_ref = db.collection(u"Tags").document(u"Genres")
    # Set the capital field
    genre_ref.update({genre: firestore.ArrayUnion([file_ref])})

