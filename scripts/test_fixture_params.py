"""
@作  者:
@文件名:
@日  期:
"""

import pytest


# @pytest.fixture(params=[1, 2, 3])
# def new_data(request):
#     return request.param
#
#
# def test_data(new_data):
#     print("测试步骤")
#     assert new_data == 3

@pytest.fixture(params=[["tom", "123"], ["jerry", "456"], ["tweety", "789"]])
def login(request):
    print("用户%s,密码%s登录" % (request.param[0], request.param[1]))


def test_add_cart(login):
    print("添加购物车")
