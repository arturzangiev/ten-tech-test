from django.db import models
from django.utils.translation import ugettext_lazy as _
from djmoney.models.fields import MoneyField
from django.conf import settings
from django.db.models import Sum

User = settings.AUTH_USER_MODEL


class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()


class HatStyle(models.Model):
    name = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=3)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()


class Hat(models.Model):
    style = models.ForeignKey(HatStyle, verbose_name=_('style'), related_name='hat')
    colour = models.CharField(max_length=20, null=True, blank=True)
    brand = models.ManyToManyField(Brand, verbose_name=_('brand'), related_name='hats', blank=True)
    price = MoneyField(max_digits=6, decimal_places=2, default_currency='GBP')

    class Meta:
        verbose_name = 'Hat'
        verbose_name_plural = 'Hats'

    @property
    def brand_meta(self):
        return self.brand.all().values('name')

    def __unicode__(self):
        return '{style_of_hat} by {brand} at {price}'.format(
            style_of_hat=self.style,
            brand=list(self.brand.all().values_list('name')),
            price=self.price,
        )

    def __str__(self):
        return self.__unicode__()


class FootwearStyle(models.Model):
    name = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=3)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()


class Footwear(models.Model):
    style = models.ManyToManyField(FootwearStyle)
    brand = models.ForeignKey(Brand, verbose_name=_('brand'), related_name='footwear')
    price = MoneyField(max_digits=6, decimal_places=2, default_currency='GBP')

    class Meta:
        verbose_name = 'Footwear'
        verbose_name_plural = 'Footwear'

    @property
    def brand_meta(self):
        return {"name": self.brand.name, "description": self.brand.description}

    def __unicode__(self):
        return '{style_of_footwear} by {brand} at {price}'.format(
            style_of_footwear=self.style,
            brand=self.brand.name,
            price=self.price,
        )

    def __str__(self):
        return self.__unicode__()


class Order(models.Model):
    hat = models.ManyToManyField(Hat, blank=True)
    footwear = models.ManyToManyField(Footwear, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def total_hat(self):
        return self.hat.all().aggregate(Sum('price'))

    @property
    def total_footwear(self):
        return self.footwear.all().aggregate(Sum('price'))


    # def __unicode__(self):
    #     return self.id
    #
    # def __str__(self):
    #     return self.__unicode__()