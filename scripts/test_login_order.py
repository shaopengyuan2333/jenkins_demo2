import pytest


class TestLogin:
    @pytest.mark.run(order=1)
    def test_login_1(self):
        """记住密码登录"""
        print("1")

    @pytest.mark.run(order=1.5)
    def test_login_2(self):
        """不记住密码登录"""
        print("1.5")

    @pytest.mark.run(order=2)
    def test_login_3(self):
        """不记住密码登录"""
        print("2")

    @pytest.mark.run(order=0)
    def test_login_4(self):
        """不记住密码登录"""
        print("0")

    @pytest.mark.run(order=-1)
    def test_login_5(self):
        """不记住密码登录"""
        print("-1")

    @pytest.mark.run(order=-1.5)
    def test_login_6(self):
        """不记住密码登录"""
        print("-1.5")

    @pytest.mark.run(order=-2)
    def test_login_7(self):
        """不记住密码登录"""
        print("-2")

    def test_login_8(self):
        """不记住密码登录"""
        print("没有标记顺序")