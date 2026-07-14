def hello():
    for i in range(5):
        print("helloworld")

    print("blah blah ")
hello()
hello()

def add():
    a=int(input("a:"))
    b=int(input("b:"))
    print(a+b)

add()
hello()
add()

def area_of_rectangle(b,h):
    return(b*h)


area=area_of_rectangle(7,9)
print(area)