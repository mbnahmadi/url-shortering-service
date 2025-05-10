from django.shortcuts import render
from .models import ShortUrlModel
from .serializers import ShortUrlSerializer, ShortUrlStatusSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

class CreateShortUrlView(generics.CreateAPIView):
    queryset = ShortUrlModel.objects.all()
    serializer_class = ShortUrlSerializer

# class CreateShortUrlView(APIView):
#     @swagger_auto_schema(request_body=ShortUrlSerializer)
#     def post(self, request):
#         serializer = ShortUrlSerializer(data=request.data)
#         if serializer.is_valid():
#             clean_data = serializer.save()
#             return Response({
#                 'id':clean_data.pk,
#                 'url': clean_data.url,
#                 'shortCode': clean_data.shortcode,
#                 'createdAt': clean_data.created_at,
#                 'updatedAt': clean_data.updated_at
#             }) 
#         return Response({'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)   


class RetreiveShortUrlView(APIView):
    # @swagger_auto_schema(
    #         manual_parameters=[
    #             openapi.Parameter('shortcode', openapi.IN_QUERY, description='Short Code', type=openapi.TYPE_STRING, required=True)
    #     ])
    def get(self, request, shortcode):
        # shortcode = request.query_params.get('shortcode')
        try:
            instance = ShortUrlModel.objects.get(shortcode=shortcode)
            serializer = ShortUrlSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ShortUrlModel.DoesNotExist:
            return Response({'error': 'shortcode not found'}, status=status.HTTP_404_NOT_FOUND)
        

class UpdateShortUrlView(APIView):
    @swagger_auto_schema(request_body=ShortUrlSerializer)
    def put(self, request, shortcode):
        instance = get_object_or_404(ShortUrlModel, shortcode=shortcode)
        serializer = ShortUrlSerializer(data=request.data, instance=instance, partial=True)  #partial=True برای بروزرسانی جزئی
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DeleteShortUrlView(APIView):
    def delete(self, request, shortcode):
        instance = get_object_or_404(ShortUrlModel, shortcode=shortcode)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ShortUrlRedirectView(APIView):
    def get(self, request, shortcode, *args, **kwargs):
        instance = get_object_or_404(ShortUrlModel, shortcode=shortcode)
        instance.access_count += 1  # افزایش تعداد بازدید
        instance.save()
        return redirect(instance.url)  # هدایت به URL اصلی

class GetshortUrlStatisticsView(APIView):
    def get(self, request, shortcode):
        instance = get_object_or_404(ShortUrlModel, shortcode=shortcode)
        serializer = ShortUrlStatusSerializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
