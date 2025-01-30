from django.urls import path
from .views import get_details

urlpatterns = [
    path('get_details/', get_details, name='get_details'),
    #path('mydetails/create_details/', create_details, name= 'create_details')
]