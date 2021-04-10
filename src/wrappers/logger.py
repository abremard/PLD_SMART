"""
Python logging module wrapper with file retention system
"""

import os
import subprocess
import datetime
import logging
import sys
import time
import datetime

def debug(logInfo):
    """ DEBUG level log

    Args:
        logInfo (str): log message
    """    
    logging.debug(logInfo+" "+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

def info(logInfo):
    """ INFO level log

    Args:
        logInfo (str): log message
    """    
    logging.info(logInfo+" "+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

def error(logInfo):
    """ ERROR level log

    Args:
        logInfo (str): log message
    """    
    logging.error(logInfo+" "+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

def log_config(directory, filename, level="DEBUG"):
    """ Initial logging configuration for project. 1 file for 1 day. Log message is appended to the file of current day. Retention is set in the powershell script.
    """    
    # Log config
    pspath = os.path.abspath("src/wrappers/log-retention.ps1")
    logpath = os.path.abspath(directory)
    p = subprocess.Popen(["powershell.exe", 
                pspath, logpath], 
                stdout=sys.stdout)
    p.communicate()
    logDay = datetime.datetime.now().strftime('%d-%m-%Y')
    
    if level == "DEBUG":
        level = logging.DEBUG
    elif level == "INFO":
        level = logging.INFO
    else:
        level = logging.ERROR
        
    logging.basicConfig(filename=directory+filename+"_"+logDay+'.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s',  datefmt='%d-%b-%y %H:%M:%S', level=level)