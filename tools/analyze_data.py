# author:lee:2021/8/17 0017 15:40
import os

import yaml

from Testfan.apiFrame.config import ABS_PATH


def analyze_data(filename,key):
    '''
    解析yml文件，得到一个列表嵌套字典的数据格式
    :param filename:要解析的yml文件
    :param key:要解析的yml文件里的key;
    :return:
    '''
    with open(ABS_PATH +f'/data/{filename}.yml','r',encoding='utf-8') as f:
        data_list = []
        yml_data = yaml.load(f,Loader=yaml.FullLoader)
        # print(yml_data)
        pre_data = yml_data.get(key).values()
        # print(pre_data)
        # for value in pre_data:
        #     print(value)
        data_list.extend(pre_data)
        # print(data_list)
        return data_list

analyze_data('test_login','test_login')