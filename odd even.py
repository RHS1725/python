num=int(input("enter num:"))

if num==0:
    print("neither odd nor even")
else:
    #if num % 2 ==0:
        #print("its even")

   # else:
        #print("its odd")
    print("even" if num%2 ==0 else "odd")