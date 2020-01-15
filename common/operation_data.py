"""
@作  者:李会
@文件名:operation_data.py
@日  期:2019/12/19
"""

import pandas
import os


class OperationFile:
    def __init__(self, filename: str):
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\data"  # 相当于"../data"
        self.filepath = os.path.join(base_path, filename)  # 文件路径
        if filename.split(".")[-1] == "csv":
            self.file = pandas.read_csv(os.path.join(base_path, filename))  # 读取csv格式的文件
        else:
            self.file = pandas.read_excel(os.path.join(base_path, filename))

    def get_data_to_list(self):
        """
        将数据读取成列表嵌套列表格式
        :return:
        """
        return self.file.values.tolist()

    def get_data_to_dict(self):
        """
        将数据读取成列表嵌套字典格式
        :return:
        """
        return [self.file.loc[i].to_dict() for i in self.file.index.values]

    def write_data_to_excel(self,data:list):
        """
        更新表格
        1.读取表格元数据
        2.将新数据插入在第一行位置
        3.将源数据追加在第一行之后
        :param data:
        :return:
        """
        #读取源数据
        old_data=self.get_data_to_list()
        #添加新数据在第一行
        self.file.loc[0]= data   #指定插入行行号
        #将老数据追加在第一行之后
        for i in range(1,len(old_data)+1):
            self.file.loc[i]=old_data[i-i]
        self.file.to_excel(self.filepath,index=None)    #保存数据




if __name__ == '__main__':
    oper = OperationFile("register_data.xls")
    from common.faker_data import Fake
    fake=Fake()
    # print(fake.get_register_data())
    # print(oper.write_data_to_excel(fake.get_register_data()))
    # # print(oper.get_data_to_list())
    # print(oper.get_data_to_dict())
    username = fake.get_name()
    email = fake.get_email()
    password = fake.get_password()
    mobile_phone = fake.get_phone()
    sel_question=fake.get_sentence()
    passwd_answer = fake.get_word()
    dit=[username,email,password,password,mobile_phone,sel_question,passwd_answer]
    oper.write_data_to_excel(dit)