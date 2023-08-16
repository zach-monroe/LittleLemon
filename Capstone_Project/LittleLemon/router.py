from rest_framework.routers import DefaultRouter
from LittleLemon.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)