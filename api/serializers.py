from pp.models import Pizza
from rest_framework import serializers


class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pizza
        fields = ['title', 'body', 'price']