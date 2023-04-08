from rest_framework import serializers
from .models import GeneratedImage, Like

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneratedImage
        fields = ['image']
        
    def to_representation(self, instance):
        """
        Serialize image field to return url
        """
        ret = super().to_representation(instance)
        ret['image'] = self.context['request'].build_absolute_uri(ret['image'])
        return ret

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['image']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # data['image'] = self.context['request'].build_absolute_uri(data['image'])
        return data
