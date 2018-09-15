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
        exclude = ('style',)


class HatSerializer(serializers.ModelSerializer):
    """Hat serializer."""

    brand = serializers.StringRelatedField(many=True)

    class Meta:
        model = Hat
        fields = '__all__'





