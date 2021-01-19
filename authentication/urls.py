from .views import RegisterView,EmailVerify
from django.urls import path

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('email_verify/',EmailVerify.as_view(),name='email-verify'),
]