'''
中文unicode案例
'''

import re

hello = '你好，世界'

pattern = re.compile(r'[\u4e00-\u9fa5]+')

m = pattern.findall(hello)
print(m)

he = 'abbbbbbccc'
pattern1 = re.compile('ab*')
m1 = pattern1.search(he)
print(m1.group())