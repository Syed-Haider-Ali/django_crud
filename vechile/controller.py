from utils.reusable_classes import BaseAPIController
from .serializer import *
from .filters import *

from utils.response_messages import *
from utils.reusable_methods import *
from .models import *
from django.db.models import F, Count, Sum, Avg, Min, Max



class MakeController(BaseAPIController):
    serializer_class = MakeSerializer
    filterset_class = MakeFilter


class VechileController(BaseAPIController):
    serializer_class = VechileSerializer
    filterset_class = VechileFilter

    def get(self,request):
        instances = self.serializer_class.Meta.model.objects.select_related('make').all()
        
        filtered_data = self.filterset_class(request.GET, queryset=instances)
        data = filtered_data.qs
        
        if not data:   
            return create_response({}, NO_RECORD, 200)
        paginated_data = paginate_data(data, request)
        count = data.count()
        
        serialized_data = self.serializer_class(paginated_data, many=True).data
        response_data = {
            "count":count,
            "data":serialized_data,
        }
        return create_response(response_data, SUCCESSFUL, 200)


    def get_aggregate(self, request):
        try:
            instances = self.serializer_class.Meta.model.objects.all()
            avg_purchase_rate = instances.aggregate(avg=Avg('purchase_rate'))
            max_purchase_rate = instances.aggregate(max=Max('purchase_rate'))
            min_purchase_rate = instances.aggregate(min=Min('purchase_rate'))
            sum_purchase_rate = instances.aggregate(sum=Sum('purchase_rate'))

            avg_price = instances.aggregate(avg=Avg('price'))
            max_price = instances.aggregate(max=Max('price'))
            min_price = instances.aggregate(min=Min('price'))
            sum_price = instances.aggregate(sum=Sum('price'))



            response_data = {
                "avg_purchase_rate": avg_purchase_rate['avg'],
                "max_purchase_rate": max_purchase_rate['max'],
                "min_purchase_rate": min_purchase_rate['min'],
                "sum_purchase_rate": sum_purchase_rate['sum'],

                "avg_price": avg_price['avg'],
                "max_price": max_price['max'],
                "min_price": min_price['min'],
                "sum_price": sum_price['sum']

            }
            return create_response(response_data, SUCCESSFUL, 200)

        except Exception as e:
            return create_response({'error':str(e)}, UNSUCCESSFUL, 500)
