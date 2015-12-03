from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
  # This line is required. Links UserProfile to a User model instance.
  user = models.OneToOneField(User)

  # Override the __unicode__() method to return out something meaningful!
  def __unicode__(self):
    return self.user.username


class ParameterChoice(models.Model):
  paramID = models.CharField(max_length=128, default = '')
  choice = models.CharField(max_length=128, default = '')

  def __unicode__(self):
    return self.paramID


class Coverpoint(models.Model):
  name = models.CharField(max_length=128, default = '')
  enable = models.BooleanField(default=True, blank=True)
  name = models.CharField(max_length=128, default = '')
  desc = models.CharField(max_length=128, default = '')
  type = models.CharField(max_length=128, default = '')
  expr = models.CharField(max_length=128, default = '')
  sensitivity = models.CharField(max_length=128, default = '', blank=True)
  sensitivityLabel = models.CharField(max_length=128, default = '')
  covergroup = models.CharField(max_length=128, default = '')
  owner = models.CharField(max_length=128, default = '')

  def __unicode__(self):
    return self.name


class Parameter(models.Model):
  paramID = models.AutoField(primary_key=True)
  enable = models.BooleanField(default=True)
  name = models.CharField(max_length=128, default='')
  owner = models.CharField(max_length=128, default = '')
  covergroup = models.CharField(max_length=128, default = '')
  select = models.ForeignKey(ParameterChoice, blank=True, null=True)

  def __unicode__(self):
    return self.name


class Covergroup(models.Model):
  name = models.CharField(max_length=128, default = '')
  type = models.CharField(max_length=128, default = '')

  def __unicode__(self):
    return self.name
