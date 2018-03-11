#-*- coding:utf-8 -*-

import unittest

loader = unittest.TestLoader()
    
suite = loader.discover(start_dir='.', pattern='*Test.py')

runner = unittest.TextTestRunner(verbosity=5)
result = runner.run(suite)