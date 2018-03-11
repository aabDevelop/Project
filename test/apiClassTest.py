#-*- coding:utf-8 -*-
import os
import ctypes

from helpers import creteDll

import unittest

class ApiClassTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):

                
        folderTargetName = os.path.join(os.path.dirname(__file__),"ApiClassTest")
        
        
        fileSO =  [
                    {
                    "sourseName":os.path.abspath("../src/api/ApiClass.cpp"),
                    "flagsCompil":"-Wall -c -fPIC",
                    "rezultName" :os.path.join(folderTargetName,"ApiClass.o")
                    },
                    {
                    "sourseName":os.path.join(folderTargetName,"ApiClassAdapter.cpp"),
                    "flagsCompil":"-Wall -c -fPIC -I../src/api",
                    "rezultName" :os.path.join(folderTargetName,"ApiClassAdapter.o")
                    }
                   ]
                   
        fileTargetName = os.path.join(folderTargetName,"ApiClass.dll")
                   
        #=====================================================================    
        creteDll.CreateDll(folderTargetName, fileTargetName, fileSO)    
                  
        lib = ctypes.cdll.LoadLibrary(fileTargetName)
    
        self.createEmptyApiClass = lib.createEmptyApiClass        
        self.deleteEmptyApiClass = lib.deleteEmptyApiClass        
    
        self.callEmptyApiClassMethod = lib.callEmptyApiClassMethod
        self.callEmptyApiClassMethod.restype = ctypes.c_int
        
        self.createApiClass = lib.createApiClass        
        self.deleteApiClass = lib.deleteApiClass        
    
        self.callApiClassMethod = lib.callApiClassMethod
        self.callApiClassMethod.restype = ctypes.c_int
        
    
    def tearDown(self):
        self.deleteEmptyApiClass()
        self.deleteApiClass()
    
        
    def test_var1(self):
        self.createEmptyApiClass()
        self.assertEqual(self.callEmptyApiClassMethod(10), 10,'10+0 = 10')
        self.assertEqual(self.callEmptyApiClassMethod(20), 30,'20+10 = 30')


    def test_var2(self):
        self.createApiClass(100)
        self.assertEqual(self.callApiClassMethod(10), 110,'10+100 = 110')
        self.assertEqual(self.callApiClassMethod(20), 130,'20+110 = 130')
         
        
