import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tools_agilesoc.settings')

import django
django.setup()

from funcov.models import Covergroup


def populate():
  add_covergroup(name='Streaming AXI-4',
                 type='axi4stream')

def add_covergroup(name, type):
    cg = Covergroup.objects.get_or_create(name=name, type=type)[0]
    cg.name=name
    cg.type=type
    cg.save()
    return cg

# Start execution here!
if __name__ == '__main__':
    populate()
