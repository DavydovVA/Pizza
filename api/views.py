from .serializers import PizzaSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from pp.models import Pizza


# can insert CreateApiView
class PizzaApi(ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]
