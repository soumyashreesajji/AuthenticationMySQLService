from rest_framework import serializers
from ..models import RefreshToken


class RefreshTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefreshToken
        fields = "__all__"
        read_only_fields = ("id", "created_at")