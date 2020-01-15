"""
@作  者:
@文件名:
@日  期:
"""
#1.导入pytest
import pytest

def setup_function():
    print("函数级别的setup")

def teardown_function():
    print("函数级别的teardown")

def test_login():
    print("执行登录测试用例")
    assert True

class TestCart:
    def setup_class(self):
        print("类级别的setup")

    def teardown_class(self):
        print("类级别的teardown")

    def setup_method(self):
        print("方法级别的setup")

    def teardown_method(self):
        print("方法级别的teardown")

    def test_add_cart(self):
        print("执行添加购物车用例")
        assert True

if __name__ == '__main__':
    pytest.main()