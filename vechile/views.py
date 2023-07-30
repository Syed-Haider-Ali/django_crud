from rest_framework.viewsets import ModelViewSet


vechile_controller = ''
make_controller = ''

class VechileAPIView(ModelViewSet):
    def get(self,request):
        vechile_controller.get(request)

    def post(self,request):
        vechile_controller.post(request)

    def update(self,request):
        vechile_controller.update(request)

    def delete(self,request):
        vechile_controller.delete(request)


class MakeAPIView(ModelViewSet):
    def get(self,request):
        make_controller.get(request)

    def post(self,request):
        make_controller.post(request)

    def update(self,request):
        make_controller.update(request)

    def delete(self,request):
        make_controller.delete(request)