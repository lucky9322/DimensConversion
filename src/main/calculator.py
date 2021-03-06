# encoding: utf-8
"""
@contact: lucky9322@163.com
@project: DimensConversion
@software: PyCharm
@file: calculator.py
@time: 2017/11/29 下午1:31

完成计算功能
"""

import io


class Calculator(object):
    def foo(self, s, scale):
        start_i = s.find('>')
        end_i = s.find('</')
        value = int(int(s[start_i + 1: end_i - 2]) * float(scale) + 0.5)
        return "%s%d%s" % (s[: start_i + 1], value, s[end_i - 2:])

    def operation(self, fileName, scale):
        result = ''
        with io.open(fileName, 'r', encoding='utf8') as file:
            for line in file:
                if '<dimen name="' not in line:
                    result += line
                else:
                    result += self.foo(line, scale)

        with io.open("dimens_output.xml", 'w', encoding='utf8') as file:
            file.write(result)



