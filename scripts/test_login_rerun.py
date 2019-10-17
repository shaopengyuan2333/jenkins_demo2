import random


class TestLogin:

    def test_login_1(self):
        """记住密码登录"""
        print("test_login_1记住密码登录")
        num = random.randint(1,2)
        if num % 2:
            assert True
        else:
            assert False  # 断言失败

    def test_login_2(self):
        """不记住密码登录"""
        print("test_login_2不记住密码登录")
        assert True
