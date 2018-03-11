#-*- coding:utf-8 -*-
import subprocess

class CallCommandHelperException(Exception):
    pass
    

def CallCommandHelper(cmd):
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True) as proc:
        if proc.wait() != 0:            
            raise CallCommandHelperException("error :" +cmd)