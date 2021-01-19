from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from .utils import Util
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.shortcuts import render
from rest_framework import generics, status


class RegisterView(generics.GenericAPIView):

  serializer_class = RegisterSerializer
  def post(self,request):
    user = request.data
    serializer = self.serializer_class(data=user)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    user_data = serializer.data

    user = User.objects.get(email=user_data['email'])
    token = RefreshToken.for_user(user).access_token
    current_site = get_current_site(request).domain
    relative_link=reverse('email-verify')
    abs_url = 'http://'+current_site+relative_link+"?token="+str(token)
    email_body ='hi' +user.username+'click the link below to verify \n'+abs_url
    data = {'body':email_body,'to_email':user.email,'subject':'verify your email'}
    Util.send_email(data)
    return Response(user_data,status=status.HTTP_201_CREATED)


class EmailVerify(generics.GenericAPIView):
  def get(request):
    pass