from django.urls import path, include
from .views import UserRegistrationView,  CustomTokenObtainPairView


urlpatterns = [
    #resgistration
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    #login
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),   
]
