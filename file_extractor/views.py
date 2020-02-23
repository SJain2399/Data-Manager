from django.shortcuts import render
from django.http import HttpResponse
import pickle
from googleapiclient.discovery import build
from file_extractor.models import DriveFiles
import dropbox
from dropbox import DropboxOAuth2Flow


# Create your views here.
def init(creds):
    service = build('drive', 'v3', credentials=creds)
    # Call the Drive v3 API
    results = service.files().list(
        pageSize=100, fields="nextPageToken, files(id, name, kind, createdTime, modifiedTime, mimeType)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} {1} {2} {3} {4} {5}'.format(item['kind'], item['id'], item['name'], item['createdTime'], item['modifiedTime'], item['mimeType']))
            dFile = DriveFiles(kind = item['kind'], id = item['id'], name = item['name'], createdTime = (item['createdTime'].replace("T", " "))[:-5], modifiedTime = (item['modifiedTime'].replace("T", " "))[:-5], mimeType = item['mimeType'] )
            dFile.save()

def extractGoogleDoc(creds):
    service = build('drive', 'v3', credentials=creds)
    lastCheckedIn = '2020-02-23 10:00:00'
    # Call the Drive v3 API
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name, kind, createdTime, modifiedTime, mimeType)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:', items)
        createdItems = filter(lambda obj : obj['createdTime']>lastCheckedIn, items)
        print('Created Items :', list(createdItems))
        updatedItems = filter(lambda obj : obj['modifiedTime']>lastCheckedIn, items)
        print('Updated Items :', list(updatedItems))
        for item in createdItems:
            print(u'{0} {1} {2} {3} {4} {5}'.format(item['kind'], item['id'], item['name'], item['createdTime'], item['modifiedTime'], item['mimeType']))
            dFile = DriveFiles(kind = item['kind'], id = item['id'], name = item['name'], createdTime = (item['createdTime'].replace("T", " "))[:-5], modifiedTime = (item['modifiedTime'].replace("T", " "))[:-5], mimeType = item['mimeType'] )
            dFile.save()
        for item in updatedItems:
            dFile = DriveFiles.objects.get(item['id'])
            dFile.modifiedTime = item['modifiedTime']
            dFile.save()

# def extractDropbox():
#     dbx = dropbox.Dropbox('bNLnsngQBLAAAAAAAAAAGha2ok1IvyUzk0xSMYxlVqOfBfXgmU2pFkIu1YcI1vIW')
#     print(dbx.users_get_current_account())
#     for entry in dbx.files_list_folder('').entries:
#         print(entry.name)


def get_dropbox_auth_flow(web_app_session):
    redirect_uri = "https://my-web-server.org/dropbox-auth-finish"
    return DropboxOAuth2Flow(
        '0azi3qhn16dgofm', 'trpjwzdmwqo0wd9', redirect_uri, web_app_session,
        "dropbox-auth-csrf-token")

# URL handler for /dropbox-auth-start
def dropbox_auth_start(web_app_session, request):
    authorize_url = get_dropbox_auth_flow(web_app_session).start()
    redirect_to(authorize_url)

# URL handler for /dropbox-auth-finish
def dropbox_auth_finish(web_app_session, request):
    # try:
        oauth_result = \
                get_dropbox_auth_flow(web_app_session).finish(
                    request.query_params)
#     except BadRequestException, e:
#         return http_status(400)
#     except BadStateException, e:
#         # Start the auth flow again.
#         redirect_to("/dropbox-auth-start")
#     except CsrfException, e:
#         http_status(403)
#     except NotApprovedException, e:
#         flash('Not approved?  Why not?')
#         return redirect_to("/home")
#     except ProviderException, e:
#         logger.log("Auth error: %s" % (e,))
#         http_status(403)

