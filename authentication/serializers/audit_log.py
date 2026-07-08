from rest_framework import serializers
from ..models import AuditLogs


class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLogs
        fields = "__all__"
        read_only_fields = ("id", "created_at")