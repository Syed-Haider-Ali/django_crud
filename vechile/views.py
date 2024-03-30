from rest_framework.viewsets import ModelViewSet
from .controller import *
from rest_framework.response import Response
from .serializer import VechileSerializer, MakeSerializer



vechile_controller = VechileController()
make_controller = MakeController()




class VechileAPIView(ModelViewSet):
    serializer_class = VechileSerializer
    def get(self,request):
        return vechile_controller.get_v2(request)

    def post(self,request):
        return vechile_controller.post(request)

    def update(self,request):
        return vechile_controller.update(request)

    def delete(self,request):
        return vechile_controller.delete(request)

    def get_aggregations(self, request):
        return vechile_controller.get_aggregations(request)
    
    def get_annotations(self, request):
        return vechile_controller.get_annotations(request)




class MakeAPIView(ModelViewSet):
    serializer_class = MakeSerializer
    def get(self,request):
        return make_controller.get(request)

    def post(self,request):
       return make_controller.post(request)

    def update(self,request):
        return make_controller.update(request)

    def delete(self,request):
        return make_controller.delete(request)