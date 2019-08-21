import regex as re


fh = open("input.txt","r")



s=fh.read()

print (s)
t="year2019  and month augest and  date 20 and"

r3=re.findall("and",s)

print(r3.count('and'))

print(r3)
'''

t="year2019  and month augest and  date 20 and"
r1=re.findall(r"^\w",t)
print(r1)

r2=re.findall(r"^\d",t)
print(r2)

r3=re.findall("and",t)

print(r3.count('and'))
print(r3)'''