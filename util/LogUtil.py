# coding=utf-8
"""
Author : AA359290
Created on : 05/02/2017 4:58 PM
"""

import logging
import logging.handlers
import sys
import inspect
import datetime
from datetime import datetime
import ConfigParser
import os

from ConfigReader import ConfigReader


class LogUtil(object):

    """
    Utility for log
    """

    def __init__(self):

        log_level = logging.DEBUG
        level = 'debug'
        configReader = ConfigReader()
        path = configReader.getConfig('LOG', 'filename')
        #print "1:",os.path.dirname(__file__)
        #print "2:",os.path.abspath()
        #logFilepath = os.path.abspath(os.path.dirname(__file__))+"/"+path
        logFilepath = os.path.abspath(os.pardir)+"/"+path
        #print "path confirm::",logFilepath
        #print"parent dir:", os.path.abspath(os.pardir)
        #print logFilepath
        logFile = logFilepath+str(datetime.now().date())
        #print logFile
        level = configReader.getConfig('LOG', 'level') #logging.INFO
        #print level
        level = level.upper()
        #print level
        if (level == 'DEBUG'):
         log_level = logging.DEBUG
        elif (level == 'INFO'):
         log_level = logging.INFO
        elif (level == 'WARN'):
         log_level = logging.WARN
        elif (level == 'ERROR'):
         log_level = logging.ERROR
        elif (level == 'CRITICAL'):
         log_level = logging.CRITICAL    

        logging.basicConfig(level=log_level,
                        format=' %(levelname)-2s %(asctime)s %(name)s %(message)s',
                        datefmt='%m-%d-%y %H:%M',
                        filename=logFile)


    def debug(self,message):
        func = inspect.currentframe().f_back.f_code
        logging.debug("%s %i : %s" % (
            func.co_filename,
            inspect.currentframe().f_back.f_lineno,
            message
        ))

    def info(self,message):
        func = inspect.currentframe().f_back.f_code
        logging.info("%s %i : %s" % (
            func.co_filename,
            inspect.currentframe().f_back.f_lineno,
            message
        ))



    def warn(self,message):
        func = inspect.currentframe().f_back.f_code
        logging.warn("%s %i : %s" % (
            func.co_filename,
            inspect.currentframe().f_back.f_lineno,
            message
        ))

    def error(self,message):
        func = inspect.currentframe().f_back.f_code
        logging.error("%s %i : %s" % (
            func.co_filename,
            inspect.currentframe().f_back.f_lineno,
            message
        ))

    def critical(self,message):
        func = inspect.currentframe().f_back.f_code
        logging.critical("%s %i : %s" % (
            func.co_filename,
            inspect.currentframe().f_back.f_lineno,
            message
        ))
