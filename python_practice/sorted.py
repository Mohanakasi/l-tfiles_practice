"""sorted"""
"""returns a new list from the items in the iterable"""
"""it has one mandatory and two optional arguments"""
"""iterable is first nad madatory argument"""
"""key and reverse are the optional argumnents"""
"""key specifies a function that is used to extract comparison key from the each item in the iterable"""
"""reverse is the boolean value by default it is set to False that means whe it is in False\n
by default the items are sored in ascending order when it is set ot True the items ill xorted in descending order"""
"example"
list_ = ['mohana kasi','chandana','jmr']
res_ = sorted(list_) # sorts based o the ascii values present inside the list_
# print(res_)
list_ = [80,1008,1,26,0,45,1,321,10000,12,26]
res_ = sorted(list_) # sorts based on the number order
# print(res_)
res_ = sorted(list_, reverse= True)
# print(res_)

string_ = 'mohana kasi jmr chandhana'
res_ = sorted(string_)
# print(res_)

dic_ = {'name':'kasi','love':'jmr','friend cum love': 'Chandana'}
res_ = sorted(dic_) # sorts based on ascii value of the keys
# print(res_)

dic_ = {1008:'kasi',1006:'jmr',1009:'chandana'}
res_ = sorted(dic_) # sorts based on key number order
# print(res_)
# print(sorted(dic_, key = lambda key: dic_[key])) # sorts based on values

"""write a program to sort the elements present inside list based on their length"""
l = ['python','javva','c','ruby','paul']
# print(sorted(l, key=len))

"""write a program to find the largest and shortest word in the following string"""
string_ = 'python is a programming language'
# res_ = sorted(string_.split(), key = len)
# print("longest word--->", res_[-1])
# print("shortest word--->", res_[0])
# short,*res,long = res_
# print(short, long)
"""write a program to sort the below list based on the first character of the each element"""
l = ['python','javva','c','ruby','paul']
res_=  sorted(l, key = lambda string_:string_[0])
# print(res_)

"""write a program to sort the dictionary based on the keys last item"""
d = {'ymail':8, 'apple':3, 'fruit':4}
res_ = sorted(d, key = lambda key_: key_[-1])
# print(res_)
"""taking d.items()"""
res_ = sorted(d.items(), key = lambda item: item[0][-1]) # sorts based on key last item and return both key and value
# print(res_)

"""write a program to sort the dictionary based on the values"""
d = {'ymail':8, 'apple':3, 'fruit':4}
res_ = sorted(d.items(), key = lambda item:item[-1])
# print(res_)
res_ = sorted(d.values()) # it will return only vslues
# print(res_)

"""write a program to get the most repeated word"""
sentence = "hai hello hai who is hello there hai hai hai"
dict_count = {word: sentence.split().count(word) for word in sentence.split()}
print(sorted(dict_count.items(), key = lambda item:item[-1])[-1])

"""write a program to print the longest word with it's length"""
string_ = 'hai mohana kasi how is your python programming'
dict_ = {word:len(word) for word in string_.split()}
print(sorted(dict_.items(), key= lambda item:item[-1])[-1])

"""write a program to print longest non repeted word"""
string_ = 'hai mohana kasi how is your python kkkkkkkkkkkk kkkkkkkkkkkk programming'
dict_ = {word:len(word) for word in string_.split() if string_.split().count(word) == 1}
res_ = sorted(dict_.items(), key=lambda item:item[-1])
print(res_[-1])

