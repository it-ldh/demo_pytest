"""
@作  者:
@文件名:
@日  期:
"""
import pytest

@pytest.fixture()
def login():
    print("登录成功!")


def test_get_address(login):
    print("进入个人在中心,查看收货地址")


def test_get_collection(login):
    print("进入个人中心,查看收藏夹")


def test_browser_goods():
    print("不需要登录,浏览商品")
