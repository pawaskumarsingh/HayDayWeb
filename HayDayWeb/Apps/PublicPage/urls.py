
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', home, name="home_page"),
]