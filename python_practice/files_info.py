# f  = open(r"my_data.docx", 'r')
import os
# print(os.getcwd())
# with open(r"D:\sample2.txt", 'w') as file:
#     print(file.closed)
#     print(file.mode)
#     print(file.name)
#     print(file.readable())
#     print(file.writable())
#     print(file.name)
# f =open(r"D:\sample2.txt",'w')
# print(f.mode)
# print(f.name)
# f.close()
# f.writable()


"""file reading"""
"""read()"""
"""reads entire data in the file"""
"""read line()"""
"""reads one line at a time"""
"""readlines()"""
"""reads all lines in the file and returns a list of lines"""
"""wap to count the no of lines in the file"""
path = r"C:\Users\Hp\PycharmProjects\Kasi_Python_TestYantra\my_files\text files\sindhu12.txt"
with open(path) as file:
    count_ = 0
    for line in file:
        count_ += 1
    # print(count_)
"""write a program print the line and line no in the file"""
with open(path) as file:
    count_ = 0
    for line in file:
        count_ += 1
        # print(count_, line)
"""write a program to count the no of words in the given file"""
with open(path) as file:
    count_ =  0
    for line in file:
        l = line.split()
        for word in l:
            count_ += 1
    # print(count_)
"""write a program to print the file from the last of the file"""
# with open(path) as file:
#     for line in reversed(list(file)):
#         print(line)
"""write a program to count the no of spaces in the given file"""
with open(path) as file:
    count_ = 0
    for line in file:
        if line.strip():
            count_ += line.count(' ')
    print(count_)
"""wap to count the no of words that are  starting with vowels"""
with open(path) as file:
    count_vow_words = 0
    for line in file:
        if line.strip():
            words = line.split()
            res_ = [word  for word in words if word[0].lower() in 'aeiou']
            count_vow_words += len(res_)
            # for word in words:
            #     if word[0].lower() in 'aeiou':
            #         count_vow_words += 1
    print(count_vow_words)
"""wap to create a dictionary with word and it's count pair in the given file"""
from collections import defaultdict
with open(path) as file:
    dict_ = defaultdict(int)
    for line in file:
        if line.strip():
            words = line.split()
            for word in words:
                dict_[word] += 1
    # print(dict_)
"""write a program extract all the ip adresses from the file"""
# with open(r"access-log.txt") as file:
#     l = []
#     for line in file:
#         if line.strip():
#             words = line.split()
#             l.append(words[0])
#     print(l)
"""to count the ip addresses"""
with open(r"access-log.txt") as file:
    dict_ = defaultdict(int)
    for line in file:
        if line.strip():
            ip_ = line.split()
            dict_[ip_[0]] += 1
    # print(dict_)
"""using counter class"""
from collections import Counter
with open(r"access-log.txt") as file:
    list_ = []
    for line in file:
        if line.strip():
            words = line.split()
            list_.append(words[0])
    ip_ = Counter(list_) # counts the each word and returns a dictionary
    # with word and it's count in decsending ordeer
    # print(ip_)
    # to print most common item
    print(ip_.most_common(5)) # you have to mention how many most common you need
    # if you not mention any it will return entire list

"""to print nth line in a file"""
n = 5
with open(path) as file:
    count_ = 0
    for line in file:
        count_ += 1
        if count_ == n:
            print(line)
            break
"""using islice"""
from itertools import islice
n = 10
with open(path) as file:
    line_ = islice(file, n, n+1)
    # print(*list(line_))
"""TO PRINT FIRST N LINES IN A FILE"""
n = 8
with open(path) as file:
    lines_ = islice(file, n)
    # print(*list(lines_))

"""to print last n lines"""
"""normal method"""
n = 5
with open(path) as file:
    count_ = 0
    list_ = []
    for line in reversed(list(file)):
        count_ += 1
        if count_ <= n:
            list_ = [line] + list_
    # print(*list_)

"using deque"
from collections import deque
with open(path) as file:
    lines_ = deque(file, n)
    print(*list(lines_))

"""write()"""
"""it will write the given data into the file"""
"""it will accept only string data type that too only one string"""
"""it will returns no of characters that are being added into the file"""
with open(path, 'a') as file:
    print(file.write("\n"))
    print(file.write("hai hello\n"))

"""write lines()"""
"""it will writethe given data into the file"""
"""it will accept a list data type , the list only contains string only"""
"""it will returns None"""
with open(path, 'a') as file:
    file.writelines(['mohana kasi\n', 'jmr\n','chandana\n'])
    file.writelines({'hai':12}) # it will take dictionary also but keys must be of string data type
