# -*- coding: UTF-8 -*-
from count import is_prime
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        print ("test start")
        # number = input("Enter a number:")
        # self.number = int(number)

    def test_case(self):
        # self.assertEqual(self.number,10,msg="Your input is not 10!")   #assertEqual()比较第一个参数是否等于第二个参数
        # self.assertTrue(is_prime(7),msg="is not prime!")               #assertTrue()测试表达式是true
        a = "hello"                                                      #assertIn()断言第一个参数是否在第二个参数中
        b = "hello world"
        self.assertIn(a,b,msg="a is not in b")

    def tearDown(self):
        print ("test end")

if __name__ == '__main__':
    unittest.main()

