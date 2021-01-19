from django.urls import path
from mysite01 import views


app_name = 'mysite01'

urlpatterns = [
    path(r'', views.index, name='Index')
]