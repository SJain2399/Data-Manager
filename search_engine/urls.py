from django.urls import path
from . import views

urlpatterns = [
    path('elastic/', views.matchStr),
]
