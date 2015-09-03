from django.test import TestCase
from django.core.urlresolvers import reverse
from registration.forms import RegistrationForm

import funcOv.views

class userTests(TestCase):
  uname = 'uname'
  passwd = 'passwd'
  email = 'email@domain.com'

  def createUser(self):
    up = UserProfile()
    up.user = User.objects.create_user(self.uname, self.email, self.passwd)
    up.save()

  def testIndexViewExists(self):
    response = self.client.get(reverse('index'))
    self.assertEqual(response.status_code, 200)

  def testNoUserIndex(self):
    response = self.client.get(reverse('index'))
    self.assertEquals(response.context['title'], 'FunkOv')
    self.assertEquals(response.context['h1'], 'FunkOv')
    self.assertEquals(response.context['h2'], 'Funktional Coverage Made Easy')
    self.assertEquals(response.context['h3'], 'Something catchy here that makes people want to register')
    self.assertEquals(response.context['buttons']['Register'], reverse('registration_register'))
    self.assertEquals(response.context['buttons']['Login'], reverse('auth_login'))

  def testUserIndex(self):
    self.createUser()
    self.client.login(username=self.uname, password=self.passwd)

    response = self.client.get(reverse('index'))
    self.assertEquals(response.context['title'], self.uname)
    self.assertEquals(response.context['h1'], 'FunkOv')
    self.assertEquals(response.context['h2'], 'Pick an interface to get started')
    self.assertEquals(response.context['h3'], '')
    self.assertEquals(response.context['buttons']['AHB'], reverse('index'))
    self.assertEquals(response.context['buttons']['APB'], reverse('index'))
    self.assertEquals(response.context['buttons']['AXI4-Stream'], reverse('index'))

  def testLoginViewExists(self):
    response = self.client.get(reverse('auth_login'))
    self.assertEqual(response.status_code, 200)

  def testLoginRedirect(self):
    self.createUser()
    response = self.client.post('/accounts/login/', {'username':self.uname, 'password':self.passwd})
    self.assertRedirects(response, reverse('index'))

  def testLogoutRedirect(self):
    response = self.client.post('/accounts/logout/')
    self.assertRedirects(response, reverse('index'))

  def testBadLoginRedirect(self):
    response = self.client.post('/accounts/login/', {'username':'dad', 'password':self.passwd})
    self.assertEquals(response.status_code, 200)

  def testRegistrationViewExists(self):
    response = self.client.get(reverse('registration_register'))
    self.assertEqual(response.status_code, 200)

  def testRegisterRedirect(self):
    response = self.client.post('/accounts/register/', {'username':'name', 'email':'name@domain.com', 'password1':'pass', 'password2':'pass'})
    self.assertRedirects(response, reverse('index'))

  def testRepeatRegistration(self):
    self.createUser()
    response = self.client.post('/accounts/register/', {'username':self.uname, 'email':'name@domain.com', 'password1':'pass', 'password2':'pass'})
    self.assertEqual(response.status_code, 200)

  def testRegistrationUnameError(self):
    response = self.client.post('/accounts/register/', {'username':' ', 'email':'name@domain.com', 'password1':'pass', 'password2':'pass'})
    self.assertFormError(response, 'form', 'username', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')

  def testRegistrationDuplicateUnameError(self):
    self.createUser()
    response = self.client.post('/accounts/register/', {'username':self.uname, 'email':'email', 'password1':'pass', 'password2':'pass'})
    self.assertFormError(response, 'form', 'username', 'A user with that username already exists.')


from django.contrib.auth.models import User
from funcOv.models import UserProfile
class userProfileTests(TestCase):
  def testCreateNewUserProfile(self):
    up = UserProfile()
    up.user = User.objects.create_user('uname', 'email', 'password')
    up.save()
    self.assertEqual(len(UserProfile.objects.all()), 1)
