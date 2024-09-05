from rest_framework import serializers

from .models import Auther, ThreadPost


class AutherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auther
        fields = "__all__"

    def to_representation(self, instance):
        obj = super().to_representation(instance)
        obj["first_name"] = obj["first_name"].title()
        obj["last_name"] = obj["last_name"].title()
        return obj


class ThreadPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreadPost
        fields = "__all__"
