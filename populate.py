import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tools_agilesoc.settings')

import django
django.setup()

from funcov.models import Covergroup, Coverpoint
from funcov.tempDataTypes import axi4StreamCoverpoints, ahbCoverpoints, apbCoverpoints


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


def add_covergroup(name, type):
    cg = Covergroup.objects.get_or_create(name=name, type=type)[0]
    cg.name=name
    cg.type=type
    cg.save()
    return cg

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
