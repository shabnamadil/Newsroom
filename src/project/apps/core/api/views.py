from rest_framework.generics import (
    CreateAPIView,
    ListAPIView)

from .serializers import (
    ContactSerializer,
    WebsiteInformationSerializer
    )

from apps.core.models import WebsiteInformation


class ContactCreateAPIView(CreateAPIView):
    serializer_class = ContactSerializer


class WebsiteRetrieveAPIView(ListAPIView):
    serializer_class = WebsiteInformationSerializer
    queryset = WebsiteInformation.objects.filter(pk=1)