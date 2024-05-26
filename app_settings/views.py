from .api.serializers import AppConfigSettingsSerializer
from rest_framework import generics
from .models import SiteSetting


class SiteConfigsAPIVIEW(generics.ListAPIView):
    serializer_class = AppConfigSettingsSerializer
    queryset = SiteSetting.objects.all()

