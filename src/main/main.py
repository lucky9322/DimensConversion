# encoding: utf-8
"""
@contact: lucky9322@163.com
@project: DimensConversion
@software: PyCharm
@file: main.py
@time: 2017/11/29 下午1:15
"""

from src.main.calculator import Calculator

if __name__ == "__main__":
    fileName = input('输入原始文件名称：')
    scale = input('输入倍率: ')
    c = Calculator()
    c.operation(fileName, scale)
