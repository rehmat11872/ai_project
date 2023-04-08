from django.shortcuts import render
from .utils import generate_image
from rest_framework import generics
from accounts.models import User
from rest_framework.permissions import IsAuthenticated
from .models import GeneratedImage, Like
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import GalleryImageSerializer, LikeSerializer
from django.views import View
from django.http import JsonResponse

class GenerateImageView(View):
    def post(self, request, *args, **kwargs):
        # Get the text input from the form
        text_input = request.POST.get('text_input')
        print(text_input, 'text______image')
        
        # Generate the image using the util function
        user = User.objects.get(email='raorehmat11@gmail.com')
        image_url = generate_image(text_input, user=user)

        # Return a JSON response with the image URL
        response_data = {'image_url': image_url}
        return JsonResponse(response_data)



class GalleryImageListView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = GeneratedImage.objects.all()
    serializer_class = GalleryImageSerializer

    # def get_queryset(self):
    #     user = self.request.user
    #     return GeneratedImage.objects.filter(user=user)    


class LikeImageView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    
    def post(self, request, *args, **kwargs):
        image = get_object_or_404(GeneratedImage, id=self.kwargs['pk'])
        user = request.user
        
        # Check if the user has already liked the image
        if Like.objects.filter(user=user, image=image).exists():
            return Response({'error': 'You have already liked this image.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Add a new like to the image
        like = Like.objects.create(user=user, image=image)
        like.save()
        
        return Response({'success': 'Image liked successfully.'}, status=status.HTTP_201_CREATED)
    

class DisplayLikeImageView(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
