import pytest
import allure


class TestLogin:
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="记住密码登录的测试脚本")
    def test_login_1(self,data):
        """记住密码登录"""
        allure.attach("输入用户名","输入用户名username_1")
        print("输入用户名")
        allure.attach("输入密码", "输入用户名password_1")
        print("输入密码")
        allure.attach("点击登录", "登录成功")
        print("点击登录")
        print(data)
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="记住密码登录的测试脚本")
    def test_login_2(self, data):
        """记住密码登录"""
        allure.attach("输入用户名", "输入用户名username_2")
        print("输入用户名")
        allure.attach("输入密码", "输入用户名password_2")
        print("输入密码")
        allure.attach("点击登录", "登录成功")
        print("点击登录")
        print(data)
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @pytest.allure.step(title="记住密码登录的测试脚本")
    def test_login_3(self, data):
        """记住密码登录"""
        allure.attach("输入用户名", "输入用户名username_3")
        print("输入用户名")
        allure.attach("输入密码", "输入用户名password_3")
        print("输入密码")
        allure.attach("点击登录", "登录成功")
        print("点击登录")
        print(data)
        assert False

    def setup(self):
        print("setup处理器")

    @pytest.fixture(params=[1,2,3])
    def data(self,request):
        print("测试数据")
        return request.param