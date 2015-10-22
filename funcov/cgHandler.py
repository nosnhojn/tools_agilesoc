axi4StreamParameters = [
                         { 'enable' : True,
                           'name'   : 'tValid',
                           'select' : None,
                         },
                         { 'enable' : True,
                           'name'   : 'tReady',
                           'select' : None,
                         },
                         { 'enable' : True,
                           'name'   : 'tData',
                           'select' : '8',
                           'choices'  : [ ('8','8'), ('16','16'), ('32','32'), ('64','64'), ('128','128'), ('256','256') ],
                         },
                         { 'enable' : True,
                           'name'   : 'tStrb',
                           'select' : 1,
                           'choices' : [ (1,1), (2,2), (4,4), (8,8), (16,16), (32,32)],
                         },
                         { 'enable' : True,
                           'name'   : 'tLast',
                           'select' : None,
                         },
                         { 'enable' : True,
                           'name'   : 'tKeep',
                           'select' : 4,
                           'choices' : [(i, "%s" % i) for i in range(1,16)]
                         },
                         { 'enable' : True,
                           'name'   : 'tId',
                           'select' : 4,
                           'choices' : [(i, "%s" % i) for i in range(1,16)]
                         },
                         { 'enable' : True,
                           'name'   : 'tDest',
                           'select' : 4,
                           'choices' : [(i, "%s" % i) for i in range(1,16)]
                         },
                         { 'enable' : True,
                           'name'   : 'tUser',
                           'select' : 4,
                           'choices' : [(i, "%s" % i) for i in range(1,16)]
                         },
                       ]

axi4StreamCovergroups = [
                          {
                            'enable'      : True,
                            'name'        : 'ActiveDataCycle',
                            'desc'        : 'Capture an active data cycle where tReady and tValid are asserted',
                            'type'        : 'value',
                            'signal'      : 'activeDataCycle',
                            'sensitivityLabel' : 'Positive clock edge',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tDataToggle',
                            'desc'        : 'Toggle coverage of the tData bus',
                            'type'        : 'toggle',
                            'signal'      : 'tData',
                            'sensitivityLabel' : 'activeDataCycle',
                            'sensitivity' : 'activeDataCycle',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tStrbValues',
                            'desc'        : 'Value coverage of the tStrb bus',
                            'type'        : 'value',
                            'signal'      : 'tStrb',
                            'sensitivityLabel' : 'activeDataCycle',
                            'sensitivity' : 'activeDataCycle',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tKeepValues',
                            'desc'        : 'Value coverage of the tKeep bus',
                            'type'        : 'value',
                            'signal'      : 'tKeep',
                            'sensitivityLabel' : 'activeDataCycle',
                            'sensitivity' : 'activeDataCycle',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tLastToggle',
                            'desc'        : 'Toggle coverage of tLast',
                            'type'        : 'value',
                            'signal'      : 'dLast',
                            'sensitivityLabel' : 'activeDataCycle',
                            'sensitivity' : 'activeDataCycle',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tIdValues',
                            'desc'        : 'Value coverage of the tId bus',
                            'type'        : 'value',
                            'signal'      : 'tId',
                            'sensitivityLabel' : 'activeDataCycle',
                            'sensitivity' : 'activeDataCycle',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tDestValues',
                            'desc'        : 'Value coverage of the tDest bus',
                            'type'        : 'value',
                            'signal'      : 'tDest',
                            'sensitivityLabel' : 'activeDataCycle',
                            'sensitivity' : 'activeDataCycle',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tUserValues',
                            'desc'        : 'Value coverage of the tUser bus',
                            'type'        : 'value',
                            'signal'      : 'tUser',
                            'sensitivityLabel' : 'activeDataCycle',
                            'sensitivity' : 'activeDataCycle',
                          },
                        ]

axi4StreamHeader = {
                     'name' : "Streaming AXI-4",
                     'type' : "axi4stream",
                   }

def coverpointAsString(parameter, covergroup):
  cp = ''
  if covergroup['enable'].value() == True:
    cp += '    %s : coverpoint %s' % (covergroup['name'].value(), covergroup['signal'].value())
    if covergroup['sensitivity'].value() != '' and covergroup['sensitivity'].value() != None:
      cp += ' iff (%s)' % covergroup['sensitivity'].value()
    if covergroup['type'].value() == 'value':
      cp += ';\n'
    elif covergroup['type'].value() == 'toggle':
      numBits = 1
      if parameter['select'].value() != None:
        numBits = int(parameter['select'].value())
      cp += '\n'
      cp += '    {\n'
      for i in range(0, numBits):
        cp += '      bins bit%s_is_0 = { 1\'b0 };\n' % i
        cp += '      bins bit%s_is_1 = { 1\'b1 };\n' % i
      cp += '    }\n'

  return cp

def covergroupAsString(parameters, covergroups):
  cg = ""
  for c in covergroups:
    if c['type'].value() == 'toggle':
      index = next(i for (i, p) in enumerate(parameters) if p['name'].value() == c['signal'].value())
      cg += coverpointAsString(parameters[index], c)
    else:
      cg += coverpointAsString(None, c)

  return cg

def coverageModuleAsString(pForm, cgForm):
  module = ""
  with open("begin.sv", "r") as f:
    for line in f:
      module += line

  module += covergroupAsString(pForm, cgForm)

  with open("end.sv", "r") as f:
    for line in f:
      module += line
  return module
