"""
@作  者:
@文件名:
@日  期:
"""
import pytest


# def setup():
#     print("连接数据库,准备测试数据")
#
# def teardown():
#     print("清除测试数据,关闭数据库连接")

@pytest.fixture()
def operation_database():
    print("连接数据库,准备测试数据")

    yield
    print("清除测试数据,关闭数据库连接")


def test_register(operation_database):
    print("测试登录")
