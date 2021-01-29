from .views import RegisterView,EmailVerify,LoginAPIView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)



urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginAPIView.as_view(),name='login'),
    path('email_verify/',EmailVerify.as_view(),name='email-verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]