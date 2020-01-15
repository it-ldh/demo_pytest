"""
@作  者:
@文件名:
@日  期:
"""
import pytest
# def setup_function():
#     print("打开浏览器")
#
# def teardown_function():
#     print("关闭浏览器")

@pytest.mark.run(order=2)
def test_login():
    print("执行测试登录用例")

@pytest.mark.run(order=1)
def test_add_cart():
    print("执行测试添加购物车用例")

@pytest.mark.run(order=3)
def test_order():
    print("执行测试下单用例")