a=5
b=10
print(a,b)

temp=a
a=b
b=temp 
print(a,b)

a,b=b,a
print(a,b)

a+=b
b=a-b
a-=b
print(a,b)

