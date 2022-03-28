""" use dictionary comprehension to create a dictionary with item and its index pair of any iterable"""
mesg = 'hello welcome to kasi world kasi is not there is in bangalore'
dict_pair = {item:index for index, item in enumerate(mesg.split())}
print(dict_pair)
""" use dictionary comprehension to create a dictionary with word and its length pair of a string"""
d_l_pair = {item:len(item) for item in mesg.split()}
# print(d_l_pair)
"""to create a dictionary with word and it's count pair (normal method)"""
d_w_count_pair = {word:mesg.split().count(word) for word in mesg.split()}
# print(d_w_count_pair)
"""use dictionary compre to create a dictionary with word and 
its count pair of string only if word is of even length"""
msg = 'this is kasi and is from python bangalore'
l_= msg.split()
n_w_count_pair = {word:l_.count(word) for word in l_ if len(word) % 2 == 0}
# print(n_w_count_pair)
""" use dict compre & take key as index and words as values if the word in a string is of odd lenth reverse it 
else keep as iti is"""
n_d_new = {index:word[::-1] if len(word) % 2 != 0 else word for index,word in enumerate(l_)}
print(n_d_new)
"""(using dict compre to create a dictionary with word and it's length psir if word is starting with vowel)"""
dict_vowels = {word:len(word) for word in l_ if word[0].lower() in 'aeiou'}
print(dict_vowels)
"""use dictionary compre to create a dictionary with index and item pair if the item is o string data type reverse it 
else keep it as it is"""
list_ = ['mohana kasi',True, bool, 1, 898, 1008, 'jmr','python']
dict_new = {index:item[::-1] if isinstance(item, str) else item for index,item in enumerate(list_)}
# print(dict_new)
"""use dict compre to create a dictionary with item and index pair if the item is o string data type keep it as it is 
else reverse it"""
list_ = ['mohana kasi',True,1, 898, 1008, 'jmr','python']
dict_new_d = {str(item)[::-1]:index if not isinstance(item, str) else index for index, item in enumerate(list_)}
# print(dict_new_d)
"""use dictionary comprehension to swaping keys and values of a dictionary"""
dict_new = {'name':'kasi','age':25,'number':8886213059}
dict_swap = {value:key for key, value in dict_new.items()}
# print(dict_swap)
# dict_swap = {dict_new[key]:key for key in dict_new}
# print(dict_swap)
string_ ='kasi'
char_dict_ = {char:ord(char) for char in string_}
print(char_dict_)
