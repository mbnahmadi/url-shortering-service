from django.shortcuts import render
from .models import ShortUrlModel
from .serializers import ShortUrlSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
# from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class CreateShortUrlView(generics.CreateAPIView):
    queryset = ShortUrlModel.objects.all()
    serializer_class = ShortUrlSerializer
