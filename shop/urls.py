"""Shop urls."""

from rest_framework_nested import routers

from shop.views import BrandViewSet, FootwearViewSet, HatViewSet, BasketViewSet


router = routers.SimpleRouter()

router.register(r'brands', BrandViewSet)
router.register(r'footwear', FootwearViewSet)
router.register(r'hats', HatViewSet)
router.register(r'basket', BasketViewSet, base_name='basket')
