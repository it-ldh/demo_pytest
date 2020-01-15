"""
@作  者:
@文件名:
@日  期:
"""
import pytest


# 当条件为真,用例执行失败
@pytest.mark.xfail(condition=True, reason="")
def test_01():
    print("当条件为真,用例执行失败")
    assert False


@pytest.mark.xfail(condition=True, reason="")
# 当条件为真,用例执行成功
def test_02():
    print("当条件为真,用例执行成功")
    assert True


@pytest.mark.xfail(condition=False, reason="")
# 当条件为假,用例执行失败
def test_03():
    print("当条件为假,用例执行失败")
    assert False


@pytest.mark.xfail(condition=False, reason="")
# 当条件为假,用例执行成功
def test_04():
    print("当条件为假,用例执行成功")
    assert True
