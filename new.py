from googleapiclient.http import MediaFileUpload
from Google import Create_Service
import os

CLIENT_SECRET_FILE= 'client_secrets.json'
API_NAME= 'drive'
API_VERSION='v3'
SCOPES=['https://www.googleapis.com/auth/drive']

service= Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id='<Folder id for your Google drive folder>'

file_names=[input("\nEnter filename to write (Enter extenxion): ")]
mime_types=['text/plain']

for file_name, mime_type in zip(file_names,mime_types):
    file_metadata={
        'name':file_name,
        'parents':[folder_id]

    }

    media= MediaFileUpload('<path where the file to be uploaded is stored>'.format(file_name), mimetype=mime_type)

    service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
