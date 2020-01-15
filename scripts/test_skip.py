"""
@作  者:
@文件名:
@日  期:
"""

import pytest
import random
num=random.randint(1,10)


@pytest.mark.skipif(condition=num%2==0,reason="女性跳过")
def test_browser_electronic():
    """浏览电子商品"""
    print("浏览电子商品")


@pytest.mark.skipif(condition=num%2==1,reason="男性跳过")
def test_browser_maquillage():
    """浏览化妆品"""
    print("浏览化妆品")
