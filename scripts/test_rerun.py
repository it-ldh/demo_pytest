"""
@作  者:
@文件名:
@日  期:
"""
import random

class TestCart:
    def test_add_cart(self):
        print("执行添加购物车")
        assert True

    def test_cart_list(self):
        print("执行查看购物车")
        num=random.randint(0,1)
        if num==0:
            assert False
        else:
            assert True

    def test_update_cart(self):
        print("执行更新购物车")
        assert True

    def test_delete_cart(self):
        print("执行删除购物车")
        assert True