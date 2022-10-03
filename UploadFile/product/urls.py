from itertools import product
from django.urls import path , include
from .views import *

urlpatterns = [
    path("", Product.as_view()),
]