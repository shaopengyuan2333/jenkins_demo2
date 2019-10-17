import pytest


class TestLogin:

    @pytest.mark.skipif(condition=2 > 1,reason="条件成立跳过测试")
    def test_login_1(self):
        """记住密码登录"""
        print("test_login_1记住密码登录")
        assert True

    def test_login_2(self):
        """不记住密码登录"""
        print("test_login_2不记住密码登录")
        assert True