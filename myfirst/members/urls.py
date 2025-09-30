from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', include('members.url')),
    path('admin/', admin.site.urls),
]
