from utils.reusable_classes import BaseAPIController
from .serializer import *
from .filters import *

from utils.response_messages import *
from utils.reusable_methods import *
from .models import *


class VechileController(BaseAPIController):
    serializer_class = VechileSerializer
    filterset_class = VechileFilter

class MakeController(BaseAPIController):
    serializer_class = MakeSerializer
    filterset_class = MakeFilter


            # reverse relation route
    # def get(self,request):
    #     # instances = self.serializer_class.Meta.model.objects.all()
    #     instan = Make.objects.get(id=8)
    #     instances = instan.vechile_set.all()
    #     filtered_data = self.filterset_class(request.GET, queryset=instances)
    #     data = filtered_data.qs
        
    #     if not data:   # filtered_qs
    #         return create_response({}, NO_RECORD, status_code=200)
    #     paginated_data = paginate_data(data, request)
    #     count = data.count()
        
    #     serialized_data = self.serializer_class(paginated_data, many=True).data
    #     response_data = {
    #         "count":count,
    #         "data":serialized_data,
    #     }
    #     return create_response(response_data, SUCCESSFUL, status_code=200)