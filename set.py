set1={1,2,7,5,7}
set2={7,8,5,4}
set3={99,100,101}
print(set1)
set1.add(99)
set1.add('99')
print(set1)
set1.remove(1)
print(set1)

print(set1.union(set2))
print(set1.difference(set2))

print(set1.union(set2).difference(set3))