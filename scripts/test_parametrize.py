"""
@作  者:
@文件名:
@日  期:
"""

import pytest
from common.operation_data import OperationFile


@pytest.mark.parametrize("phone", ["18080022293", "18080022292"])
def test_verifycode(phone):
    print("输入电话:", phone)

# data=[["110","123"],["120","234"],["119","456"]]
data=OperationFile("register_data.xls").get_data_to_list()
@pytest.mark.parametrize("phone,code",data)
def test_login(phone, code):
    print("手机号%s,验证码%s" % (phone, code))
