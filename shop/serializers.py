from rest_framework import serializers

from shop.models import Brand, Footwear, Hat, Order


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
        fields = ('url', 'colour', 'price_currency', 'price', 'brand', 'brand_meta')


class IndividualHatSerializer(serializers.ModelSerializer):
    """Hat serializer."""

    class Meta:
        model = Hat
        fields = ('price', 'brand_meta')


class OrderSerializer(serializers.ModelSerializer):
    """Hat serializer."""

    # hat = HatSerializer(many=True)
    # footwear = FootwearSerializer(many=True, read_only=True)

    # hat = serializers.PrimaryKeyRelatedField(many=True)
    # footwear = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Order
        # fields = '__all__'

        fields = ('id', 'created_date', 'updated_date', 'user', 'hat', 'footwear', 'total_hat', 'total_footwear', 'total_all')
