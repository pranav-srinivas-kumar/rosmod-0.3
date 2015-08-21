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
__CHEETAH_genTime__ = 1440190063.025103
__CHEETAH_genTimestamp__ = 'Fri Aug 21 15:47:43 2015'
__CHEETAH_src__ = '/home/jeb/Repositories/rosmod-gui/src/rosmod_v0.3/templates/Logger_cpp.tmpl'
__CHEETAH_srcLastModified__ = 'Mon Aug 17 21:11:39 2015'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class Logger_cpp(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(Logger_cpp, self).__init__(*args, **KWs)
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
        write(u''' "''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"package_name",True) # u'$package_name' on line 1, col 16
        if _v is not None: write(_filter(_v, rawExpr=u'$package_name')) # from line 1, col 16.
        write(u'''/Logger.hpp"

/*
 * Write remaining log contents to file
 */
Logger::~Logger() {
  WRITE_TO_FILE();
  log_stream.close();
}

/*
 * Open file outstream @ provided target path
 */
bool Logger::CREATE_FILE(string target_log_path) {
  log_path = target_log_path;
  log_stream.open(log_path, ios::out | ios::app );  
  log_content = "--------------------------------------------------------------------------------\\n";
  return true;
}

/*
 * Write Log contents to file & close stream
 */ 
bool Logger::WRITE_TO_FILE() {
  log_stream << log_content;
  log_stream.flush();
  return true;
}

/*
 * Check log content size 
 * If size > max_log_unit, write to file
 */
bool Logger::CHECK_LOG_SIZE() {
  if (SIZE_OF_LOG() > max_log_unit) {
    WRITE_TO_FILE();
    log_content = "";
    return true;
  }
  return false;
}

/*
 * Create a DEBUG log entry
 */
bool Logger::DEBUG(const char * format, ...) {
  if (log_levels.DEBUG == true) {
    va_list args;
    va_start (args, format);
    char log_entry[1024];
    vsprintf (log_entry, format, args);
    std::string log_entry_string(log_entry);
    va_end (args);

    log_content += "ROSMOD::DEBUG::" + CLOCK_VALUE() + "::" + log_entry_string + "\\n"; 
  }
  return true;
}

/*
 * Create a INFORMATION log entry
 */
bool Logger::INFO(const char * format, ...) {
  if (log_levels.INFO == true) {
    va_list args;
    va_start (args, format);
    char log_entry[1024];
    vsprintf (log_entry, format, args);
    std::string log_entry_string(log_entry);
    va_end (args);

    log_content += "ROSMOD::INFO::" + CLOCK_VALUE() + "::" + log_entry_string + "\\n"; 
    CHECK_LOG_SIZE();
  }
  return true;
}

/*
 * Create a WARNING log entry
 */
bool Logger::WARNING(const char * format, ...) {
  if (log_levels.WARNING == true) {
    va_list args;
    va_start (args, format);
    char log_entry[1024];
    vsprintf (log_entry, format, args);
    std::string log_entry_string(log_entry);
    va_end (args);

    log_content += "ROSMOD::WARNING::" + CLOCK_VALUE() + "::" + log_entry_string + "\\n"; 
    CHECK_LOG_SIZE();
  }
  return true;
}

/*
 * Create an ERROR log entry
 */
bool Logger::ERROR(const char * format, ...) {
  if (log_levels.ERROR = true) {
    va_list args;
    va_start (args, format);
    char log_entry[1024];
    vsprintf (log_entry, format, args);
    std::string log_entry_string(log_entry);
    va_end (args);

    log_content += "ROSMOD::ERROR::" + CLOCK_VALUE() + "::" + log_entry_string + "\\n"; 
    CHECK_LOG_SIZE();
  }
  return true;
}

/*
 * Create a CRITICAL log entry
 */
bool Logger::CRITICAL(const char * format, ...) {
  if (log_levels.CRITICAL == true) {
    va_list args;
    va_start (args, format);
    char log_entry[1024];
    vsprintf (log_entry, format, args);
    std::string log_entry_string(log_entry);
    va_end (args);

    log_content += "ROSMOD::CRITICAL::" + CLOCK_VALUE() + "::" + log_entry_string + "\\n"; 
    CHECK_LOG_SIZE();
  }
  return true;
}

/*
 * Set Log Levels 
 */
bool Logger::SET_LOG_LEVELS(Log_Levels target_log_levels) {
  log_levels.DEBUG = target_log_levels.DEBUG;
  log_levels.INFO = target_log_levels.INFO;
  log_levels.WARNING = target_log_levels.WARNING;
  log_levels.ERROR = target_log_levels.ERROR;
  log_levels.CRITICAL = target_log_levels.CRITICAL;
}

/*
 * Return size of log_content
 */
int Logger::SIZE_OF_LOG() {
  return log_content.size();
}

/*
 * Get Current Clock Value
 */
string Logger::CLOCK_VALUE() {
  stringstream clock_string;
  clock_string << clock.now().time_since_epoch().count();
  return clock_string.str();  
}
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

    _mainCheetahMethod_for_Logger_cpp= 'respond'

## END CLASS DEFINITION

if not hasattr(Logger_cpp, '_initCheetahAttributes'):
    templateAPIClass = getattr(Logger_cpp, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(Logger_cpp)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=Logger_cpp()).run()


