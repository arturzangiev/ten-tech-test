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
        fields = ('url', 'price_currency', 'price', 'brand', 'brand_meta')
        # exclude = ('style',)


class HatSerializer(serializers.HyperlinkedModelSerializer):
    """Hat serializer."""

    class Meta:
        model = Hat
        fields = ('url', 'style', 'colour', 'price_currency', 'price', 'brand', 'brand_meta')


class IndividualHatSerializer(serializers.ModelSerializer):
    """Hat serializer."""

    class Meta:
        model = Hat
        fields = ('price', 'brand_meta')


