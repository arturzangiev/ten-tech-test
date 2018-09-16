from rest_framework.viewsets import ModelViewSet

from shop.models import Brand, Footwear, Hat, Order
from shop.serializers import BrandSerializer, FootwearSerializer, HatSerializer, IndividualHatSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication


class BrandViewSet(ModelViewSet):
    """Brand views everything included."""

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    authentication_classes = [TokenAuthentication, ]


class FootwearViewSet(ModelViewSet):
    """Footwear views everything included."""

    queryset = Footwear.objects.all().order_by('price')
    serializer_class = FootwearSerializer
    authentication_classes = [TokenAuthentication,]


class HatViewSet(ModelViewSet):
    """Hat views everything included."""

    queryset = Hat.objects.all().order_by('price')
    serializer_class = HatSerializer
    authentication_classes = [TokenAuthentication, ]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = IndividualHatSerializer(instance)
        return Response(serializer.data)


class BasketViewSet(ModelViewSet):
    """Brand views everything included."""
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication, ]

    def get_queryset(self):
        if self.request.user.is_superuser is True:
            queryset = Order.objects.all()
        else:
            queryset = Order.objects.all().filter(user=self.request.user)

        return queryset

    def create(self, request, *args, **kwargs):
        # data = request.data
        order = Order.objects.create(user=self.request.user)
        order.save()

        serializer = BasketViewSet(order)
        return Response(serializer.data)

        # print(data)