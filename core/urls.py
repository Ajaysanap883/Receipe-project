from django.urls import path
from core.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('',student),
  path('delete-receipe/<id>',delete),
  path('update-receipe/<id>',update),
  path('register/',register),
  path('login_page/',login_page),
  path('logout/',logout_page)


    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
