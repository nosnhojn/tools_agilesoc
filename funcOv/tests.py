from django.test import TestCase
from django.core.urlresolvers import reverse

import funcOv.views

class IndexViewTests(TestCase):

  def testIndexViewExists(self):
    response = self.client.get('/funcOv/')
    self.assertEqual(response.status_code, 200)

# def testIndexContextHasAuthenticationForm(self):
#   response = self.client.get(reverse('index'))
#   self.assertTrue(response.context['authForm'])
#
# def testIndexContextHasRegistrationtionForm(self):
#   response = self.client.get(reverse('index'))
#   self.assertTrue(response.context['regForm'])


class authenticationTests(TestCase):
  uname = 'uname'
  passwd = 'passwd'

  def createUser(self):
    up = UserProfile()
    up.user = User.objects.create_user(self.uname, 'email', self.passwd)
    up.save()

  def testLoginViewExists(self):
    response = self.client.get(reverse('auth_login'))
    self.assertEqual(response.status_code, 200)

  def testLoginRedirect(self):
    self.createUser()
    response = self.client.post('/accounts/login/', {'username':self.uname, 'password':self.passwd})
    self.assertRedirects(response, '/funcOv/')

  def testBadLoginRedirect(self):
    response = self.client.post('/accounts/login/', {'username':'dad', 'password':self.passwd})
    self.assertEquals(response.status_code, 200)


class registrationTests(TestCase):
  def testRegistrationViewExists(self):
    response = self.client.get(reverse('registration_register'))
    self.assertEqual(response.status_code, 200)

  def testRegisterRedirect(self):
    response = self.client.post('/accounts/register/', {'username':'name', 'email':'name@domain.com', 'password1':'pass', 'password2':'pass'})
    self.assertRedirects(response, '/funcOv/')


from django.contrib.auth.models import User
from funcOv.models import UserProfile
class userProfileTests(TestCase):
  def testCreateNewUserProfile(self):
    up = UserProfile()
    up.user = User.objects.create_user('uname', 'email', 'password')
    up.save()
    self.assertEqual(len(UserProfile.objects.all()), 1)
