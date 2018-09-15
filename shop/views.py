from rest_framework.viewsets import ModelViewSet

from shop.models import Brand, Footwear, Hat
from shop.serializers import BrandSerializer, FootwearSerializer, HatSerializer, IndividualHatSerializer
from rest_framework.response import Response


class BrandViewSet(ModelViewSet):
    """Brand views everything included."""

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class FootwearViewSet(ModelViewSet):
    """Footwear views everything included."""

    queryset = Footwear.objects.all().order_by('price')
    serializer_class = FootwearSerializer


class HatViewSet(ModelViewSet):
    """Hat views everything included."""

    queryset = Hat.objects.all().order_by('price')
    serializer_class = HatSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = IndividualHatSerializer(instance)
        return Response(serializer.data)
