import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tools_agilesoc.settings')

import django
django.setup()

from funcov.models import Covergroup, Coverpoint, Parameter, ParameterChoice
from funcov.tempDataTypes import axi4StreamCoverpoints, ahbCoverpoints, apbCoverpoints, axi4StreamParameters, ahbParameters, apbParameters


def populate():
  add_covergroup(name='Streaming AXI-4',
                 type='axi4stream')

  add_covergroup(name='AHB',
                 type='ahb')

  add_covergroup(name='APB',
                 type='apb')

  for cp in axi4StreamCoverpoints:
    add_coverpoint(name = cp['name'],
                   enable = cp['enable'],
                   desc = cp['desc'],
                   type = cp['type'],
                   expr = cp['expr'],
                   owner = 'nosnhojn',
                   sensitivity = cp['sensitivity'],
                   sensitivityLabel = cp['sensitivityLabel'],
                   covergroup = 'axi4stream')

  for cp in apbCoverpoints:
    add_coverpoint(name = cp['name'],
                   enable = cp['enable'],
                   desc = cp['desc'],
                   type = cp['type'],
                   expr = cp['expr'],
                   owner = 'nosnhojn',
                   sensitivity = cp['sensitivity'],
                   sensitivityLabel = cp['sensitivityLabel'],
                   covergroup = 'apb')

  for cp in ahbCoverpoints:
    add_coverpoint(name = cp['name'],
                   enable = cp['enable'],
                   desc = cp['desc'],
                   type = cp['type'],
                   expr = cp['expr'],
                   owner = 'nosnhojn',
                   sensitivity = cp['sensitivity'],
                   sensitivityLabel = cp['sensitivityLabel'],
                   covergroup = 'ahb')

  for p in axi4StreamParameters:
    add_parameter(name = p['name'],
                  enable = p['enable'],
                  select = p['select'],
                  choices = p['choices'],
                  owner = 'nosnhojn',
                  covergroup = 'axi4stream')

  for p in apbParameters:
    add_parameter(name = p['name'],
                  enable = p['enable'],
                  select = p['select'],
                  choices = p['choices'],
                  owner = 'nosnhojn',
                  covergroup = 'apb')

  for p in ahbParameters:
    add_parameter(name = p['name'],
                  enable = p['enable'],
                  select = p['select'],
                  choices = p['choices'],
                  owner = 'nosnhojn',
                  covergroup = 'ahb')


def add_covergroup(name, type):
    cg = Covergroup.objects.get_or_create(name=name, type=type)[0]
    cg.name=name
    cg.type=type
    cg.save()
    return cg


def add_parameter(name, enable, select, choices, owner, covergroup):
    p = Parameter.objects.get_or_create(name=name,
                                        enable=enable,
                                        #select=select,
                                        owner=owner,
                                        covergroup=covergroup)[0]
    p.name=name
    p.enable=enable
#   p.select=select
#   p.choices=choices
    p.owner=owner
    p.covergroup=covergroup
    p.save()

    for c in choices:
      pc = ParameterChoice.objects.get_or_create(paramID=p.paramID,
                                                 choice=c)[0]
      pc.paramID = p.paramID
      pc.choice = c
      pc.save()

    if p.select:
      p.select.queryset = ParameterChoice.objects.filter(paramID=p.paramID)
      p.save()

    return p

def add_coverpoint(name, enable, desc, type, expr, owner, sensitivity, sensitivityLabel, covergroup):
    cp = Coverpoint.objects.get_or_create(name=name,
                                          enable = enable,
                                          desc = desc,
                                          type = type,
                                          expr = expr,
                                          owner = owner,
                                          sensitivity = sensitivity,
                                          sensitivityLabel = sensitivityLabel,
                                          covergroup = covergroup)[0]
    cp.name = name
    cp.enable = enable
    cp.desc = desc
    cp.type = type
    cp.expr = expr
    cp.owner = owner
    cp.sensitivity = sensitivity
    cp.sensitivityLabel = sensitivityLabel
    cp.covergroup = covergroup
    cp.save()
    return cp

# Start execution here!
if __name__ == '__main__':
  populate()
