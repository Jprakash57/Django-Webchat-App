from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


# I have used serializers to convert my python format to json, it cant be done directly by python itslef
# so we have serializers for that which will convert all the python format to json response
# Futher is exlained in views 