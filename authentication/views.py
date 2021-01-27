from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.conf import settings
import jwt
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from .utils import Util
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .serializers import RegisterSerializer,EmailVerificationSerializer,LoginSerializer
from django.shortcuts import render
from rest_framework import generics, serializers, status,views


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


class EmailVerify(views.APIView):
  serializer_class = EmailVerificationSerializer
  token_param_config = openapi.Parameter('token',in_=openapi.IN_QUERY,description='description',type=openapi.TYPE_STRING)
  

  @swagger_auto_schema(manual_parameters=[token_param_config])
  def get(self,request):
    token = request.GET.get('token')

    try:
      # we use the secret key to encode and decode the tokens
      payload = jwt.decode(token,settings.SECRET_KEY)
      user = User.objects.get(id=payload['user_id'])
      # avoid unneccessery write to the db
      if not user.is_verified:
        user.is_verified=True
        user.save()
      return Response({'email':'successfully activated'},status=status.HTTP_200_OK)

    except jwt.ExpiredSignatureError as identifier:
      return Response({'error':'activation link expired'},status=status.HTTP_400_BAD_REQUEST)

    except jwt.exceptions.DecodeError as identifier:
      return Response({'error':'invalid token'},status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self,request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)

    return Response(serializer.data,status = status.HTTP_200_OK)
