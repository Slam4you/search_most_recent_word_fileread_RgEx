import re

with open("C:/Users/Slam/Documents/testhtml.html", "r", encoding='utf-8') as f:
    html= f.read()
print(html)
pattern ='<code>(.*?)</code>'


print(html.count('<code>'))
print(html.count('</code>'))
mlist = re.findall(pattern,html)
print(mlist)
for i in mlist:
    if mlist.count(i) > 3:
        print(i, ':', mlist.count(i))