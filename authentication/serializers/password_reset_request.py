from rest_framework import serializers
from ..models import PasswordResetRequest


class PasswordResetRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordResetRequest
        fields = "__all__"
        read_only_fields = ("id", "created_at")