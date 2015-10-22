from django.test import TestCase
from unittest.mock import patch
from django.core.urlresolvers import reverse
from registration.forms import RegistrationForm
from django.http import HttpRequest
from django.http import HttpResponse

import funcov.views
from funcov.cgHandler import coverpointAsString
from funcov.forms import ParameterForm, CovergroupForm

class userTests(TestCase):
  uname = 'uname'
  passwd = 'passwd'
  email = 'email@domain.com'

  def createUser(self):
    up = UserProfile()
    up.user = User.objects.create_user(self.uname, self.email, self.passwd)
    up.save()

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



class generalViewTests(TestCase):
  def testUrlTranslationViewExists(self):
    response = self.client.get('/FuNcOv/')
    self.assertEqual(response.status_code, 200)

  def testIndexViewExists(self):
    response = self.client.get(reverse('index'))
    self.assertEqual(response.status_code, 200)



class indexViewTests(TestCase):
  @patch('funcov.views.render') # mocked relative the to the module using it, not the definition
  def testIndexRendersIndexHtml(self, mock_render):
    request = HttpRequest()
    request.user = User.objects.create_user('uname', 'email', 'password')
    funcov.views.index(request)
    args, kwargs = mock_render.call_args
    self.assertEqual(args[0], request)
    self.assertEqual(args[1], 'funcov/index.html')

  def testLoginViewExists(self):
    response = self.client.get(reverse('auth_login'))
    self.assertEqual(response.status_code, 200)



class editorViewTests(TestCase):
  def setUp(self):
    up = UserProfile()
    up.user = User.objects.create_user('a', 'b', 'c')
    up.save()
    self.client.login(username='a', password='c')

  def testEditorRedirectsWithoutLogin(self):
    self.client.logout()
    response = self.client.get(reverse('editor'))
    self.assertEqual(response.status_code, 302)

  def testEditorRedirectForUndefinedType(self):
    response = self.client.get(reverse('editor'), { 'type':'bagels' })
    self.assertEqual(response.status_code, 302)

  @patch('funcov.views.HttpResponseRedirect', return_value=HttpResponse())
  def testEditorRedirectToIndex(self, mock_HttpResponseRedirect):
    self.client.get(reverse('editor'), { 'type':'bagels' })
    mock_HttpResponseRedirect.assert_called_with(reverse('index'))

  @patch('funcov.views.render', return_value=HttpResponse())
  def testRendersAhb(self, mock_render):
    self.client.get(reverse('editor'), { 'type':'ahb' })
    args, kwargs = mock_render.call_args
    self.assertEqual(args[1], 'funcov/editor.html')

  def testAhbContext(self):
    response = self.client.get(reverse('editor'), { 'type':'ahb' })
    self.assertEqual(response.context['name'], 'AHB')
    self.assertEqual(response.context['type'], 'ahb')
    self.assertTrue(len(response.context['covergroups']) > 0)

  @patch('funcov.views.render', return_value=HttpResponse())
  def testRendersApb(self, mock_render):
    self.client.get(reverse('editor'), { 'type':'apb' })
    args, kwargs = mock_render.call_args
    self.assertEqual(args[1], 'funcov/editor.html')

  def testApbContext(self):
    response = self.client.get(reverse('editor'), { 'type':'apb' })
    self.assertEqual(response.context['name'], 'APB')
    self.assertEqual(response.context['type'], 'apb')
    self.assertTrue(len(response.context['covergroups']) > 0)


class axi4StreamTests(TestCase):
  def setUp(self):
    up = UserProfile()
    up.user = User.objects.create_user('a', 'b', 'c')
    up.save()
    self.client.login(username='a', password='c')

  @patch('funcov.views.render', return_value=HttpResponse())
  def testRendersStreamAxi4(self, mock_render):
    self.client.get(reverse('editor'), { 'type':'axi4stream' })
    args, kwargs = mock_render.call_args
    self.assertEqual(args[1], 'funcov/editor.html')

  def testAxi4StreamContext(self):
    response = self.client.get(reverse('editor'), { 'type':'axi4stream' })
    self.assertEqual(response.context['name'], 'Streaming AXI-4')
    self.assertEqual(response.context['type'], 'axi4stream')
 
  def testAxi4StreamParams(self):
    response = self.client.get(reverse('editor'), { 'type':'axi4stream' })
    parameters = response.context['parameters']
    self.assertTrue(len(parameters) > 0)
    for p in parameters:
      self.assertTrue(p.fields['enable'])
      self.assertTrue(p.fields['name'])
      if p['select'] is not None:
        self.assertTrue(len(p['select']) > 0)
 
  def testAxi4StreamCovergroups(self):
    response = self.client.get(reverse('editor'), { 'type':'axi4stream' })
    covergroups = response.context['covergroups']
    self.assertTrue(len(covergroups) > 0)
    for c in covergroups:
      self.assertTrue(c.fields['enable'])
      self.assertTrue(c.fields['name'])
      self.assertTrue(c.fields['desc'])
      self.assertTrue(c.fields['type'])
      self.assertTrue(c.fields['signal'])
      self.assertTrue(c.fields['sensitivityLabel'])
      self.assertTrue(c.fields['sensitivity'])


from django.contrib.auth.models import User
from funcov.models import UserProfile
class dbInteractionTests(TestCase):
  def testCreateNewUserProfile(self):
    up = UserProfile()
    up.user = User.objects.create_user('uname', 'email', 'password')
    up.save()
    self.assertEqual(len(UserProfile.objects.all()), 1)

class coverageTemplateTests(TestCase):
  def setUp(self):
    self.pForm = ParameterForm()
    self.cgForm = CovergroupForm()

  def testDisabledCoverpointIsNullString(self):
    self.cgForm = CovergroupForm(initial={
                                           'enable':False,
                                         })
    self.assertTrue(coverpointAsString(self.pForm, self.cgForm) == "")

  def testEnabledCoverpointIsString(self):
    self.cgForm.enable = True
    self.assertTrue(coverpointAsString(self.pForm, self.cgForm) != "")

  def testEnabledCoverpointValueInsensitive(self):
    self.cgForm = CovergroupForm(initial={
                                           'name':'theName',
                                           'type':'value',
                                           'signal':'theSignal',
                                           'sensitivity':None,
                                         })
    self.assertEquals(coverpointAsString(self.pForm, self.cgForm), "  theName : coverpoint theSignal;")

  def testEnabledCoverpointValueSensitive(self):
    self.cgForm.enable = True
    self.cgForm.name = 'aName'
    self.cgForm.type = 'value'
    self.cgForm.signal = 'aSignal'
    self.cgForm.sensitivity = 'someSignal'
    self.assertEquals(coverpointAsString(self.pForm, self.cgForm), "  aName : coverpoint aSignal iff (someSignal);")
