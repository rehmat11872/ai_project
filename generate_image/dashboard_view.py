from accounts.models import User
from .utils import generate_image
from django.shortcuts import render
from django.shortcuts import redirect
from .models import GeneratedImage, Like
from django.views.generic import ListView
from django.http import HttpResponseBadRequest



def generate_image_view(request):
    if request.method == 'POST':
        # Get the text input from the form
        text_input = request.POST.get('text_input')
        print(text_input, 'text______image')
        
        # Generate the image using the util function
        user = User.objects.get(email='raorehmat11@gmail.com')
        image_url = generate_image(text_input,  user=user)
        
        return render(request, 'generated_image.html', {'image_url': image_url})

    else:
        # Render the form template if no form has been submitted
        return render(request, 'text_input_form.html')


class ImageListView(ListView):
    model = GeneratedImage
    template_name = 'image_list.html'
    context_object_name = 'images'

    # def get_queryset(self):
    #     qs = super().get_queryset()
        # if self.request.user.is_authenticated:
        #     qs = qs.filter(user=self.request.user)
        # else:
        #     qs = qs.none()
        # return qs  



def save_like(request):
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        if not image_id:
            return HttpResponseBadRequest("Invalid request.")
        try:
            image = GeneratedImage.objects.get(id=image_id)
        except GeneratedImage.DoesNotExist:
            return HttpResponseBadRequest("Image not found.")
        user = User.objects.get(email='raorehmat11@gmail.com')
        like, created = Like.objects.get_or_create(user=user, image=image)
        if not created:
            # The like already exists
            pass
        return redirect('show_images')
    else:
        return HttpResponseBadRequest("Invalid request method.")


  