#-*- coding:utf-8 -*-
import os
from helpers import callCommandHelper



def CreateDll(folderTargetName, fileTargetName,fileSO):
    '''
    если нет то создает папку folderTargetName
    
    если в данной папке есть ранее созданные объектные файлы, 
    то они удаляются.
    Если в данной папке есть ранее созданная динамическо линкуемая 
    библиоткека то она удаляется
    
    в данную папку будут помещенны объектные файлы.
    в данную папку будет помещенна создаваемая динамическо линкуемая 
    библиоткека       
    '''
    
    
    templateCompill = "g++  {flags}  {fileSourse} -o {fileTarget}"
    templateLinc    = "g++  -shared {objectfile} -o {fileTarget}"


    if os.path.exists(folderTargetName) == False:
        os.makedirs(folderTargetName)
    

#---------------delete old version-----------------------------------
    if os.path.exists(fileTargetName):
        os.remove(fileTargetName)
        #print("remove : "+ fileTargetName)
    for fso in fileSO:
        if os.path.exists(fso["rezultName"]):
            os.remove(fso["rezultName"])
            #print("remove : "+ fso["rezultName"])
#---------------compil -----------------------------------------------
    
    for filePair in fileSO:
        fileSourseName  =  filePair["sourseName"]
        fileObjecteName = filePair["rezultName"]
        flagCompil = filePair["flagsCompil"]
        cmd = templateCompill.format(
            fileSourse = fileSourseName,
            flags      = flagCompil, 
            fileTarget = fileObjecteName)
        
        
        callCommandHelper.CallCommandHelper(cmd)
   
#---------------linck-----------------------------------------------
    fileObjectName = " "
    for filePair in fileSO:
        fileObjectName = fileObjectName + filePair["rezultName"]+" "
    
    
    cmd = templateLinc.format(
        objectfile = fileObjectName,
        fileTarget = fileTargetName)
    
    
    callCommandHelper.CallCommandHelper(cmd)    
#=====================================================================    
