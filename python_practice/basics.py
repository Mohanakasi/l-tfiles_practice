d = {'a':10, 'b':20}
print(d['a'])
print(d.get('a'))
d.update(a=50)
print(d)
d.update(c=100)
print(d)
d.update({'d':1000})
print(d)
dict_ = dict.fromkeys(['a','ab','abc'], [8,2,3])
print(dict_)
print(d.popitem())
print(d.pop('c'))
a = {'a':10, 'b':500}
b = {'c':80, 'f':80}
# a = {1,2,3}
# b = {5,4,5}
# print({*a, *b})
print({*a, *b}) # unpacks only keys
print({**a, **b}) # unpacks keys and values
a = (1,2,3)
b = (4,5,6)
print(a+b)
# i = 1
# while i < 11:
#     print(i, end=' ')
#     i += 1

a = 1
b = 20
a,b = b,a
print(a)
print(b)