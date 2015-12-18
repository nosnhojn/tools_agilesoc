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
  param = models.CharField(max_length=50, default = '')
  choice = models.CharField(max_length=50, default = '')

  def __unicode__(self):
    return self.choice


class Coverpoint(models.Model):
  name = models.CharField(max_length=50, default = '')
  enable = models.BooleanField(default=True, blank=True)
  desc = models.CharField(max_length=200, default = '')
  kind = models.CharField(max_length=50, default = '')
  expr = models.CharField(max_length=50, default = '')
  sensitivity = models.CharField(max_length=50, default = '', blank=True)
  sensitivityLabel = models.CharField(max_length=50, default = '')
  covergroup = models.CharField(max_length=50, default = '')

  def __unicode__(self):
    return self.name


class Parameter(models.Model):
  name = models.CharField(max_length=50, default='')
  enable = models.BooleanField(default=True)
  covergroup = models.CharField(max_length=50, default = '')
  select = models.ForeignKey(ParameterChoice, blank=True, null=True)

  def __unicode__(self):
    return self.name


class Covergroup(models.Model):
  name = models.CharField(max_length=50, default = '')
  type = models.CharField(max_length=50, default = '')
  beginning = models.CharField(max_length=10000, default = '')
  middle = models.CharField(max_length=100, default = '')
  private = models.BooleanField(default=True, blank=True)
  owner = models.CharField(max_length=50, default = '')

  def __unicode__(self):
    return self.name
