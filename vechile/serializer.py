from rest_framework.serializers import ModelSerializer
from .models import Make, Vechile



class VechileSerializer(ModelSerializer):
    class Meta:
        model = Vechile
        fields ='__all__'

    def to_representation(self, instance):
        data = super(VechileSerializer, self).to_representation(instance)
        data["make"] = MakeSerializer(instance.make).data
        return data


class MakeSerializer(ModelSerializer):
    class Meta:
        model = Make
        fields ='__all__'
