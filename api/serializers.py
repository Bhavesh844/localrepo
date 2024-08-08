from rest_framework import serializers
from api.models import company,employee

class comany_serializers(serializers.HyperlinkedModelSerializer):
    compaid=serializers.ReadOnlyField()
    class Meta:
        model=company
        fields='__all__'

class employee_serializers(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=employee
        fields='__all__'

