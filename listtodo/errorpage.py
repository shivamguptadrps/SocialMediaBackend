import sys
import os
import datetime
import logging
from Todobackend.settings import BASE_DIR
from logging import Formatter, handlers as loghandler


logObj = logging.getLogger()
format  = Formatter('%(asctime)s %(message)s')
loghandle = loghandler.RotatingFileHandler(filename="{}/logs/error.log".format(BASE_DIR), maxBytes=20000000, backupCount=1)
loghandle.setFormatter(format)
loghandle.setLevel(logging.ERROR)
logObj.addHandler(loghandle)
version = "2.5.0.0"

def throwError(e):
    error = str(e)  # str(e.__dict__.get('orig'))
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    logObj.error("*****************Error*************************")
    logObj.error("{}-ERROR: {} in file {} at line no {} IN PROCESS {} IN V-{}".format(
        datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), error, fname, exc_tb.tb_lineno, os.getpid(),"version"))
    logObj.error("*****************Error*************************")
    return "Error :{}".format(error)


def printLog(msg):
    logObj.error(": {} IN PROCESS {} IN V-{}".format(msg, os.getpid(), version))
