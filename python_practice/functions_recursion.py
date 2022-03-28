def nums_print(start, end):
    for num in range(start, end+1):
        print(num, end=' ')
# nums_print(1,50)
"""print 10 to 1 using for loop"""
def num_rev_print(start, end):
    for num in range(start, end-end, -1):
        print(num, end=' ')
# num_rev_print(10,1)
"""print -1 to -10 using for"""
def num_neg_print(start, end):
    for num in range(start, end-1, -1):
        print(num, end=' ')
# num_neg_print(-1,-10)
"""print even numbers using for loop"""
def even_nums(start, end):
    for num in range(start, end):
        if num%2 == 0:
            print(num, end=' ')
# even_nums(1,80)
"""print even characters in a string"""
def even_chars(s):
    for index in range(len(s)):
        if index % 2 == 0:
            print(s[index])
# even_chars('kasi')
"""to print the digits in a string using inbuilt method"""
def digits_string(s):
    for char in s:
        if '0'<= char <='9':
            print(int(char), end=' ')
# digits_string('Mohanakasi1995')
"""to count no of special characters in a string"""
def count_spe_Chars(s):
    count_ = len(s)
    for char in s:
        if char.isalpha() or char.isnumeric():
            count_ -= 1
    print(f"the number of special characters are {count_}")
# count_spe_Chars("Mohan@1995%2589 ")
# count_spe_Chars("kasi&^$$")
def prime_check(num):
    for i in range(2, num):
        if num % i == 0:
            print("not a prime")
            break
    else:
        print("prime")
# prime_check(8)
def prime_series(start, end):
    list_ = []
    for num in range(start, end):
        for i in range(2, num):
            if num %i == 0:
                break
        else:
            list_.append(num)
    return list_
# print(prime_series(50,100))
"""printing characters and its count of a string into dictionary uisng inbuilt method count"""
def dict_count(string_):
    def count_(char):
        return string_.count(char)
    d = {char:count_(char) for char in string_}
    return d
# print(dict_count("kasi is knows virtue kkkkkkkkkkkkkkkkkkkkkkk"))
from collections import defaultdict
def dict_count_dd(string_):
    dd = defaultdict(int)
    def count_(char):
        for char in string_:
            dd[char] += 1
        return dd[char]
    dict_ = {char:count_(char) for char in string_}
# print(dict_count('Kasi is King of Guntur KIng'))
"""printing characters and its count of a string into dictionary without using inbuilt method"""
def charscount(string_):
    dict_ = {}
    def count_(char):
        count_char = 0
        for char1 in string_:
            if char_ == char1:
                count_char += 1
        dict_[char_] = count_char
    for char_ in string_:
        count_(char_)
    return dict_
# print(charscount('Kasi is King of Guntur KIng'))
"""counting no words in a string and printing with word and count into  a dictionary 
using without inbuilt (if-else)"""
def words_count(string_):
    def count_(word):
        count_word = 0
        for word2 in words:
            if word == word2:
                count_word += 1
        return count_word
    words = string_.split()
    dict_ = {word: count_(word) for word in words}
    return dict_
# print(words_count("this is mohana kasi is from this state kasi"))
# print(words_count("k k k k k"))
# print(words_count('k l k l k l k l k l'))
"""printing words and its count of string into dictionary if the word is not repeated  in string"""
def count_words(string_):
    words = string_.split()
    word_count = lambda word:words.count(word)
    dict_ = {}
    for word in words:
        if word_count(word) == 1:
            dict_[word] = word_count(word)
    return dict_
# print(count_words("this is mohana kasi is is"))
"""printing first letter of a word in a string as key and that word as list of word"""
def dict_constr(string_):
    dict_ = defaultdict(list)
    for word in string_.split():
        dict_[word[0]] += [word]
    return dict_
# print(dict_constr("Mohana kasi is known of materal outer of the memorandam of the ketrogeon"))
"""swaping keys and values using items method"""
def key_value_swap(dict_):
    d = {}
    for key, value in dict_.items():
        d[value] = key
    return d
# print(key_value_swap({'name':'kasi','desig':'qa', 'sal':500000}))
"""to print fibonaci series upto n number"""
def fibo(n):
    first = 0
    second = 1
    while first <= n:
        print(first, end=' ')
        sum = first + second
        first = second
        second = sum
# fibo(50)
"""print fibonaci series in the user defined range"""
def fibo_series(nth):
    first = 0
    second = 1
    i = 1
    while i <= nth:
        print(first, end=' ')
        sum = first+second
        first = second
        second = sum
        i += 1
# fibo_series(20)
"""check whether the given no is a fibo number or not"""
def fibo_check(num):
    first = 0
    second = 1
    while first <= num:
        if first == num:
            return f"{num} is a fibonaci number"
        sum = first+second
        first = second
        second = sum
    else:
        return f"{num} is not a fibonaci number"

# print(fibo_check(89))
# print(fibo_check(45))
# print(fibo_check(55))

def sum_(*args):
    sum_all = 0
    for numeric in args:
        sum_all += numeric
    return sum_all
# print(sum_(1,25,2.5,48,16))

def temp_(**kwargs):
    print(len(kwargs))
    return kwargs
# print(temp_(kasi=2020, jmr=2020, meet=2022))

list_ = ['kasi','knows','python',2020]
def new_pack(*args):
    d = {word:len(word) if isinstance(word, str) else word for word in args}
    print(d)
# new_pack(*list_)
"""perfect square root"""
"2*2 = 4 --> 4 is perfect square root"
"10*10 = 100 ---> 100 is perfect sqaure root"
"7 * 7 = 49 ---> 49 is perfect sqaure root"
def perfect_square_check(num):
    for i in range(num+1):
        if i*i == num:
            return True
    return False
# print(perfect_square_check(49))

def func(string, i):
    if i == 0:
        print(string[1::2])
    elif i == 1:
        print(string[::2])
# func("tracxn",0)
# func("tracxn",1)
"to print a series of numbers using recursion (taking starting as default parameter)"
def num_series(end, start=0):
    if start <= end:
        print(start, end=' ')
        start += 1
        return num_series(end, start)
# num_series(50, 1)
"write a recursion program 10 to 1"
def num_series(start, end):
    if start >= end:
        print(start, end=' ')
        return num_series(start-1, end)
# num_series(10,1)
"write recursion function that prints even nubers in the range 10 to 50 "
def num_even_series(start, end):
    if start <= end:
        if start % 2 == 0:
            print(start, end=' ')
        return num_even_series(start+1, end)
# num_even_series(10,50)
"wa recursion function that checks each number in a list even or not if even print it"
def list_item_ev_check(list_, index=0):
    if index < len(list_):
        if list_[index] % 2 == 0:
            print(list_[index], end=' ')
        return list_item_ev_check(list_, index+1)
# list_item_ev_check([45,89,65,1,2,8,10])

# "write a recursion program to add the digits of a number"
def num_sum(number, index=0,count_=0):
    if index < len(str(number)):
        count_ += int(str(number)[index])
        return num_sum(number, index+1, count_)
    return count_
# print(num_sum(548))
"write a recursion program to reverse a stirng"
def string_rever(string_, index=0, res=''):
    if index < len(string_):
        res = string_[index] + res
        return string_rever(string_, index+1, res)
    return res
# print(string_rever('kasi is king'))
"wa recursion program to find the factorial of a number"
def facto_num(num, res=1):
    if num > 0:
        res *= num
        return facto_num(num-1, res)
    return res
# print(facto_num(5))
"write a recursion program to find the sum of first n numbers"
def sum_fir_n(n, sum=0):
    if n > 0:
        sum += n
        return sum_fir_n(n-1, sum)
    return sum
print(sum_fir_n(3))
"to check a number is prime or not using ecursion"
def prime_check(num, i=2):
    if i < num:
        if num % i == 0:
            return f"{num} is not a prime number"
        return prime_check(num, i+1)
    return f"{num} is a prime number"
# print(prime_check(123))
"using recursion to check whether the number is a fibo number or not"
def fibo_check(num, first=0, second=1):
    if first <= num:
        if first == num:
            return f"the {num} is a fibo number"
        sum = first + second
        return fibo_check(num, first=second, second=sum)
    return f"{num} is not a fibo number"
# print(fibo_check(7))
# print(fibo_check(55))
# print(fibo_check(90))
# print(fibo_check(89))

"using recursion to print fibo series up to n number"
def fibo_series_rec(n, i= 1, first=0, second=1):
    if i <= n:
        print(first, end=' ')
        sum = first+second
        return fibo_series_rec(n, i+1, first=second, second=sum)
# fibo_series_rec(10)

def sum(a:int, b:int):
    return a+b
# print(sum(1,2))







