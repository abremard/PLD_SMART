"""
Not working, giving up scripted drive upload
"""

# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
#
# gauth = GoogleAuth()
# gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
# drive = GoogleDrive(gauth)
#
# upload_file_list = ["th07_05.mid"]
# for upload_file in upload_file_list:
# 	gfile = drive.CreateFile({'parents': [{'id': '1MpcF4DM-SQz8P6VQLZqFj_vw0DKeBD50'}]})
# 	# Read file and set it as the content of this instance.
# 	gfile.SetContentFile(upload_file)
# 	gfile.Upload() 			# Upload the file.
# 	print(f"uploaded file {upload_file}")

import json
import os
import requests

access_token = "_4OgLWE14MEnR4p50w5sB7hS"
filename = './th07_05.mid'

filesize = os.path.getsize(filename)

# 1. Retrieve session for resumable upload.
headers = {"Authorization": "Bearer "+access_token, "Content-Type": "application/json"}
print(f'Headers: \n{headers}')

params = {
    "name": "TEST_FILE_DELETE_PLZ.mid",
    "mimeType": "audio/midi"
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=resumable",
    headers=headers,
    data=json.dumps(params)
)
print(r.status_code)
print(r.headers)
location = r.headers['Location']

# 2. Upload the file.
headers = {"Content-Range": "bytes 0-" + str(filesize - 1) + "/" + str(filesize)}
r = requests.put(
    location,
    headers=headers,
    data=open(filename, 'rb')
)
print(r.text)
