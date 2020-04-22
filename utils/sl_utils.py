# -*- coding: utf-8 -*-
# utils/sl.utils.py

import pickle as pkl

#### save_file, load_file
#### save_file: 用文件方式保存python变量
#### load_file: 读取以此法得到的文件，获得python变量

def save_file(var, filename):
    """输入一个变量和一个文件名，将这个变量存入这个文件名对应的文件中。这个函数基于pickle.dump
    @param: var(python var): python中的一个变量
    @param: filename(str): 变量将存入这个目标路径。这个路径最好是一个.pkl文件
    @returns: None
    @usage example: save_file(name_list, "save/namelist.pkl")
    """
    tmp_file = open(filename, 'wb')
    pkl.dump(var, tmp_file)
    tmp_file.close()


def load_file(filename):
    """读取一个文件名，加载这个文件名对应的内容。这个函数基于pickle.load
    @param: filename(str): 文件名，对应一个通过save_file生成的文件
    @returns: var(python var: 这个文件对应的python变量
    @usage example: name_list = open_file("save/namelist.pkl")
    """
    tmp_file = open(filename, 'rb')
    var = pkl.load(tmp_file)
    tmp_file.close()
    return var


#### 单元测试

def test_save_file():
    va = [2, 3, 5, 7, 11]
    save_file(va, "ls.pkl")


def test_load_file():
    va = load_file('ls.pkl')
    print(va)
