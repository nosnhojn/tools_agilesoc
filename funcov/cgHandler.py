from funcov.models import ParameterChoice

def coverpointAsString(parameter, covergroup):
  cp = ''
  if covergroup['enable'].value() == True:
    cp += '    %s : coverpoint %s' % (covergroup['name'].value(), covergroup['expr'].value())
    if covergroup['sensitivity'].value() != '' and covergroup['sensitivity'].value() != None:
      cp += ' iff (%s)' % covergroup['sensitivity'].value()
    if covergroup['kind'].value() == 'value':
      cp += ';\n'
    elif covergroup['kind'].value() == 'toggle':
      numBits = 1
      if parameter['select'].value() != None:
        numBits = int(ParameterChoice.objects.filter(id=parameter['select'].value())[0].choice)
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
    if c['kind'].value() == 'toggle':
      index = next(i for (i, p) in enumerate(parameters) if p['name'].value() == c['expr'].value())
      cg += coverpointAsString(parameters[index], c)
    else:
      cg += coverpointAsString(None, c)

  return cg

def coverageModuleAsString(pForm, cgForm, begin, middle, end):
  module = ""
  module += begin

  module += portsAsString(pForm)

  module += middle

  module += covergroupAsString(pForm, cgForm)

  module += end

  return module

def portAsString(parameter):
  if parameter['select'].value() != None:
    width = ParameterChoice.objects.filter(id=parameter['select'].value())[0].choice
    return '  input [%s:0] %s' % (int(width)-1, parameter['name'].value())
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
