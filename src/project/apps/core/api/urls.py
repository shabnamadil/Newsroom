from django.urls import path
from .views import (
    ContactCreateAPIView,
    WebsiteRetrieveAPIView
)


urlpatterns = [
    path('contact/', ContactCreateAPIView.as_view(), name='contact'),
    path('website/', WebsiteRetrieveAPIView.as_view(), name='website')
]