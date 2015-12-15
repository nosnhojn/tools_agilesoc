from django.test import TestCase
from unittest.mock import patch
from django.core.urlresolvers import reverse
from registration.forms import RegistrationForm
from django.http import HttpRequest
from django.http import HttpResponse

import funcov.views
from funcov.cgHandler import covergroupAsString, coverpointAsString, portAsString, portsAsString
from funcov.forms import ParameterForm, CoverpointForm
from django.forms.formsets import formset_factory

from django.contrib.auth.models import User
from funcov.models import UserProfile, Coverpoint, Covergroup, ParameterChoice, Parameter

import populate

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
    populate.populate()
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
  def testRendersStreamAxi4(self, mock_render):
    self.client.get(reverse('editor'), { 'type':'axi4stream' })
    args, kwargs = mock_render.call_args
    self.assertEqual(args[1], 'funcov/editor.html')

  @patch('funcov.views.parameterFormSet')
  @patch('funcov.views.coverpointFormSet')
  def testAxi4StreamContext(self, mock_coverpointFormSet, mock_parameterFormSet):
    response = self.client.get(reverse('editor'), { 'type':'axi4stream' })
    cps = Coverpoint.objects.filter(covergroup = 'axi4stream')
    ps = Parameter.objects.filter(covergroup = 'axi4stream')

    self.assertEqual(response.context['name'], 'Streaming AXI-4')
    self.assertEqual(response.context['type'], 'axi4stream')
    args, kwargs = mock_parameterFormSet.call_args
    mismatches = [t for t in kwargs['init'] if t not in ps.values()]
    self.assertEqual(len(mismatches), 0);
    args, kwargs = mock_coverpointFormSet.call_args
    mismatches = [t for t in kwargs['init'] if t not in cps.values()]
    self.assertEqual(len(mismatches), 0);

  @patch('funcov.views.render', return_value=HttpResponse())
  def validatedPostToMyCovergroup(self, mock_render):
    data = {
        u'parameters-INITIAL_FORMS': [u'1'],
        u'parameters-TOTAL_FORMS': [u'0'],

        u'covergroups-INITIAL_FORMS': [u'1'],
        u'covergroups-TOTAL_FORMS': [u'0'],

        u'type': [u'axi4stream'],
        u'kind': [u'result'],
    }
    response = self.client.post(reverse('editor'), data)
 
    args, kwargs = mock_render.call_args
    self.assertEqual(args[1], 'funcov/myCovergroup.html')

  def testAxi4StreamParams(self):
    response = self.client.get(reverse('editor'), { 'type':'axi4stream' })
    parameters = response.context['parameters']
    self.assertTrue(len(parameters) > 0)
    for p in parameters:
      self.assertTrue(p.initial['enable'])
      self.assertTrue(p.initial['name'] != None)
      #if p['select'] != None:
      #  self.assertTrue(len(p['select']) > 0)
 
  def testAxi4StreamCovergroups(self):
    response = self.client.get(reverse('editor'), { 'type':'axi4stream' })
    coverpoints = response.context['coverpoints']
    self.assertTrue(len(coverpoints) > 0)
    for c in coverpoints:
      self.assertTrue(c.initial['enable'])
      self.assertTrue(c.initial['name'] != None)
      self.assertTrue(c.initial['desc'] != None)
      self.assertTrue(c.initial['type'] != None)
      self.assertTrue(c.initial['expr'] != None)
      self.assertTrue(c.initial['sensitivityLabel'] != None)
      self.assertTrue(c.initial['sensitivity'] != None)
    


class dbInteractionTests(TestCase):
  def setUp(self):
    cp = Coverpoint()
    cp.enable = True
    cp.name = 'n'
    cp.desc = 'a d'
    cp.type = 't'
    cp.expr = 'e'
    cp.sensitivityLabel = 'sL'
    cp.covergroup = 'c'
    cp.owner = 'o'
    cp.save()

    cg = Covergroup()
    cg.name = 'n'
    cg.type = 't'
    cg.save()

  def testCreateNewUserProfile(self):
    up = UserProfile()
    up.user = User.objects.create_user('uname', 'email', 'password')
    up.save()
    self.assertEqual(len(UserProfile.objects.all()), 1)
 
  def testCreateNewCoverpoint(self):
    self.assertEqual(len(Coverpoint.objects.all()), 1)
    qs = Coverpoint.objects.filter(
                                   enable = True
                          ).filter(
                                   name = 'n'
                          ).filter(
                                   desc = 'a d'
                          ).filter(
                                   type = 't'
                          ).filter(
                                   expr = 'e'
                          ).filter(
                                   sensitivityLabel = 'sL'
                          ).filter(
                                   covergroup = 'c'
                          ).filter(
                                   owner = 'o'
                          )
    self.assertEqual(len(qs), 1)

  def testCreateNewCoverpoint(self):
    self.assertEqual(len(Covergroup.objects.all()), 1)
    qs = Covergroup.objects.filter(name = 'n').filter(type = 't')
    self.assertEqual(len(qs), 1)


from populate import add_parameter
class coverageTemplateTests(TestCase):
  def setUp(self):
    self.pForm = ParameterForm()
    self.cgForm = CoverpointForm()

  def testDisabledCoverpointIsNullString(self):
    self.cgForm = CoverpointForm(initial={
                                           'enable':False,
                                         })
    self.assertTrue(coverpointAsString(self.pForm, self.cgForm) == "")

  def testEnabledCoverpointIsString(self):
    self.assertTrue(coverpointAsString(self.pForm, self.cgForm) != "")

  def testCoverpointValueInsensitive(self):
    self.cgForm = CoverpointForm(initial={
                                           'name':'theName',
                                           'type':'value',
                                           'expr':'theSignal',
                                         })
    self.assertEquals(coverpointAsString(self.pForm, self.cgForm), "    theName : coverpoint theSignal;\n")

  def testCoverpointValueSensitive(self):
    self.cgForm = CoverpointForm(initial={
                                           'name':'aName',
                                           'type':'value',
                                           'expr':'aSignal',
                                           'sensitivity':'someSignal',
                                         })
    self.assertEquals(coverpointAsString(self.pForm, self.cgForm), "    aName : coverpoint aSignal iff (someSignal);\n")

  def testCoverpointToggle1BitInsensitive(self):
    self.cgForm = CoverpointForm(initial={
                                           'name':'aName',
                                           'type':'toggle',
                                           'expr':'aSignal',
                                         })
    cp  = '    aName : coverpoint aSignal\n'
    cp += '    {\n'
    cp += '      wildcard bins bit0_is_0 = { 1\'b0 };\n'
    cp += '      wildcard bins bit0_is_1 = { 1\'b1 };\n'
    cp += '    }\n'
    self.assertEquals(coverpointAsString(self.pForm, self.cgForm), cp)

  def testCoverpointToggleNBitInsensitive(self):
    add_parameter(name = 'aSignal', enable = True, select = '7', choices = [ '7' ], owner = 'blah', covergroup = 'blah')
    self.pForm = ParameterForm(initial={
                                         'name':'aSignal',
                                       })
    qs = ParameterChoice.objects.filter(param='aSignal')
    self.pForm.fields['select'].queryset = qs
    self.pForm.fields['select'].initial = qs[0]

    self.cgForm = CoverpointForm(initial={
                                           'name':'aName',
                                           'type':'toggle',
                                           'expr':'aSignal',
                                         })
    cp  = '    aName : coverpoint aSignal\n'
    cp += '    {\n'
    cp += '      wildcard bins bit0_is_0 = { 7\'bxxxxxx0 };\n'
    cp += '      wildcard bins bit0_is_1 = { 7\'bxxxxxx1 };\n'
    cp += '      wildcard bins bit1_is_0 = { 7\'bxxxxx0x };\n'
    cp += '      wildcard bins bit1_is_1 = { 7\'bxxxxx1x };\n'
    cp += '      wildcard bins bit2_is_0 = { 7\'bxxxx0xx };\n'
    cp += '      wildcard bins bit2_is_1 = { 7\'bxxxx1xx };\n'
    cp += '      wildcard bins bit3_is_0 = { 7\'bxxx0xxx };\n'
    cp += '      wildcard bins bit3_is_1 = { 7\'bxxx1xxx };\n'
    cp += '      wildcard bins bit4_is_0 = { 7\'bxx0xxxx };\n'
    cp += '      wildcard bins bit4_is_1 = { 7\'bxx1xxxx };\n'
    cp += '      wildcard bins bit5_is_0 = { 7\'bx0xxxxx };\n'
    cp += '      wildcard bins bit5_is_1 = { 7\'bx1xxxxx };\n'
    cp += '      wildcard bins bit6_is_0 = { 7\'b0xxxxxx };\n'
    cp += '      wildcard bins bit6_is_1 = { 7\'b1xxxxxx };\n'
    cp += '    }\n'
    self.assertEquals(coverpointAsString(self.pForm, self.cgForm), cp)

  def testCoverpointToggle1BitSensitive(self):
    self.cgForm = CoverpointForm(initial={
                                           'name':'aName',
                                           'type':'toggle',
                                           'expr':'aSignal',
                                           'sensitivity':'bucko',
                                         })
    cp  = '    aName : coverpoint aSignal iff (bucko)\n'
    cp += '    {\n'
    cp += '      wildcard bins bit0_is_0 = { 1\'b0 };\n'
    cp += '      wildcard bins bit0_is_1 = { 1\'b1 };\n'
    cp += '    }\n'
    self.assertEquals(coverpointAsString(self.pForm, self.cgForm), cp)

  def testCovergroupTemplate(self):
    _2coverpoints = [
                      {
                        'name'        : 'ActiveDataCycle',
                        'type'        : 'value',
                        'expr'      : 'signal1',
                        'sensitivityLabel' : 'dud',
                      },
                      {
                        'name'        : 'tDataToggle',
                        'type'        : 'toggle',
                        'expr'      : 'signal2',
                        'sensitivityLabel' : 'dud',
                        'sensitivity' : 'activeDataCycle',
                      },
                    ]
    cgFormSet = formset_factory(CoverpointForm, extra=0)
    cgForm = cgFormSet(initial=_2coverpoints)

    add_parameter(name = 'signal2', enable = True, select = '2', choices = [ '2' ], owner = 'blah', covergroup = 'blah')
    _2parameters = [
                     {
                       'name'   : 'signal2',
                     },
                     {
                       'name'   : 'signal1',
                     },
                   ]
    pFormSet = formset_factory(ParameterForm, extra=0)
    pForm = pFormSet(initial=_2parameters)
    for form in pForm:
      if form.initial['name'] == 'signal2':
        qs = ParameterChoice.objects.filter(param='signal2')
        form.fields['select'].queryset = qs
        form.fields['select'].initial = qs[0]

    cp = ''
    cp += '    ActiveDataCycle : coverpoint signal1;\n'
    cp += '    tDataToggle : coverpoint signal2 iff (activeDataCycle)\n'
    cp += '    {\n'
    cp += '      wildcard bins bit0_is_0 = { 2\'bx0 };\n'
    cp += '      wildcard bins bit0_is_1 = { 2\'bx1 };\n'
    cp += '      wildcard bins bit1_is_0 = { 2\'b0x };\n'
    cp += '      wildcard bins bit1_is_1 = { 2\'b1x };\n'
    cp += '    }\n'
    self.assertEquals(covergroupAsString(pForm, cgForm), cp)

  def test1BitParameter(self):
    self.pForm = ParameterForm(initial={
                                         'name':'port',
                                         'select':None,
                                       })
    self.assertEquals(portAsString(self.pForm), '  input port')

  def testNBitParameter(self):
    add_parameter(name = 'port', enable = True, select = '41', choices = [ '41' ], owner = 'blah', covergroup = 'blah')
    self.pForm = ParameterForm(initial={
                                         'name':'port',
                                       })
    qs = ParameterChoice.objects.filter(param='port')
    self.pForm.fields['select'].queryset = qs
    self.pForm.fields['select'].initial = qs[0]
    self.assertEquals(portAsString(self.pForm), '  input [40:0] port')

  def testPortsAsString(self):
    add_parameter(name = 'signal2', enable = True, select = '2', choices = [ '2' ], owner = 'blah', covergroup = 'blah')
    _2parameters = [
                     {
                       'name'   : 'signal2',
                     },
                     {
                       'name'   : 'signal1',
                     },
                   ]
    pFormSet = formset_factory(ParameterForm, extra=0)
    pForm = pFormSet(initial=_2parameters)
    for form in pForm:
      if form.initial['name'] == 'signal2':
        qs = ParameterChoice.objects.filter(param='signal2')
        form.fields['select'].queryset = qs
        form.fields['select'].initial = qs[0]
    self.assertEquals(portsAsString(pForm), '  input [1:0] signal2,\n  input signal1\n')
