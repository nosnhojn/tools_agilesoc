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
                           'select' : '1',
                           'choices'  : [ (1,'8'), (2,'16'), (3,'32'), (4,'64'), (5,'128'), (6,'256') ],
                         },
                         { 'enable' : True,
                           'name'   : 'tStrb',
                           'select' : '1',
                           'choices' : [ (1,'1'), (2,'2'), (3,'4'), (4,'8'), (5,'16'), (6,'32')],
                         },
                         { 'enable' : True,
                           'name'   : 'tLast',
                           'select' : None,
                         },
                         { 'enable' : True,
                           'name'   : 'tKeep',
                           'select' : '4',
                           'choices' : [(i, "%s" % i) for i in range(1,16)]
                         },
                         { 'enable' : True,
                           'name'   : 'tId',
                           'select' : '4',
                           'choices' : [(i, "%s" % i) for i in range(1,16)]
                         },
                         { 'enable' : True,
                           'name'   : 'tDest',
                           'select' : '4',
                           'choices' : [(i, "%s" % i) for i in range(1,16)]
                         },
                         { 'enable' : True,
                           'name'   : 'tUser',
                           'select' : '4',
                           'choices' : [(i, "%s" % i) for i in range(1,16)]
                         },
                       ]
axi4StreamContext = {
                     'name' : "Streaming AXI-4",
                     'type' : "axi4stream",
                     'covergroups' :
                                     [
                                       {
                                         'name'        : 'activeDataCycle',
                                         'enabled'     : True,
                                         'desc'        : "Capture an active data cycle where tReady and tValid are asserted",
                                         'sensitivity' : "Positive clock edge",
                                       },
                                       {
                                         'name'        : 'tDataToggle',
                                         'enabled'     : True,
                                         'desc'        : "Toggle coverage of the tData bus",
                                         'sensitivity' : "activeDataCycle",
                                       },
                                     ],
                     'parameters' : 
                                    [
                                      {
                                        'name'    : 'tValid',
                                        'select' : None,
                                      },
                                      {
                                        'name'    : 'tReady',
                                        'select' : None,
                                      },
                                      {
                                        'name'    : 'tData',
                                        'select' : '8',
                                        'values'  : [ 8, 16, 32, 64, 128, 256 ],
                                      },
                                      {
                                        'name'    : 'tStrb',
                                        'select' : '1',
                                        'values'  : [ 1, 2, 4, 8, 16, 32 ],
                                      },
                                      {
                                        'name'    : 'tLast',
                                        'select' : None,
                                      },
                                      {
                                        'name'    : 'tKeep',
                                        'select' : '4',
                                        'values'  : range(1,16) 
                                      },
                                      {
                                        'name'    : 'tId',
                                        'select' : '4',
                                        'values'  : range(1,16) 
                                      },
                                      {
                                        'name'    : 'tDest',
                                        'select' : '4',
                                        'values'  : range(1,16) 
                                      },
                                      {
                                        'name'    : 'tUser',
                                        'select' : '4',
                                        'values'  : range(1,16) 
                                      },
                                    ],
             }       
