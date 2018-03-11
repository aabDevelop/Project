#-*- coding:utf-8 -*-
import os
import ctypes

from helpers import creteDll

import unittest


class Data(ctypes.Structure):
    _fields_ = [("intValue",ctypes.c_int),("doubleValue",ctypes.c_double),("ucharValue",ctypes.c_ubyte)]

class BigData(ctypes.Structure):
    _fields_ = [("iv",ctypes.c_int),
                ("v1",ctypes.c_int,4),
                ("v2",ctypes.c_int,4),
                ("v3",ctypes.c_int,8),
                ("v4",ctypes.c_int,16),
                ("st",ctypes.c_char*12)]

class ApiFunctionTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
       

        folderTargetName = os.path.join(os.path.dirname(__file__),"ApiFunctionTest")
       
        fileSO =  [
                    {"sourseName":"../src/api/ApiFunction.cpp",
                    "flagsCompil":"-Wall -c -fPIC",
                    "rezultName" :os.path.join(folderTargetName,"ApiFunction.o")}
                  ]
                    
        fileTargetName = os.path.join(folderTargetName,"ApiFunction.dll")
                
        #===============================================================
        creteDll.CreateDll(folderTargetName, fileTargetName, fileSO)
        
        
        lib = ctypes.cdll.LoadLibrary(fileTargetName)
    
        self.apiFunction = lib.apiFunction
        self.apiFunction.restype = ctypes.c_int

        self.apiFunctionMutablePointer = lib.apiFunctionMutablePointer
        self.apiFunctionMutablePointer.argtype  = ctypes.POINTER(ctypes.c_double)
        
        
        self.apiFunctionGetData = lib.apiFunctionGetData
        self.apiFunctionGetData.restype = Data
        
        
        self.apiFunctionGetPointerData = lib.apiFunctionGetPointerData
        self.apiFunctionGetPointerData.restype = ctypes.POINTER(Data)
         
        self.apiFunctionMutablePointerData = lib.apiFunctionMutablePointerData
        self.apiFunctionMutablePointerData.argtype  = ctypes.POINTER(Data)
       
        
        self.apiFunctionGetBigData = lib.apiFunctionGetBigData
        self.apiFunctionGetBigData.restype = BigData
        
       
        
    def test_var1(self):
        self.assertEqual(self.apiFunction(10,20), 200,'10*20 = 200')


    def test_var2(self):
        self.assertEqual(self.apiFunction(30,40), 1200,'30*40 = 1200')


    def test_var3(self):
        vl = ctypes.c_double(1.1)
        print(vl.value)
        self.apiFunctionMutablePointer(ctypes.pointer(vl) )
        print(vl.value)
        self.assertEqual(vl.value, 110.00000000000001,'vl != 110')
        
    def test_var4(self):
        data = self.apiFunctionGetData()
        self.assertEqual(data.intValue, 1,'data.intValue != 1')
        self.assertEqual(data.doubleValue, 3.1415,'data.doubleValue != 3.1415')
        self.assertEqual(data.ucharValue, 0xff,'data.ucharValue != 0xff')
        
        print("\nintValue= {:d}, doubleValue= {:f}, ucharValue= {:x}".format(data.intValue,data.doubleValue,data.ucharValue ))
        
    def test_var5(self):
        pointerData = self.apiFunctionGetPointerData()    
        
        self.assertEqual(pointerData.contents.intValue, 1*2,'data.intValue != 1*2')
        self.assertEqual(pointerData.contents.doubleValue, 3.1415*2,'data.doubleValue != 3.1415 * 2')
        self.assertEqual(pointerData.contents.ucharValue, 0xAA,'data.ucharValue != 0xAA')

        print("\nintValue= {:d}, doubleValue= {:f}, ucharValue= {:x}".format(pointerData.contents.intValue,pointerData.contents.doubleValue,pointerData.contents.ucharValue ))

        
    def test_var5(self):
        pointerData = ctypes.pointer(Data())
        pointerData.contents.intValue = ctypes.c_int(10)
        pointerData.contents.doubleValue = ctypes.c_double(20)
        pointerData.contents.ucharValue = ctypes.c_ubyte(85)
        
        print("\nintValue= {:d}, doubleValue= {:f}, ucharValue= {:x}".format(pointerData.contents.intValue,pointerData.contents.doubleValue,pointerData.contents.ucharValue ))

        self.apiFunctionMutablePointerData(pointerData)
 
        print("\nintValue= {:d}, doubleValue= {:f}, ucharValue= {:x}".format(pointerData.contents.intValue,pointerData.contents.doubleValue,pointerData.contents.ucharValue ))
        
        self.assertEqual(pointerData.contents.intValue, 30,'data.intValue != 30')
        self.assertEqual(pointerData.contents.doubleValue, 60,'data.doubleValue != 60')
        self.assertEqual(pointerData.contents.ucharValue, 0xff,'data.ucharValue != 0xff')
             
    def test_var6(self):
        
        bigData = self.apiFunctionGetBigData()
        st = ctypes.c_char_p(bigData.st).value
        print(st)
        
        print("\niv= {:d}, v1= {:d},v2= {:d},v3= {:d},v4= {:d}".format(bigData.iv,
                                                                       bigData.v1,
                                                                       bigData.v2,
                                                                       bigData.v3,
                                                                       bigData.v4))
        
        self.assertEqual(bigData.iv, 1,'1')
        self.assertEqual(bigData.v1, 2,'2')
        self.assertEqual(bigData.v2, 3,'3')
        self.assertEqual(bigData.v3, 4,'4')
        self.assertEqual(bigData.v4, 5,'5')
        
        
        self.assertEqual(st in b"hello world",True,'getting string')
        
        