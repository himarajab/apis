from faker import Faker
from django.urls import reverse
from rest_framework.test import APITestCase,APIClient


class TestSetup(APITestCase):

  def setUp(self) -> None:

      self.register_url = reverse('register')
      self.login_url = reverse('login')
      self.fake = Faker()
      self.fake_email = self.fake.email()

      self.user_data = {
        'email':self.fake_email,
        'username':self.fake_email.split('@')[0],
        'password':self.fake_email
      }

      return super().setUp()

  def tearDown(self) -> None:
      return super().tearDown()