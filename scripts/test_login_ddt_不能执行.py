"""
多个参数的参数化
"""


import pytest
import ddt
test_data = [{"username":"zhangsan","password":"123456"},
             {"username": "lisi", "password": "123456"},
             {"username": "jerry", "password": "123456"}]

@ddt.ddt
class TestLogin:

    # @pytest.mark.parametrize("data",[3,6,9])  # data参数被赋予三个值，函数会运⾏三遍
    # def test_login_1(self,data):  # 参数必须和parametrize⾥⾯的参数⼀致
    #     """记住密码登录"""
    #     print("test data:a=%d" % data)
    #     assert data % 3 == 0

    # @pytest.mark.parametrize(("username","password"), [("张三","123"),("李四", "456"),("王五", "789")])
    # def test_login_2(self, username,password):  # 参数必须和parametrize⾥⾯的参数⼀致
    @ddt.data(*test_data)
    def test_login_2(self,data):
        """记住密码登录"""
        print("username: ----> %s" % data["username"])
        print("password: ----> %s" % data["password"])


