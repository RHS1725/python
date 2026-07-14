listq=[1,'baby',9.0,True]
listp=[10,2,6,9]
#lista=listq+listp
#print("the last elemnt:",len(lista*3))

#listp.append(3)
#listp.insert(2,"tri")
listq.append(listp)
print(listq)
print(listq.count('baby'))

listp.sort()
listp[2]=999
print(listp)
print(sum(listp))

