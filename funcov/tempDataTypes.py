##############################################################################################################
# AHB
##############################################################################################################
ahbParameters = [
                  { 'enable'  : True,
                    'name'    : 'hAddr',
                    'select'  : '8',
                    'choices' : [('%s' % i) for i in range(1,32)]
                  },
                  { 'enable'  : True,
                    'name'    : 'hTrans',
                    'select'  : '2',
                    'choices' : [ '2' ],
                  },
                  { 'enable'  : True,
                    'name'    : 'hWrite',
                    'select'  : None,
                    'choices' : '',
                  },
                  { 'enable'  : True,
                    'name'    : 'hSize',
                    'select'  : '3',
                    'choices' : [ '3' ],
                  },
                  { 'enable'  : True,
                    'name'    : 'hBurst',
                    'select'  : '3',
                    'choices' : [ '3' ],
                  },
                  { 'enable'  : True,
                    'name'    : 'hProt',
                    'select'  : '4',
                    'choices' : [ '4' ],
                  },
                  { 'enable'  : True,
                    'name'    : 'hWdata',
                    'select'  : '8',
                    'choices' : [ '8', '16', '32', '64', '128' ],
                  },
                  { 'enable'  : True,
                    'name'    : 'hSel',
                    'select'  : '1',
                    'choices' : [("%s" % i) for i in range(1,32)]
                  },
                  { 'enable'  : True,
                    'name'    : 'hRdata',
                    'select'  : '8',
                    'choices' : [ '8', '16', '32', '64', '128' ],
                  },
                  { 'enable'  : True,
                    'name'    : 'hReady',
                    'select'  : None,
                    'choices' : '',
                  },
                  { 'enable'  : True,
                    'name'    : 'hResp',
                    'select'  : '2',
                    'choices' : [ '2' ],
                  },
                ]

ahbCoverpoints = [
                   {
                     'enable'      : True,
                     'name'        : 'ActiveDataCycle',
                     'desc'        : 'Capture an active data cycle where hTrans != 0 and hReady is asserted',
                     'kind'        : 'value',
                     'expr'        : 'activeDataCycle',
                     'sensitivityLabel' : 'Negative clock edge',
                     'sensitivity' : '',
                   },
                   {
                     'enable'      : True,
                     'name'        : 'hAddrToggle',
                     'desc'        : 'Toggle coverage of the hAddr bus',
                     'kind'        : 'toggle',
                     'expr'        : 'hAddr',
                     'sensitivityLabel' : 'activeDataCycle',
                     'sensitivity' : 'activeDataCycle',
                   },
                   {
                     'enable'      : True,
                     'name'        : 'hTransValues',
                     'desc'        : 'Value coverage of the hTrans bus',
                     'kind'        : 'value',
                     'expr'        : 'hTrans',
                     'sensitivityLabel' : 'Negative clock edge',
                     'sensitivity' : '',
                   },
                   {
                     'enable'      : True,
                     'name'        : 'hWrite',
                     'desc'        : 'Toggle coverage of the hWrite bus',
                     'kind'        : 'toggle',
                     'expr'        : 'hWrite',
                     'sensitivityLabel' : 'activeDataCycle',
                     'sensitivity' : 'activeDataCycle',
                   },
                   {
                     'enable'      : True,
                     'name'        : 'hSizeValue',
                     'desc'        : 'Value coverage of the hSize bus',
                     'kind'        : 'value',
                     'expr'        : 'hSize',
                     'sensitivityLabel' : 'activeDataCycle',
                     'sensitivity' : 'activeDataCycle',
                   },
                   {
                     'enable'      : True,
                     'name'        : 'hBurstValue',
                     'desc'        : 'Value coverage of the hBurst bus',
                     'kind'        : 'value',
                     'expr'        : 'hBurst',
                     'sensitivityLabel' : 'activeDataCycle',
                     'sensitivity' : 'activeDataCycle',
                   },
                   {
                     'enable'      : True,
                     'name'        : 'hProtToggle',
                     'desc'        : 'Toggle coverage of the hProt bus',
                     'kind'        : 'toggle',
                     'expr'        : 'hProt',
                     'sensitivityLabel' : 'activeDataCycle',
                     'sensitivity' : 'activeDataCycle',
                   },
                   {
                     'enable'      : True,
                     'name'        : 'hWdataToggle',
                     'desc'        : 'Toggle coverage of the hWdata bus',
                     'kind'        : 'toggle',
                     'expr'        : 'hWdata',
                     'sensitivityLabel' : 'activeDataCycle',
                     'sensitivity' : 'activeDataCycle',
                   },
                   {
                     'enable'      : True,
                     'name'        : 'hSelToggle',
                     'desc'        : 'Toggle coverage of the hSel bus',
                     'kind'        : 'toggle',
                     'expr'        : 'hSel',
                     'sensitivityLabel' : 'activeDataCycle',
                     'sensitivity' : 'activeDataCycle',
                   },
                   {
                     'enable'      : True,
                     'name'        : 'hRdataToggle',
                     'desc'        : 'Toggle coverage of the hRdata bus',
                     'kind'        : 'toggle',
                     'expr'        : 'hRdata',
                     'sensitivityLabel' : 'activeDataCycle',
                     'sensitivity' : 'activeDataCycle',
                   },
                   {
                     'enable'      : True,
                     'name'        : 'hReadyToggle',
                     'desc'        : 'Toggle coverage of the hReady bus',
                     'kind'        : 'toggle',
                     'expr'        : 'hReady',
                     'sensitivityLabel' : 'Negative clock edge',
                     'sensitivity' : '',
                   },
                   {
                     'enable'      : True,
                     'name'        : 'hRespValue',
                     'desc'        : 'Value coverage of the hResp bus',
                     'kind'        : 'value',
                     'expr'        : 'hResp',
                     'sensitivityLabel' : 'activeDataCycle',
                     'sensitivity' : 'activeDataCycle',
                   },
                 ]

##############################################################################################################
# APB
##############################################################################################################
apbParameters = [
                  { 'enable'  : True,
                    'name'    : 'pAddr',
                    'select'  : '8',
                    'choices' : [("%s" % i) for i in range(1,32)]
                  },
                  { 'enable'  : True,
                    'name'    : 'pSel',
                    'select'  : '1',
                    'choices' : [("%s" % i) for i in range(1,32)]
                  },
                  { 'enable'  : True,
                    'name'    : 'pEnable',
                    'select'  : None,
                    'choices' : '',
                  },
                  { 'enable'  : True,
                    'name'    : 'pWrite',
                    'select'  : None,
                    'choices' : '',
                  },
                  { 'enable'  : True,
                    'name'    : 'pWdata',
                    'select'  : '8',
                    'choices' : [ '8', '16', '32' ],
                  },
                  { 'enable'  : True,
                    'name'    : 'pReady',
                    'select'  : None,
                    'choices' : '',
                  },
                  { 'enable'  : True,
                    'name'    : 'pRdata',
                    'select'  : '8',
                    'choices' : [ '8', '16', '32' ],
                  },
                  { 'enable'  : True,
                    'name'    : 'pSlvErr',
                    'select'  : None,
                    'choices' : '',
                  },
                ]

apbCoverpoints = [
                   {
                     'enable'      : True,
                     'name'        : 'ActiveDataCycle',
                     'desc'        : 'Capture an active data cycle where pReady and pEnable are asserted',
                     'kind'        : 'value',
                     'expr'        : 'activeDataCycle',
                     'sensitivityLabel' : 'Negative clock edge',
                     'sensitivity' : '',
                   },
                   {
                     'enable'      : True,
                     'name'        : 'pAddrToggle',
                     'desc'        : 'Toggle coverage of the pAddr bus',
                     'kind'        : 'toggle',
                     'expr'        : 'pAddr',
                     'sensitivityLabel' : 'activeDataCycle',
                     'sensitivity' : 'activeDataCycle',
                   },
                   {
                     'enable'      : True,
                     'name'        : 'pSelToggle',
                     'desc'        : 'Toggle coverage of the pSel bus',
                     'kind'        : 'toggle',
                     'expr'        : 'pSel',
                     'sensitivityLabel' : 'activeDataCycle',
                     'sensitivity' : 'activeDataCycle',
                   },
                   {
                     'enable'      : True,
                     'name'        : 'pEnableToggle',
                     'desc'        : 'Toggle coverage of the pEnable bus',
                     'kind'        : 'toggle',
                     'expr'        : 'pEnable',
                     'sensitivityLabel' : 'Negative clock edge',
                     'sensitivity' : '',
                   },
                   {
                     'enable'      : True,
                     'name'        : 'pWriteToggle',
                     'desc'        : 'Toggle coverage of the pWrite bus',
                     'kind'        : 'toggle',
                     'expr'        : 'pWrite',
                     'sensitivityLabel' : 'activeDataCycle',
                     'sensitivity' : 'activeDataCycle',
                   },
                   {
                     'enable'      : True,
                     'name'        : 'pWdataToggle',
                     'desc'        : 'Toggle coverage of the pWdata bus',
                     'kind'        : 'toggle',
                     'expr'        : 'pWdata',
                     'sensitivityLabel' : 'activeDataCycle',
                     'sensitivity' : 'activeDataCycle',
                   },
                   {
                     'enable'      : True,
                     'name'        : 'pReadyToggle',
                     'desc'        : 'Toggle coverage of the pReady bus',
                     'kind'        : 'toggle',
                     'expr'        : 'pReady',
                     'sensitivityLabel' : 'Negative clock edge',
                     'sensitivity' : '',
                   },
                   {
                     'enable'      : True,
                     'name'        : 'pRdataToggle',
                     'desc'        : 'Toggle coverage of the pRdata bus',
                     'kind'        : 'toggle',
                     'expr'        : 'pRdata',
                     'sensitivityLabel' : 'activeDataCycle',
                     'sensitivity' : 'activeDataCycle',
                   },
                   {
                     'enable'      : True,
                     'name'        : 'pSlvErrToggle',
                     'desc'        : 'Toggle coverage of the pSlvErr bus',
                     'kind'        : 'toggle',
                     'expr'        : 'pSlvErr',
                     'sensitivityLabel' : 'activeDataCycle',
                     'sensitivity' : 'activeDataCycle',
                   },
                 ]

##############################################################################################################
# streaming axi4
##############################################################################################################
axi4StreamParameters = [
                         { 'enable' : True,
                           'name'   : 'tValid',
                           'select' : None,
                           'choices' : '',
                         },
                         { 'enable' : True,
                           'name'   : 'tReady',
                           'select' : None,
                           'choices' : '',
                         },
                         { 'enable' : True,
                           'name'   : 'tData',
                           'select' : '8',
                           'choices'  : [ '8','16','32','64','128','256', ],
                         },
                         { 'enable' : True,
                           'name'   : 'tStrb',
                           'select' : 1,
                           'choices' : [ '1', '2', '4', '8', '16', '32'],
                         },
                         { 'enable' : True,
                           'name'   : 'tLast',
                           'select' : None,
                           'choices' : '',
                         },
                         { 'enable' : True,
                           'name'   : 'tKeep',
                           'select' : 4,
                           'choices' : [("%s" % i) for i in range(1,16)]
                         },
                         { 'enable' : True,
                           'name'   : 'tId',
                           'select' : 4,
                           'choices' : [("%s" % i) for i in range(1,16)]
                         },
                         { 'enable' : True,
                           'name'   : 'tDest',
                           'select' : 4,
                           'choices' : [("%s" % i) for i in range(1,16)]
                         },
                         { 'enable' : True,
                           'name'   : 'tUser',
                           'select' : 4,
                           'choices' : [("%s" % i) for i in range(1,16)]
                         },
                       ]

axi4StreamCoverpoints = [
                          {
                            'enable'      : True,
                            'name'        : 'ActiveDataCycle',
                            'desc'        : 'Capture an active data cycle where tReady and tValid are asserted',
                            'kind'        : 'value',
                            'expr'        : 'activeDataCycle',
                            'sensitivityLabel' : 'Negative clock edge',
                            'sensitivity' : '',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tDataToggle',
                            'desc'        : 'Toggle coverage of the tData bus',
                            'kind'        : 'toggle',
                            'expr'        : 'tData',
                            'sensitivityLabel' : 'activeDataCycle',
                            'sensitivity' : 'activeDataCycle',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tStrbValues',
                            'desc'        : 'Value coverage of the tStrb bus',
                            'kind'        : 'value',
                            'expr'        : 'tStrb',
                            'sensitivityLabel' : 'activeDataCycle',
                            'sensitivity' : 'activeDataCycle',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tKeepValues',
                            'desc'        : 'Value coverage of the tKeep bus',
                            'kind'        : 'value',
                            'expr'        : 'tKeep',
                            'sensitivityLabel' : 'activeDataCycle',
                            'sensitivity' : 'activeDataCycle',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tLastToggle',
                            'desc'        : 'Toggle coverage of tLast',
                            'kind'        : 'value',
                            'expr'        : 'tLast',
                            'sensitivityLabel' : 'activeDataCycle',
                            'sensitivity' : 'activeDataCycle',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tIdValues',
                            'desc'        : 'Value coverage of the tId bus',
                            'kind'        : 'value',
                            'expr'        : 'tId',
                            'sensitivityLabel' : 'activeDataCycle',
                            'sensitivity' : 'activeDataCycle',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tDestValues',
                            'desc'        : 'Value coverage of the tDest bus',
                            'kind'        : 'value',
                            'expr'        : 'tDest',
                            'sensitivityLabel' : 'activeDataCycle',
                            'sensitivity' : 'activeDataCycle',
                          },
                          {
                            'enable'      : True,
                            'name'        : 'tUserValues',
                            'desc'        : 'Value coverage of the tUser bus',
                            'kind'        : 'value',
                            'expr'        : 'tUser',
                            'sensitivityLabel' : 'activeDataCycle',
                            'sensitivity' : 'activeDataCycle',
                          },
                        ]
