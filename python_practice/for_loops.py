list_ = ['kasi','rao',1234]
# for item in list_:
# #     if isinstance(item, str):
# #         print(item[::-1])
# #     print(item)
# list_2 = [1,8,1008,420,654,1008]
# ele = 1008
# for item in list_2:
#     if item == ele:
#         print(list_2.index(ele))
#         break
# for index, item in enumerate(list_2):
#     if item == ele:
#         print(index, item)
#         break
# """write a program to print all the lements other than element given"""
# list_2 = [1,8,1008,420,654,1008]
# ele = 1008
# # for item in list_2:
# #     if item != ele:
# #         print(item, end=' ')
# # for item in list_2:
# #     if item == ele:
# #         continue
# #     print(item, end=' ')
# """write a program to remove given element from the set"""
# set_ = {1,2,3,48}
# ele_ = 2
# set_.discard(ele_)
# set_ = {1,2,3,48}
# for key in set_:
#     if key == ele_:
#         set_.discard(key)
#         break
# print(set_)
# a = [1,2,3,4]
# b = [8,6,8,9,456,89]
# for item in zip(a,b):
#     print(item)
# from itertools import zip_longest
# for item in zip_longest(a,b):
#     print(item)
#
# string_meseg = 'this is mohana kasi is is is is'
# d = {}
# words_ = string_meseg.split()
# for word in words_:
#     d[word] = words_.count(word)
# print(d)
# dict_ ={}
# for word in words_:
#     if word not in dict_:
#         dict_[word] = 1
#     else:
#         dict_[word] += 1
# print(dict_)
# from collections import defaultdict
# dict_2 = defaultdict(int)
# for item in words_:
#     dict_2[item] += 1
# print(dict_2)
#
# string_ = 'this is python language is is python'
# dict_3 = {}
# for word in string_.split():
#     dict_3[word] = len(word)
# print(dict_3)
# dict_4 = {}
# for word in string_.split():
#     if len(word) % 2 == 0:
#         dict_4[word] = len(word)
# print(dict_4)
# dict_5 = {}
# for item in string_.split():
#     if item[0].lower() in 'aeiou':
#         dict_5[item] = len(item)
# print(dict_5)
#
# dict_ = {'id':1008, 'username':'Mohana kasi108', 'desig':'qa'}
# for key in dict_:
#     if isinstance(dict_[key], str):
#         dict_[key] = dict_[key][::-1]
# print(dict_)
# """WRITE A PROGRAM TO GET ALL THE DUPLICATE ITEMS AND NO OF TIMES THAT IS REPEATD IN THE LIST"""
# list_ = ['kasi',1008,'kasi','rao','abc', 1008, 'reg', 'abc']
# dict_ = defaultdict(int)
# for item in list_:
#     if list_.count(item) > 1:
#         dict_[item] += 1
# print(dict_)
#
# dict_ = {'id':1008, 'username':'Mohana kasi108', 'desig':'qa'}
# d = {}
# # for key, value in dict_.items():
# #     d[value] = key
# # print(d)
# for key in dict_:
#     d[dict_[key]] = key
# print(d)
#
# """ to print alternate items in a list (odd) """
# list_od_el = ['kais',108, 45, 'rao']
# # for item in list_od_el[1::2]:
# #     print(item)
# """ to print alternate items in a list  (even) """
# # for item in list_od_el[::2]:
# #     print(item)
# # for index in range(len(list_od_el)):
# #     # if index % 2 ==0:
# #     #     print(list_od_el[index])
# #     if index % 2 != 0:
# #         print(list_od_el[index])
#
# """print even length items in a list using inbuilt function"""
# list_ele = ['kasi','mohana','python','king','and','had']
# for item in list_ele:
#     if len(item) % 2 == 0:
#         print(item)
# for item in list_ele:
#     count_ = 0
#     for char in item:
#         count_ += 1
#     if count_ % 2 == 0:
#         print(item)

"""checking index of first occurence of a number in list (without suing nbuilt method)"""
lsit_ = ['kasi','is','from',1,2,8,1,60]
# num = 1
# for index in range(len(lsit_)):
#     if lsit_[index] == num:
#         print("index is","-->",index, "item is --->",
#               lsit_[index])
#         break

# num  = 45
# for i in range(2,num):
#     if num % i == 0:
#         print("not a prime")
#         break
# else:
#     print(f"{num} is a prime")

# list_= []
# for num in range(2,50):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         list_.append(num)
# print(list_)
"""wap to print strings in list which are of even length using list comprehension"""
list_2 = ['rao','python','and','is this fine']
new_list = [item for item in list_2 if len(item) % 2 == 0]
# print(new_list)
"""wap to print strings in the list if the string is of even lenth keepit as it is if it is odd lenth reverse it
using list comprehension"""
list_2 = ['rao','python','and','is this fine']
newlist_ = [item if len(item) % 2 == 0 else item[::-1] for item in list_2]
# print(newlist_)
"""wap to print all the palindrome in a list using list comprehesnion"""
list_pals = ['mom','dad','king','kasi']
new_list_pals = [item for item in list_pals if item == item[::-1]]
print(new_list_pals)
''"""print list having powers of each element of another list"""''
list_ps = [1,8,9,25]
new_list_ps = [item**2 for item in list_ps]
print(new_list_ps)
"""to print a list having tuple of index and item using list comprehension"""""
list_ = ['mohana kasi', 'guntur', 'jmr']
new_list_item = [(index, item) for index, item in enumerate(list_)]
# print(new_list_item)
"""creating list of even no's using list comprehension"""
list_evens = [num for num in range(1,50) if num % 2 == 0]
# print(list_evens)
"""   if word is of even append into list else is if word lenth is odd reverser it """
list_ = ['mohana kasi', 'guntur', 'jmr']
new_list_5 = [item if len(item) % 2 == 0 else item[::-1] for item in list_]
# print(new_list_5)
"""if item in a list is string keep it as it is else reverse that item"""
l_new = ['king kasi','jmr',4265, 1.8456, 'janardhana', (50+50J), True]
n_list = [item if isinstance(item, str) else str(item)[::-1] for item in l_new]
# print(n_list)
"""create a list having words starting with owel (using list comprehension)"""
l_words = ['mohana kasi', 'user_name','is','correct','and','effective','on']
# n_v_words = [item for item in l_words if item[0].lower() in 'aeiou']
# print(n_v_words)
"""tuple of index and item using enumewrate"""
li_ = ['kasi','mohana','king']
new_set = {(item, index) for index, item in enumerate(li_)}
# print(new_set)
"""use set comprehension  to create a set of tuples having item and it's index pair of list using range()"""
li_ = ['kasi','mohana','king']
n_se = {(index, li_[index]) for index in range(len(li_))}
# print(n_se)
"""set comprehension to create a set with even items present in a list"""
li_val = ['kasi','king','mohana kasi',1008,'nanglaore']
n_set_ev_i = {item for item in li_val[::2]}
# print(n_set_ev_i)
"""set comprehension to create a set with even items present in a list (unsing range())"""
li_val = ['kasi','king','mohana kasi',1008,'nanglaore']
n_set_ev_items = {li_val[index] for index in range(len(li_val)) if index % 2 == 0}
# print(n_set_ev_items)
"""set comprehension to create a set with if the item has even length keep it as its else reverse it"""
l_ = ['king', 'together','please','jointhe']
# n_s_it = {item if len(item) % 2 == 0 else item[::-1] for item in l_}
# print(n_s_it)
"""set comprehension to 
create a set with if the item has even length keep it as its else reverse it (using range)"""
l_ = ['king', 'together','please','jointhe']
n_set_8 = {l_[index] if len(l_[index]) % 2 == 0 else l_[index][::-1] for index in range(len(l_))}
# print(n_set_8)
# set comprehension to create a set with if the item string  keep it as its else reverse it
l_items = ['kasi',123,50+50j,True, 'rao']
b_s_is = {item if isinstance(item, str) else str(item)[::-1] for item in l_items}
# print(b_s_is)


