import os

a = 'kasi'
# def samp():
#     global a
#     del a
# samp()
# print(a)
"""gloabla variables"""
"the variables which is present outside of the function"
"""the gloabla variables can be accessed in side the function and assigned with a new value in side the fynction but\n
when we want to increment it to some other vslue it raised to error to overcome this we use global keyword"""
a = 10
def temp_():
    global a
    a += 1
temp_()
print(a)

"""local variables"""
"""a variable which is created inside a function is called local variables"""
"""local variables cant be accessed out side a function"""
def samp():
    name = 'kasi'
    print(name.upper())
    name += 'jmr'
    print(name)
samp()

"""non local variables"""
"""the variables which are present outside a nested function those are called as non local variables"""
"""we can access these non local variables inside a nested function but we cant increment it to \n
do that we have to use nonlocal key word"""
def temp_():
    id_ = 1008
    name = 'mohana kasi'
    def samp_():
        nonlocal id_
        id_ += 1
        print(id_)
    print(id_)
    samp_()
temp_()

"""module"""
"""module is a file consists of python code"""
"the code can be of any type class functions, variables"

"""import"""
"""it is used to import the module and the specific class inside module or can import all the items inside modules"""
"""from"""
"""it is used to import the module when the module is present in the differenet packages"""
"""as"""
"""used to give alias name for the module imported as wel as functions too"""
import os as my_os
print(my_os.getcwd())
os.mkdir(r"C:\Users\Hp\PycharmProjects\l&t_practice\python_practice\kasi_temp\new_python_file.py")

