from django.test import TestCase
from django.core.urlresolvers import reverse

import funcOv.views

class IndexViewTests(TestCase):
  uname = 'uname'
  passwd = 'passwd'

  def createUser(self):
    up = UserProfile()
    up.user = User.objects.create_user(self.uname, 'email', self.passwd)
    up.save()

  def testIndexViewExists(self):
    response = self.client.get(reverse('index'))
    self.assertEqual(response.status_code, 200)

# def testIndexContextHasAuthenticationForm(self):
#   response = self.client.get(reverse('index'))
#   self.assertTrue(response.context['authForm'])
#
# def testIndexContextHasRegistrationtionForm(self):
#   response = self.client.get(reverse('index'))
#   self.assertTrue(response.context['regForm'])

# def testHuh(self):
#   self.createUser()
#   print(self.client.login(username=self.uname, password=self.passwd))


class authenticationTests(TestCase):
  def testLoginViewExists(self):
    response = self.client.get(reverse('auth_login'))
    self.assertEqual(response.status_code, 200)

  def testRegistrationViewExists(self):
    response = self.client.get(reverse('registration_register'))
    self.assertEqual(response.status_code, 200)


from django.contrib.auth.models import User
from funcOv.models import UserProfile
class userProfileTests(TestCase):
  def testCreateNewUserProfile(self):
    up = UserProfile()
    up.user = User.objects.create_user('uname', 'email', 'password')
    up.save()
    self.assertEqual(len(UserProfile.objects.all()), 1)
