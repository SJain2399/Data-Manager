from django.urls import path

from . import views

urlpatterns = [
    #path('dropboxAuth/', views.get_dropbox_auth_flow),
    path('dropBoxAuth/', views.dropbox_auth_start)
    #path('dropBoxauthFinish/', views.dropbox_auth_finish)
]