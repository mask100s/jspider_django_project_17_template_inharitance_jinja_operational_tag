from django.urls import path
from app1.views import *

app_name='connect1'

urlpatterns = [
    path('parent/',parent, name='parent'),
    path('child/',child, name='child'),
]
