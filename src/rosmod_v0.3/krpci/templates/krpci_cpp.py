#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1435691902.445487
__CHEETAH_genTimestamp__ = 'Tue Jun 30 14:18:22 2015'
__CHEETAH_src__ = '/home/jeb/Repositories/rosmod/src/rosmod_v0.3/krpci/templates/krpci_cpp.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Jun 24 10:41:06 2015'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class krpci_cpp(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(krpci_cpp, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        _v = VFSL([locals()]+SL+[globals(), builtin],"hash_include",True) # u'$hash_include' on line 1, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'$hash_include')) # from line 1, col 1.
        write(u''' "krpci/krpci.hpp"
using namespace std;

''')
        if VFSL([locals()]+SL+[globals(), builtin],"services",True) != []: # generated from line 4, col 1
            for service in VFSL([locals()]+SL+[globals(), builtin],"services",True): # generated from line 5, col 1
                if VFSL([locals()]+SL+[globals(), builtin],"service.procedures",True) != []: # generated from line 6, col 1
                    for procedure in VFSL([locals()]+SL+[globals(), builtin],"service.procedures",True): # generated from line 7, col 1
                        if VFSL([locals()]+SL+[globals(), builtin],"procedure.parameters",True) != []: # generated from line 8, col 1
                            write(u'''bool KRPCI::''')
                            _v = VFSL([locals()]+SL+[globals(), builtin],"procedure.name",True) # u'${procedure.name}' on line 9, col 13
                            if _v is not None: write(_filter(_v, rawExpr=u'${procedure.name}')) # from line 9, col 13.
                            write(u'''_createRequest(''')
                            _v = VFSL([locals()]+SL+[globals(), builtin],"procedure.input_args",True) # u'${procedure.input_args}' on line 9, col 45
                            if _v is not None: write(_filter(_v, rawExpr=u'${procedure.input_args}')) # from line 9, col 45.
                            write(u''', krpc::Request& request)
''')
                        else: # generated from line 10, col 1
                            write(u'''bool KRPCI::''')
                            _v = VFSL([locals()]+SL+[globals(), builtin],"procedure.name",True) # u'${procedure.name}' on line 11, col 13
                            if _v is not None: write(_filter(_v, rawExpr=u'${procedure.name}')) # from line 11, col 13.
                            write(u'''_createRequest(krpc::Request& request)
''')
                        write(u'''{
  request.set_service("''')
                        _v = VFSL([locals()]+SL+[globals(), builtin],"service.name",True) # u'${service.name}' on line 14, col 24
                        if _v is not None: write(_filter(_v, rawExpr=u'${service.name}')) # from line 14, col 24.
                        write(u'''");
  request.set_procedure("''')
                        _v = VFSL([locals()]+SL+[globals(), builtin],"procedure.name",True) # u'${procedure.name}' on line 15, col 26
                        if _v is not None: write(_filter(_v, rawExpr=u'${procedure.name}')) # from line 15, col 26.
                        write(u'''");
''')
                        if VFSL([locals()]+SL+[globals(), builtin],"procedure.parameters",True) != []: # generated from line 16, col 1
                            write(u'''  krpc::Argument* argument;
''')
                        if VFSL([locals()]+SL+[globals(), builtin],"procedure.parameters",True) != []: # generated from line 19, col 1
                            for parameter in VFSL([locals()]+SL+[globals(), builtin],"procedure.parameters",True): # generated from line 20, col 1
                                write(u'''  argument = request.add_arguments();
  argument->set_position(''')
                                _v = VFSL([locals()]+SL+[globals(), builtin],"parameter.position",True) # u'${parameter.position}' on line 22, col 26
                                if _v is not None: write(_filter(_v, rawExpr=u'${parameter.position}')) # from line 22, col 26.
                                write(u''');
''')
                                if VFSL([locals()]+SL+[globals(), builtin],"parameter.datatype",True) == "uint64_t": # generated from line 23, col 1
                                    write(u'''  argument->mutable_value()->resize(10);
  CodedOutputStream::WriteVarint64ToArray(''')
                                    _v = VFSL([locals()]+SL+[globals(), builtin],"parameter.name",True) # u'${parameter.name}' on line 25, col 43
                                    if _v is not None: write(_filter(_v, rawExpr=u'${parameter.name}')) # from line 25, col 43.
                                    write(u''', 
\t\t      (unsigned char *)argument->mutable_value()->data());

''')
                                elif VFSL([locals()]+SL+[globals(), builtin],"parameter.datatype",True) == "float": # generated from line 28, col 1
                                    write(u'''  argument->set_value((const char*)(&''')
                                    _v = VFSL([locals()]+SL+[globals(), builtin],"parameter.name",True) # u'${parameter.name}' on line 29, col 38
                                    if _v is not None: write(_filter(_v, rawExpr=u'${parameter.name}')) # from line 29, col 38.
                                    write(u'''), sizeof(''')
                                    _v = VFSL([locals()]+SL+[globals(), builtin],"parameter.name",True) # u'${parameter.name}' on line 29, col 65
                                    if _v is not None: write(_filter(_v, rawExpr=u'${parameter.name}')) # from line 29, col 65.
                                    write(u'''));

''')
                                elif VFSL([locals()]+SL+[globals(), builtin],"parameter.datatype",True) == "double": # generated from line 31, col 1
                                    write(u'''  argument->set_value((const char*)(&''')
                                    _v = VFSL([locals()]+SL+[globals(), builtin],"parameter.name",True) # u'${parameter.name}' on line 32, col 38
                                    if _v is not None: write(_filter(_v, rawExpr=u'${parameter.name}')) # from line 32, col 38.
                                    write(u'''), sizeof(''')
                                    _v = VFSL([locals()]+SL+[globals(), builtin],"parameter.name",True) # u'${parameter.name}' on line 32, col 65
                                    if _v is not None: write(_filter(_v, rawExpr=u'${parameter.name}')) # from line 32, col 65.
                                    write(u'''));  

''')
                                elif VFSL([locals()]+SL+[globals(), builtin],"parameter.datatype",True) == "bool": # generated from line 34, col 1
                                    write(u'''  argument->mutable_value()->resize(10);
  CodedOutputStream::WriteVarint32ToArray(''')
                                    _v = VFSL([locals()]+SL+[globals(), builtin],"parameter.name",True) # u'${parameter.name}' on line 36, col 43
                                    if _v is not None: write(_filter(_v, rawExpr=u'${parameter.name}')) # from line 36, col 43.
                                    write(u''', 
\t\t      (unsigned char *)argument->mutable_value()->data());

''')
                                elif VFSL([locals()]+SL+[globals(), builtin],"parameter.datatype",True) == "KRPC.Tuple": # generated from line 39, col 1
                                    write(u'''  krpc::Tuple ''')
                                    _v = VFSL([locals()]+SL+[globals(), builtin],"parameter.name",True) # u'${parameter.name}' on line 40, col 15
                                    if _v is not None: write(_filter(_v, rawExpr=u'${parameter.name}')) # from line 40, col 15.
                                    write(u''';
  KRPCI::EncodeTuple(''')
                                    _v = VFSL([locals()]+SL+[globals(), builtin],"parameter.name",True) # u'${parameter.name}' on line 41, col 22
                                    if _v is not None: write(_filter(_v, rawExpr=u'${parameter.name}')) # from line 41, col 22.
                                    write(u'''_x, 
\t\t     ''')
                                    _v = VFSL([locals()]+SL+[globals(), builtin],"parameter.name",True) # u'${parameter.name}' on line 42, col 8
                                    if _v is not None: write(_filter(_v, rawExpr=u'${parameter.name}')) # from line 42, col 8.
                                    write(u'''_y, 
\t\t     ''')
                                    _v = VFSL([locals()]+SL+[globals(), builtin],"parameter.name",True) # u'${parameter.name}' on line 43, col 8
                                    if _v is not None: write(_filter(_v, rawExpr=u'${parameter.name}')) # from line 43, col 8.
                                    write(u'''_z, 
\t\t     ''')
                                    _v = VFSL([locals()]+SL+[globals(), builtin],"parameter.name",True) # u'${parameter.name}' on line 44, col 8
                                    if _v is not None: write(_filter(_v, rawExpr=u'${parameter.name}')) # from line 44, col 8.
                                    write(u'''); 
  ''')
                                    _v = VFSL([locals()]+SL+[globals(), builtin],"parameter.name",True) # u'${parameter.name}' on line 45, col 3
                                    if _v is not None: write(_filter(_v, rawExpr=u'${parameter.name}')) # from line 45, col 3.
                                    write(u'''.SerializeToString(argument->mutable_value());

''')
                                elif VFSL([locals()]+SL+[globals(), builtin],"parameter.datatype",True) == "KRPC.List": # generated from line 47, col 1
                                    write(u'''  ''')
                                    _v = VFSL([locals()]+SL+[globals(), builtin],"parameter.name",True) # u'${parameter.name}' on line 48, col 3
                                    if _v is not None: write(_filter(_v, rawExpr=u'${parameter.name}')) # from line 48, col 3.
                                    write(u'''.SerializeToString(argument->mutable_value());

''')
                                elif VFSL([locals()]+SL+[globals(), builtin],"parameter.datatype",True) == "KRPC.Dictionary": # generated from line 50, col 1
                                    write(u'''  ''')
                                    _v = VFSL([locals()]+SL+[globals(), builtin],"parameter.name",True) # u'${parameter.name}' on line 51, col 3
                                    if _v is not None: write(_filter(_v, rawExpr=u'${parameter.name}')) # from line 51, col 3.
                                    write(u'''.SerializeToString(argument->mutable_value());

''')
                        write(u'''  return true;
}

bool KRPCI::''')
                        _v = VFSL([locals()]+SL+[globals(), builtin],"procedure.name",True) # u'${procedure.name}' on line 59, col 13
                        if _v is not None: write(_filter(_v, rawExpr=u'${procedure.name}')) # from line 59, col 13.
                        write(u'''(''')
                        _v = VFSL([locals()]+SL+[globals(), builtin],"procedure.args",True) # u'${procedure.args}' on line 59, col 31
                        if _v is not None: write(_filter(_v, rawExpr=u'${procedure.args}')) # from line 59, col 31.
                        write(u''')
{
  if (!connected_)
    return false;
  krpc::Request request;
  krpc::Response response;
''')
                        if VFSL([locals()]+SL+[globals(), builtin],"procedure.parameters",True) != []: # generated from line 65, col 1
                            write(u'''  KRPCI::''')
                            _v = VFSL([locals()]+SL+[globals(), builtin],"procedure.name",True) # u'${procedure.name}' on line 66, col 10
                            if _v is not None: write(_filter(_v, rawExpr=u'${procedure.name}')) # from line 66, col 10.
                            write(u'''_createRequest(''')
                            _v = VFSL([locals()]+SL+[globals(), builtin],"procedure.request_args",True) # u'${procedure.request_args}' on line 66, col 42
                            if _v is not None: write(_filter(_v, rawExpr=u'${procedure.request_args}')) # from line 66, col 42.
                            write(u''', request);
''')
                        else: # generated from line 67, col 1
                            write(u'''  KRPCI::''')
                            _v = VFSL([locals()]+SL+[globals(), builtin],"procedure.name",True) # u'${procedure.name}' on line 68, col 10
                            if _v is not None: write(_filter(_v, rawExpr=u'${procedure.name}')) # from line 68, col 10.
                            write(u'''_createRequest(request);
''')
                        write(u'''
  if (getResponseFromRequest(request,response))
    {
      if (response.has_error())
\t{
\t  std::cout << "Response error: " << response.error() << endl;
\t  return false;
\t}
''')
                        if VFSL([locals()]+SL+[globals(), builtin],"procedure.return_type",True) == "uint64": # generated from line 78, col 1
                            write(u'''      ''')
                            _v = VFSL([locals()]+SL+[globals(), builtin],"procedure.name",True) # u'${procedure.name}' on line 79, col 7
                            if _v is not None: write(_filter(_v, rawExpr=u'${procedure.name}')) # from line 79, col 7.
                            write(u'''_parseResponse(response, return_value);
''')
                        elif VFSL([locals()]+SL+[globals(), builtin],"procedure.return_type",True) == "KRPC.Tuple": # generated from line 80, col 1
                            write(u'''      ''')
                            _v = VFSL([locals()]+SL+[globals(), builtin],"procedure.name",True) # u'${procedure.name}' on line 81, col 7
                            if _v is not None: write(_filter(_v, rawExpr=u'${procedure.name}')) # from line 81, col 7.
                            write(u'''_parseResponse(response, x, y, z);
''')
                        elif VFSL([locals()]+SL+[globals(), builtin],"procedure.return_type",True) == "KRPC.List": # generated from line 82, col 1
                            write(u'''      ''')
                            _v = VFSL([locals()]+SL+[globals(), builtin],"procedure.name",True) # u'${procedure.name}' on line 83, col 7
                            if _v is not None: write(_filter(_v, rawExpr=u'${procedure.name}')) # from line 83, col 7.
                            write(u'''_parseResponse(response, return_vector);
''')
                        elif VFSL([locals()]+SL+[globals(), builtin],"procedure.return_type",True) == "double": # generated from line 84, col 1
                            write(u'''      ''')
                            _v = VFSL([locals()]+SL+[globals(), builtin],"procedure.name",True) # u'${procedure.name}' on line 85, col 7
                            if _v is not None: write(_filter(_v, rawExpr=u'${procedure.name}')) # from line 85, col 7.
                            write(u'''_parseResponse(response, return_value);
''')
                        elif VFSL([locals()]+SL+[globals(), builtin],"procedure.return_type",True) == "float": # generated from line 86, col 1
                            write(u'''      ''')
                            _v = VFSL([locals()]+SL+[globals(), builtin],"procedure.name",True) # u'${procedure.name}' on line 87, col 7
                            if _v is not None: write(_filter(_v, rawExpr=u'${procedure.name}')) # from line 87, col 7.
                            write(u'''_parseResponse(response, return_value);
''')
                        write(u'''    }
  return true;
}

''')
                        if VFSL([locals()]+SL+[globals(), builtin],"procedure.output_args",True) != "": # generated from line 93, col 1
                            write(u'''bool KRPCI::''')
                            _v = VFSL([locals()]+SL+[globals(), builtin],"procedure.name",True) # u'${procedure.name}' on line 94, col 13
                            if _v is not None: write(_filter(_v, rawExpr=u'${procedure.name}')) # from line 94, col 13.
                            write(u'''_parseResponse(krpc::Response response, ''')
                            _v = VFSL([locals()]+SL+[globals(), builtin],"procedure.output_args",True) # u'${procedure.output_args}' on line 94, col 70
                            if _v is not None: write(_filter(_v, rawExpr=u'${procedure.output_args}')) # from line 94, col 70.
                            write(u''')
{
''')
                            if VFSL([locals()]+SL+[globals(), builtin],"procedure.return_type",True) == "uint64": # generated from line 96, col 1
                                write(u'''  KRPCI::DecodeVarint(return_value, 
\t\t      (char *)response.return_value().data(), 
\t\t      response.return_value().size());
''')
                            elif VFSL([locals()]+SL+[globals(), builtin],"procedure.return_type",True) == "KRPC.Tuple": # generated from line 100, col 1
                                write(u'''  krpc::Tuple tuple;
  tuple.ParseFromString(response.return_value());
  KRPCI::DecodeTuple(tuple, x, y, z);
''')
                            elif VFSL([locals()]+SL+[globals(), builtin],"procedure.return_type",True) == "KRPC.List": # generated from line 104, col 1
                                write(u'''  krpc::List output_list;
  output_list.ParseFromString(response.return_value());
  for(int i=0; i< output_list.items_size(); i++)
    {
      uint64_t return_value;
      KRPCI::DecodeVarint(return_value,
\t\t\t  (char *)output_list.items(i).data(),
\t\t\t  output_list.items(i).size());
      return_vector.push_back(return_value);
    }
''')
                            elif VFSL([locals()]+SL+[globals(), builtin],"procedure.return_type",True) == "double": # generated from line 115, col 1
                                write(u'''  return_value = 0.0;
  memcpy(&return_value, response.return_value().data(), response.return_value().size());
''')
                            elif VFSL([locals()]+SL+[globals(), builtin],"procedure.return_type",True) == "float": # generated from line 118, col 1
                                write(u'''  return_value = 0.0;
  memcpy(&return_value, response.return_value().data(), response.return_value().size());
''')
                            write(u'''  return true;
}
''')
                        write(u'''
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_krpci_cpp= 'respond'

## END CLASS DEFINITION

if not hasattr(krpci_cpp, '_initCheetahAttributes'):
    templateAPIClass = getattr(krpci_cpp, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(krpci_cpp)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=krpci_cpp()).run()


