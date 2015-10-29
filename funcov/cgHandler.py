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
        bits1 = ['x'] * numBits
        bits0 = ['x'] * numBits
        bits1[numBits-i-1] = '1'
        bits0[numBits-i-1] = '0'
        cp += '      wildcard bins bit%s_is_0 = { %0d\'b%s };\n' % ( i, numBits, ''.join(bits0))
        cp += '      wildcard bins bit%s_is_1 = { %0d\'b%s };\n' % ( i, numBits, ''.join(bits1))
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

  module += portsAsString(pForm)

  with open("middle.sv", "r") as f:
    for line in f:
      module += line

  module += covergroupAsString(pForm, cgForm)

  with open("end.sv", "r") as f:
    for line in f:
      module += line
  return module

def portAsString(parameter):
  if parameter['select'].value() != None:
    return '  input [%s:0] %s' % (int(parameter['select'].value())-1, parameter['name'].value())
  else:
    return '  input %s' % parameter['name'].value()

def portsAsString(parameters):
  ports = ''
  for i in range(0,len(parameters)):
    if i < len(parameters)-1:
      ports += portAsString(parameters[i]) + ',\n'
    else:
      ports += portAsString(parameters[i]) + '\n'
  return ports
