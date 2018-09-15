from rest_framework.viewsets import ModelViewSet

from shop.models import Brand, Footwear, Hat
from shop.serializers import BrandSerializer, FootwearSerializer, HatSerializer


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
