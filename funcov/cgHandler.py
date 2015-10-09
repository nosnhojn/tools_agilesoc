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
                           'choices'  : [ ('8','8'), (2,'16'), (3,'32'), (4,'64'), (5,'128'), (6,'256') ],
                         },
                         { 'enable' : True,
                           'name'   : 'tStrb',
                           'select' : 1,
                           'choices' : [ (1,'1'), (2,'2'), (3,'4'), (4,'8'), (5,'16'), (6,'32')],
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
                            'name'        : 'activeDataCycle',
                            'desc'        : 'Capture an active data cycle where tReady and tValid are asserted',
                            'sensitivity' : 'Positive clock edge',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tDataToggle',
                            'desc'        : 'Toggle coverage of the tData bus',
                            'sensitivity' : 'activeDataCycle',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tStrbValues',
                            'desc'        : 'Value coverage of the tStrb bus',
                            'sensitivity' : 'activeDataCycle',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tKeepValues',
                            'desc'        : 'Value coverage of the tKeep bus',
                            'sensitivity' : 'activeDataCycle',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tLastToggle',
                            'desc'        : 'Toggle coverage of tLast',
                            'sensitivity' : 'activeDataCycle',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tIdValues',
                            'desc'        : 'Value coverage of the tId bus',
                            'sensitivity' : 'activeDataCycle',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tDestValues',
                            'desc'        : 'Value coverage of the tDest bus',
                            'sensitivity' : 'activeDataCycle',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tUserValues',
                            'desc'        : 'Value coverage of the tUser bus',
                            'sensitivity' : 'activeDataCycle',
                          },
                        ]

axi4StreamHeader = {
                     'name' : "Streaming AXI-4",
                     'type' : "axi4stream",
                   }

def covergroupAsString(parameters, covergroups):
  covergroup = ""
  with open("group.sv", "r") as f:
    for line in f:
      covergroup += line
  return covergroup
