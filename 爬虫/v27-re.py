'''
findall案例
'''

import re

pattern = re.compile(r'\d+')

s = pattern.findall('i am 18 years old and 180 high')

print(s)

s1 = pattern.finditer('i am 18 years old and 180 high')
print(s1)
print(type(s1))
for i in s1:
    print(i.group())