from django.urls import path

from items.views import home

urlpatterns = [

path('', home, name='home')

]
