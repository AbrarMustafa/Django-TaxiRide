from rest_framework import serializers
from riders.models import RiderProfile, SavedAddress
from authapp.api.serializers import UserModelSerializer


class RiderProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    user = UserModelSerializer(many=False)
    class Meta:
        model = RiderProfile
        fields = [ "id" , "user", "profile_picture", "account_status", "created_on", "edited_at" ]
    
    def create(self, validated_data):
        get_request = self.context["request"]
        rider = RiderProfile(
            **validated_data
        )
        rider.user = get_request.user

        rider.save()

        return rider



class SavedAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedAddress
        fields = [ "id", "address" ]
    
    def create(self, validated_data):
        get_request = self.context["request"]
        address = SavedAddress(
            **validated_data
        )
        address.rider = get_request.user.rider_profile

        address.save()

        return address