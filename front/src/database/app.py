import flask
from flask import request, jsonify, send_file, make_response, redirect, url_for, Flask
import firebase_admin
from datetime import datetime
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("firestore/cred.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)
@app.route('/', methods=['GET'])
def api_server_name():
    
    doc_ref = db.collection('ids').document('serverid')
    doc = doc_ref.get()
    doc = doc.to_dict()
    #my_dict = { el.id: el.to_dict() for el in doc }
    print(doc)
    if doc['idd'] is not None:
        resp = make_response(jsonify(doc))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        
        return resp
    else:
        return "No server name found!"


