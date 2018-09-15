from rest_framework import serializers

from shop.models import Brand, Footwear, Hat


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    """Brand serializer."""

    class Meta:
        model = Brand
        fields = '__all__'


class FootwearSerializer(serializers.HyperlinkedModelSerializer):
    """Footwear serializer."""

    class Meta:
        model = Footwear
        fields = ['url', 'price_currency', 'price', 'brand']


class HatSerializer(serializers.HyperlinkedModelSerializer):
    """Hat serializer."""

    class Meta:
        model = Hat
        fields = '__all__'
