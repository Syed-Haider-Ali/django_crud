
from django.urls import path
from .views import MakeAPIView, VechileAPIView
from . import views

urlpatterns = [
    path('vechile' , VechileAPIView.as_view({'get':'get', 
                                             'post':'post',
                                             'patch':'update',
                                             'delete':'delete'}), name='vechile_view'),

    path('vechile/aggregate', VechileAPIView.as_view({"get":"get_aggregate"})),
                                             
    path('make' , MakeAPIView.as_view({'get':'get', 
                                             'post':'post',
                                             'patch':'update',
                                             'delete':'delete'}), name='make_view')
]
