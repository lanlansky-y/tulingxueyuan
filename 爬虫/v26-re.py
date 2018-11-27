"""
search
"""

import re

s = r"\d+"

pattern = re.compile(s)

#和match一样，search后面也可以继续带参数，表示查找的起始范围
m = pattern.search("one12two34three56", 10, 40)
print(m.group())