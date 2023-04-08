from django.db import models
from accounts.models import User

# Create your models here.
class GeneratedImage(models.Model):
    image = models.ImageField(upload_to='Images/generated_images')
    text_input = models.CharField(max_length=255,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='generated_images')


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    image = models.ForeignKey(GeneratedImage, on_delete=models.CASCADE, related_name='likes')