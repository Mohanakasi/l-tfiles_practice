# import threading
import time
from threading import *
"""creating threads without any class"""
# def display():
#     # print("executing by child thread:",current_thread().name)
#     for _ in range(5):
#         print("kasi knows python1")
# t = Thread(target=display) # creation of thread object
# # for target we have to intialize the the indepenent task
# t.start()
# """the below code executed by main thread"""
# # print("executing by:", current_thread().name)
# for i in range(5):
#     print('kasi knows python2')
#
# """getting child thread and main thread namnes"""
# def display():
#     a = 10
#     # print("child thread is:", current_thread().name)
#
# t = Thread(target=display)
# t.start()
# print("executing by:", current_thread().name)

"""creating thread using class"""
# class my_thread(Thread):
#     def run(self):
#         # print("run is called")
#         for _ in range(5):
#             print("child thread")
# t = my_thread()
# t.start()
# for i  in range(5):
#     print("main thread")
#
# class my_thread:
#     def display(self):
#         print(current_thread().name)
#         for _ in range(5):
#             print("kasi")
#
# t = my_thread()
# new_thread = Thread(target=t.display)
# new_thread.start()
# print(current_thread().name)
# for _ in range(5):
#     print("mohana")
#

# class abc:
#     def __display(self):
#         return 1008
#
#     def _college(self):
#         return "rvr&jc"
#     def kasi_id_details(self):
#         res = self.__display()
#         print(res)
# a = abc()
# a.kasi_id_details()
# # a.__display()
# print(a._college())

class my_data:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print("get method onvoked")
        return self.__name
    @name.setter
    def name(self, value):
        print("setter method invoked")
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name

e = my_data('kasi')
print(e.name)
e.name = 'mohana kasi'





