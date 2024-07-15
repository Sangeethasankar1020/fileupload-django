# urls.py (in your Django app)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_to_firebase, name='upload_file'),
    # Other URL patterns as needed
]
