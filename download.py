import io
from googleapiclient.http import MediaIoBaseDownload
from Google import Create_Service
from googleapiclient.discovery import build
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)

# Generate a client_secret.json file and store it
CLIENT_SECRET_FILE= '/home/user/path to the json file' # Update the variable to refelct the path of the json file 
API_NAME= 'drive'
API_VERSION='v3'
SCOPES=['https://www.googleapis.com/auth/drive']

service= Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('folder id of the drive folder where the file is stored')}).GetList()
for file in file_list:
	print('title: %s, id: %s' % (file['title'], file['id']))


file_ids=[input("Enter the file id: ")]
file_names=[input("Enter the file name to be downloaded: ")]



for file_id,file_name in zip(file_ids,file_names):
    request=service.files().get_media(fileId=file_id)

    fh=io.BytesIO()
    downloader= MediaIoBaseDownload(fd=fh, request=request)

    done=False

    while not done:
        status,done= downloader.next_chunk()
        print('Download progress{0}'.format(status.progress()*100))

    fh.seek(0)

    with open(os.path.join('<path to where the file is to be downloaded on local system>',file_name),'wb') as f:
        f.write(fh.read())
        f.close()


    
