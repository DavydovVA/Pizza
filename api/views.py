from .serializers import PizzaSerializer, UserSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from pp.models import Pizza
from accounts.models import User


class PizzaApi(ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]


class UserApi(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAdminUser]
