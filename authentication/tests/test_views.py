from ..models import User
from .test_setup import TestSetup

class TestViews(TestSetup):

  def test_register(self):
    response = self.client.post(self.register_url,self.user_data,format="json")
    self.assertEqual(response.data['email'],self.user_data['email'])
    self.assertEqual(response.data['username'],self.user_data['username'])
    self.assertEqual(response.status_code,201)

  def test_no_login_with_unverified_email(self):
    self.client.post(self.register_url,self.user_data,format="json")
    response = self.client.post(self.login_url,self.user_data,format="json")

    self.assertEqual(response.status_code,401)

  def test_login_after_verification(self):
    response = self.client.post(self.register_url,self.user_data,format="json")
    email = response.data['email']
    user = User.objects.get(email=email)
    user.is_verified = True
    user.save()
    resp = self.client.post(self.login_url,self.user_data,format="json")

    self.assertEqual(resp.status_code,200)