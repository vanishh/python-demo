# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 23:28:53 2018

@author: Administrator
"""
class Bank(object):
    
    # 存储所有开户信息
    __userInfo = []
    
    # 用户开户
    def resigterUser(self):
        return 
    # 获取所有开户信息
    def getUserInfo(self):
        return self.__usersInfo
    
    def getUserCount(self):
        return len(self.__userInfo)
    
class User(object):
    
    def __init__(self, cardNumber, password, userName, balance):
        self.__bankCardNumber = cardNumber
        self.__password = password
        self.__userName = userName
        self.__balance = balance
        
    def queryMoney(self, cardNumber, password, money):
        if self.__bankCardNumber == cardNumber and self.__password == password:
            if money <= 0 :
                return "取的钱数不能为负"
            elif money > self.__balance:
                return "您的余额不足, 余额为：" + str(self.__balance)
            else:
                self.__balance -= money
                print("取钱成功！")
                return self.__balance
    
    def getBankCardNumber(self):
        return self.__bankCardNumber
    
    def getPassword(self):
        return self.__password
    
    def getUserName(self):
        return self.__userName
    
    def getBalance(self):
        return self.__balance

user1 = User("1234", "123", "geyang", 1000)
#print(user1.__balance)  # 访问不到，balance为私有属性
print(user1.getBalance())
balance = user1.queryMoney("1234", "123", 50)

# 单元测试
# 引入Python自带的unittest模块
import unittest

# 单元测试类继承自unittest的TestCase类
class TestUser(unittest.TestCase):
    
    # 在单元测试中编写两个特殊的方法
    # 在每个测试用例之前运行该方法
    def setUp(self):
        print("set up")
        
    # 在每个测试用例之后运行该方法
    def tearDown(self):
        print("tear down")
        
    # 单元测试用例
    def test_init(self):
        user = User("1234","123", "geyang", 1000)
        self.assertEqual(user.getBalance(), 1000)
        self.assertEqual(user.getUserName(), "geyang")
        self.assertIsNotNone(user.getPassword())
        self.assertTrue(user.getBankCardNumber() == "1234")
        
    def test_query_money(self):
        user = User("1234","123", "geyang", 1000)
        bankCardNumber = "1234"
        password = "123"
        self.assertEqual(user.queryMoney(bankCardNumber, password, 100), 900)

# 运行单元测试
if __name__ == "__main__":
    unittest.main()