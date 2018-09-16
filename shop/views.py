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
        data = request.data
        hat_ids = data.get('hat') if isinstance(data.get('hat'), (list,)) else list()
        footwear_ids = data.get('footwear') if isinstance(data.get('footwear'), (list,)) else list()
        order = Order.objects.create(user=self.request.user)
        for hat_id in hat_ids:
            hat = Hat.objects.get(id=hat_id)
            order.hat.add(hat)
        for footwear_id in footwear_ids:
            footwear = Footwear.objects.get(id=footwear_id)
            order.footwear.add(footwear)

        order.save()

        return Response("Order is placed")