from django.shortcuts import render
from django.http import HttpResponse
import pickle
from googleapiclient.discovery import build

# Create your views here.
def extractGoogleDoc(creds):
    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name, kind, createdTime, modifiedTime)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} {1} {2} {3} {4}'.format(item['kind'], item['id'], item['name'], item['createdTime'], item['modifiedTime']))

