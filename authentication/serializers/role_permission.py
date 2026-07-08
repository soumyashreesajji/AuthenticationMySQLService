from rest_framework import serializers
from ..models import RolePermission


class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermission
        fields = "__all__"
        read_only_fields = ("id",)