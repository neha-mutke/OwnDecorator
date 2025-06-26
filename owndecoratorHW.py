#create own decorator
#with argument

def neha_decorator(n):
    def wrapper():
        print("!!!!!!!!!!!!!!!   CONGRATULATION     !!!!!!!!!!!!!!!")
        print("******** You Have Created Your Own Decorator*******")
        n()
        print("@@@@@@@@@@@   AND LET'S END YOUR DECORATOR HERE    @@@@@@@@@@@")
        print("@@@@@@@ Have a BEST LUCK!! for creating another decorators. @@@@@@")
    return wrapper

@neha_decorator 
def name():
    print("                      NEHA                        ")

name()         


##without argument

def join_twostr(func):
    def wrapper(*a, **b):
        str1, str2 = func(*a, **b)
        add = str1 + str2
        print("Concatenated result:", add)
        return add
    return wrapper

@join_twostr
def strname(name):
    return "Hello, ", name + "!"


result = strname("Python")


  