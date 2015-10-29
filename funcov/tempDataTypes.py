##############################################################################################################
# AHB
##############################################################################################################
ahbParameters = [
                         { 'enable' : True,
                           'name'   : 'tValid',
                           'select' : None,
                         },
                ]

ahbCovergroups = [
                   {
                     'enable'      : True,
                     'name'        : 'ActiveDataCycle',
                     'desc'        : 'Capture an active data cycle where tReady and tValid are asserted',
                     'type'        : 'value',
                     'signal'      : 'activeDataCycle',
                     'sensitivityLabel' : 'Positive clock edge',
                   },
                 ]

##############################################################################################################
# APB
##############################################################################################################
apbParameters = [
                  { 'enable'  : True,
                    'name'    : 'pAddr',
                    'select'  : '8',
                    'choices' : [(i, "%s" % i) for i in range(1,32)]
                  },
                  { 'enable'  : True,
                    'name'    : 'pSel',
                    'select'  : '1',
                    'choices' : [(i, "%s" % i) for i in range(1,32)]
                  },
                  { 'enable'  : True,
                    'name'    : 'pEnable',
                    'select'  : None,
                  },
                  { 'enable'  : True,
                    'name'    : 'pWrite',
                    'select'  : None,
                  },
                  { 'enable'  : True,
                    'name'    : 'pWdata',
                    'select'  : '8',
                    'choices' : [ ('8','8'), ('16','16'), ('32','32') ],
                  },
                  { 'enable'  : True,
                    'name'    : 'pReady',
                    'select'  : None,
                  },
                  { 'enable'  : True,
                    'name'    : 'pRdata',
                    'select'  : '8',
                    'choices' : [ ('8','8'), ('16','16'), ('32','32') ],
                  },
                ]

apbCovergroups = [
                   {
                     'enable'      : True,
                     'name'        : 'ActiveDataCycle',
                     'desc'        : 'Capture an active data cycle where tReady and tValid are asserted',
                     'type'        : 'value',
                     'signal'      : 'activeDataCycle',
                     'sensitivityLabel' : 'Positive clock edge',
                   },
                 ]

##############################################################################################################
# streaming axi4
##############################################################################################################
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
                            'signal'      : 'tLast',
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
