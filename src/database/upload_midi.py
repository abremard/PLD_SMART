
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate("./cred.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


if __name__ == "__main__":
    print("yo")
