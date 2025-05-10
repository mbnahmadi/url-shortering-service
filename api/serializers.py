from rest_framework import serializers
from .models import ShortUrlModel


class ShortUrlSerializer(serializers.ModelSerializer):
    # access_count = serializers.IntegerField(read_only=True)
    # created_at = serializers.DateTimeField(read_only=True)
    # updated_at = serializers.DateTimeField(read_only=True)
    # shortcode = serializers.DateTimeField(read_only=True)
    class Meta:
        model = ShortUrlModel
        fields = ('id', 'url', 'shortcode', 'created_at', 'updated_at')
        read_only_fields = ('id', 'shortcode', 'created_at', 'updated_at')


class ShortUrlStatusSerializer(serializers.ModelSerializer):
    # access_count = serializers.IntegerField(read_only=True)
    # created_at = serializers.DateTimeField(read_only=True)
    # updated_at = serializers.DateTimeField(read_only=True)
    # shortcode = serializers.DateTimeField(read_only=True)
    class Meta:
        model = ShortUrlModel
        fields = ('id', 'url', 'shortcode', 'created_at', 'updated_at', 'access_count')
        read_only_fields = ('id', 'shortcode', 'created_at', 'updated_at', 'access_count')       
