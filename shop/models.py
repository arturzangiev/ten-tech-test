from django.db import models
from django.utils.translation import ugettext_lazy as _

from djmoney.models.fields import MoneyField
from multiselectfield import MultiSelectField


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


class Hat(models.Model):
    FEDORA = 'FED'
    TOP_HAT = 'TOP'
    TRILBY = 'TBY'
    PANAMA = 'PNM'
    FEZ = 'FEZ'
    CAP = 'CAP'
    STYLES = (
        (FEDORA, 'Fedora'),
        (TOP_HAT, 'Top Hat'),
        (TRILBY, 'Trilby'),
        (PANAMA, 'Panama'),
        (FEZ, 'Fez'),
        (CAP, 'Cap'),
    )
    style = models.CharField(_('style'), max_length=3, choices=STYLES)
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
            brand=self.brand.all().values('name'),
            price=self.price,
        )

    def __str__(self):
        return self.__unicode__()


class Footwear(models.Model):
    OXFORD = 'OXF'
    DERBY = 'DRB'
    BROGUE = 'BRG'
    MONK = 'MNK'
    BALMORAL = 'BML'
    STYLES = (
        (OXFORD, 'Oxford'),
        (DERBY, 'Derby'),
        (BROGUE, 'Brogue'),
        (MONK, 'Monk'),
        (BALMORAL, 'Balmoral'),
    )
    style = MultiSelectField(choices=STYLES)
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
