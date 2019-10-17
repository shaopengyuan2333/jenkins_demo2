import pytest


class TestLogin:
    """
    标记为预期失败的几种情况
        1. 预期: 成功 结果: 成功
        2. 预期: 成功 结果: 失败
        3. 预期: 失败 结果: 成功
        4. 预期: 失败 结果: 失败
        预期失败,结果中以X开头
    """
    # XFailed 报告中显示橙色   x表示
    @pytest.mark.xfail(True,reason="条件成立跳过测试")  # 4. 预期: 失败 结果: 失败
    def test_login_1(self):
        """记住密码登录"""
        print("test_login_1")
        assert False

    # Passed 报告中显示绿色    .表示
    @pytest.mark.xfail(False, reason="条件成立跳过测试")  # 1. 预期: 成功 结果: 成功
    def test_login_2(self):
        """不记住密码登录"""
        print("test_login_2")
        assert True

    # XPassed 报告中显示红色   X表示
    @pytest.mark.xfail(True, reason="条件成立跳过测试")  # 3. 预期: 失败 结果: 成功
    def test_login_3(self):
        """记住密码登录"""
        print("test_login_3")
        assert True

    # Failed 报告中显示红色    F表示
    @pytest.mark.xfail(False, reason="条件成立跳过测试")  # 2. 预期: 成功 结果: 失败
    def test_login_4(self):
        """不记住密码登录"""
        print("test_login_4")
        assert False
