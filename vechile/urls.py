
from django.urls import path
from .views import MakeAPIView, VechileAPIView

urlpatterns = [
    path('vechile' , VechileAPIView.as_view({'get':'get', 
                                             'post':'post',
                                             'patch':'update',
                                             'delete':'delete'})),
                                             
    path('make' , MakeAPIView.as_view({'get':'get', 
                                             'post':'post',
                                             'patch':'update',
                                             'delete':'delete'}))
]
