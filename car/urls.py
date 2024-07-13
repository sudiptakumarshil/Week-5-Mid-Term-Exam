from django.urls import path
from .views import *

urlpatterns = [path('load-car-by-brand', LoadCarView.as_view(), name='car.by_brand')]
