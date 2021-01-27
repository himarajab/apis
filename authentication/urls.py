from .views import RegisterView,EmailVerify,LoginAPIView
from django.urls import path

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginAPIView.as_view(),name='login'),
    path('email_verify/',EmailVerify.as_view(),name='email-verify'),
]