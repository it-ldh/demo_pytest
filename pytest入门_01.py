
"""
@作  者:
@文件名:
@日  期:
"""
#1.导入pytest
import pytest
#2.测试函数
def test_register():
    print("输入用户名")
    print("输入邮箱")
    print("输入密码")
    print("点击注册")
def testlihui():
    pass

def test_0814():
    print("test0814")
if __name__ == '__main__':
    pytest.main(["-s","-v"])