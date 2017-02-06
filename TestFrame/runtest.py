# -*- coding: UTF-8 -*-
import unittest

# 加载测试文件
# import testadd
# import testsub
#
# #构造测试集
# suite = unittest.TestSuite()
#
# suite.addTest(testadd.TestAdd("test_add"))
# suite.addTest(testadd.TestAdd("test_add2"))
# suite.addTest(testsub.TestSub("test_sub"))
# suite.addTest(testsub.TestSub("test_sub2"))
#
# if __name__ == '__main__':
#     #运行测试集合
#     runner = unittest.TextTestRunner()
#     runner.run(suite)

# 为了解决添加用例的问题
# 定义测试用例的目录为当前目录
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)
