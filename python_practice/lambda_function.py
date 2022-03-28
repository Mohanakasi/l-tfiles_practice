"""write a lambda expression that checks the given no is even or not"""
ev_check = lambda num: num % 2 == 0
print(ev_check(3))
"""write a lambda expression that multiplies two numbers"""
mul_nums = lambda num1, num2: num1 * num2
# print(mul_nums(10,30))
"""write a lambda expression that return last elemts of the sequence"""
las_el = lambda seq: seq[-1]
# print(las_el([1,2,3,'jmr']))
"""write a lambda function that checks if the string is palindrome or not"""
pal_check_lam = lambda string: string == string[::-1]
# print(pal_check_lam('mom'))
# print(pal_check_lam('dad'))
# print(pal_check_lam('kasi'))
"""lambda expression to check string is of even length and string stars with vowel"""
string_checks = lambda string_: len(string_) % 2 == 0 and string_[0].lower() in 'aeiou'
# print(string_checks('kasi'))
# print(string_checks('userid'))

"""wap to convert all the strings in the list to upper case using map"""
upper_conv = map(lambda string: string.upper(), ['kasi', 'chandana','jmr'])
# print(list(upper_conv))
"""wap to convert allthe negeative numbers into positive using map"""
neg_pos = map(lambda num: abs(num), [1,2,3,-1,-458,30,-12])
print(list(neg_pos))
"""write a map function that return a list of even numbers inside a list using map"""
def even_num_check(num):
    if num % 2 == 0:
        return num
res = map(even_num_check, [1,87,2,45,36,97])
# print(list(res))
"""write a map function that takes two lists and return sum of each element"""
sum_list_ = map(lambda item1, item2: item1+item2, [1,2,3,4],[1,4,5,6])
# print(list(sum_list_))
'''write a map function that returns the  numeric data present  inside the list, tuple, set, and dictionary '''
def numeric_check(item):
    if isinstance(item, int):
        return item
res_ = map(numeric_check, [1,2,3,'kasi',{1,2,3}])
print(list(res_))
"""write a map function that returns the strings having even lenth present inside a list"""
def eve_string(string_):
    if len(string_) % 2 == 0:
        return string_
res_ = map(eve_string, ['kasi','jmr','chandana'])
# print(list(res_))
""""write a map function to create a dictionary of word and it's count pair in the following sentence"""
def word_count(word):
    return word,words.count(word)
string_ = 'mohana kasi loves jmr kasi like chandhana too'
words = string_.split()
res_ = map(word_count, words)
# print(dict(res_))
"""write a map function that returns the list of numbers raised to the power of their indices using map"""
res_pows = map(lambda args: args[1] ** args[0], list(enumerate([1,2,3,8])))
# print(list(res_pows))
"""filter out the even values in the list"""
def even_check(num):
    if num % 2 == 0:
        return num
res_ = filter(even_check, [1,2,4,8,7,6,3,21])
# print(list(res_))
"""write a program that returns a list of strings with odd length using filter function"""
odd_strings = filter(lambda string: len(string) % 2 != 0, ['kasi','jmr','chandana','loves'])
# print(list(odd_strings))
'''write a function that returns only the  numeric data present  inside the list, tuple, set, and dictionary '''
def data_type_check_num(item):
    if isinstance(item, (int, float, complex)):
        return item
res_ = filter(data_type_check_num, [1,2,3,'kasi','chandana','jmr',50+50j,True])
print(list(res_))
"""write a  function that returns only the strings which having even lenth present inside a list"""
def str_len_check(string_):
    if len(string_) % 2 == 0:
        return string_
res_ = filter(str_len_check, ['kasi','chandana','jmr','loves'])
print(list(res_))
"""write a function to returns only the words starting with vowels"""
res_ = filter(lambda word:word[0].lower() in 'aeiou', "kasi loves jmr and likes chandana too".split())
print(list(res_))