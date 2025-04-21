from rest_framework import serializers
from .models import ShortUrlModel


class ShortUrlSerializer(serializers.ModelSerializer):
    access_count = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = ShortUrlModel
        fields = ('url', 'shortcode', 'access_count', 'created_at', 'updated_at')
