from django.urls import path, include
from .views import MenuItemView, BookingViewSet, SingleMenuItemView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', BookingViewSet)
urlpatterns = [
    path('menu/', MenuItemView.as_view(), name='Menu'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name="Menu-Item"),
    path('booking/', include(router.urls)),
]
