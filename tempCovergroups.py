axi4StreamParameters = [
                         { 'name'   : 'tValid',
                           'select' : None,
                         },
                         { 'name'   : 'tReady',
                           'select' : None,
                         },
                         { 'name'   : 'tData',
                           'select' : '8',
                           'values'  : [ 8, 16, 32, 64, 128, 256 ],
                         },
                         { 'name'   : 'tStrb',
                           'select' : '1',
                           'values' : [ 1, 2, 4, 8, 16, 32 ],
                         },
                         { 'name'   : 'tLast',
                           'select' : None,
                         },
                         { 'name'   : 'tKeep',
                           'select' : '4',
                           'values' : range(1,16) 
                         },
                         { 'name'   : 'tId',
                           'select' : '4',
                           'values' : range(1,16) 
                         },
                         { 'name'   : 'tDest',
                           'select' : '4',
                           'values' : range(1,16) 
                         },
                         { 'name'   : 'tUser',
                           'select' : '4',
                           'values' : range(1,16) 
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
