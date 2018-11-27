from lxml import etree

html = etree.parse("./v30.xml")

print(type(html))

rst = html.xpath('//book')
print(type(rst))
print(rst)

#查找带有属性category的且值为sport的book元素
rst1 = html.xpath('//book[@category="sport"]')
print(type(rst1))
print(rst1)

rst2 = html.xpath('//book[price=30]')
print(rst2)

rst3 = html.xpath('//book[@category="sport"]/year')
print(rst3)
rst4 = rst3[0]
print(rst4)
print(rst4.tag)
print(rst4.text)