from rest_framework import serializers
from app_settings.models import SiteSetting


class AppConfigSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSetting
        fields = [ "base_price", "price_minute", "price_km"]