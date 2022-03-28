import csv
"""reading csv files"""
"""csv.reader(csv_file)"""
"""it will reads data in a csv file each row in the form of list"""
"""that list containg each cell in row as a string including header"""


"""csv.DictReader(csv_file)"""
"""it will reads the data in csv file"""
"""it will reads the data in the form of dictionary"""
"""so each row in the file is a one dictionary"""
"""each cell in the row is a one string as value in the dictionary keys are respective header names"""
"""while reading through file using dict reader you no need to skip the header"""
"""and you no need to check hether row is empty or not"""

"""CSV.reader(csv_file)"""
path = r"C:\Users\Hp\PycharmProjects\Kasi_Python_TestYantra\my_files\csv_files\employees.csv"
# with open(path) as csv_file:
#     read_obj = csv.reader(csv_file)
#     next(read_obj) # it will skips the header
#     for row in read_obj:
#         if row:
#             print(row)

"""csv.DictReader(csv_file)"""
with open(path) as csv_file:
    read_obj = csv.DictReader(csv_file)
    for row in read_obj:
        print(row)

"""writing into csv files"""

"""csv.writer()"""

"""write row()"""
"""takes any iterable containing any data type"""
"""here each item in the iterable is a single cell value"""
"""it will write one row at a time"""
"""but each item is writes in a single line only that no item will writes down in a new line"""
with open("my_file.csv",'w') as csv_file:
    write_obj = csv.writer(csv_file)
    # write_obj.writerow("name") # writes the each character as a cell value
    # write_obj.writerow("age")
    # write_obj.writerow("salary")
    write_obj.writerow([('name','age','salary'),(1,2,3,('jmr')),(1,2,3)])
    # writes each item in the iterable as a  one cell value as a string data type that may be of any data type

"""write rows()"""
"""it will write the data into csv files"""
"""it will takes iterable of iterables as a input argument"""
"""it will write each iterable in the iterable as a one row in the csv file"""
"""and each item in the iterable as a one cell value """
with open("my_file.csv",'a') as csv_file:
    write_obj = csv.writer(csv_file)
    write_obj.writerows([(1,2,3),(4,5,6),(8,9,10)])


"""csv.DictWriter"""
"""it will writes the data into the csv file"""
"""it will takes input as a python dictionary"""

""" every time writing using dict reader you have to specify filed names in the write object creation"""
"""if you writing first time you  have to create header"""
"""if you not create that filed names the write row and write rows methods will not work"""

"""writerow()"""
"""it will write values given in the dictionary as a cell value in each row"""
"""keys must be same as filed names given in the write object creation"""
with open("dic_temp.csv", "w") as csv_file1:
    w_obj = csv.DictWriter(csv_file1,['name','age','sal'])
    w_obj.writeheader()
    w_obj.writerow({'name':'kasi','age':25, 'sal':25000})
    w_obj.writerow({'name':'mohana kasi','age':30, 'sal':245000})

"""write rows()"""
"""write rows will take a list of dictionaries"""
"""the values in the each dictionary is a cell values of each row"""
with open("dic_temp.csv", "a") as csv_file2:
    w_obj = csv.DictWriter(csv_file2,['name','age','sal'])
    w_obj.writerows([{'name':'kasi nadh','age':45,'sal':3000},{'name':'jmr','age':27,'sal':250000}])

path =r"C:\Users\Hp\PycharmProjects\Kasi_Python_TestYantra\my_files\csv_files\employees.csv"
# with open(path) as csv_file:
#     r_obj = csv.reader(csv_file)
#     next(r_obj)
#     for row in r_obj:
#         print(row)
"""write a program to print only the names having salary > 7000"""
# with open(path) as csv_file1:
#     r_obj = csv.reader(csv_file1)
#     next(r_obj)
#     for row in r_obj:
#         if row:
#             if int(row[3]) > 7000:
#                 print(row[0])

"write a program to group male and female candidate in employees file"
from collections import  defaultdict
dict_ = defaultdict(list)
with open(path) as csv_file:
    r_obj = csv.reader(csv_file)
    next(r_obj)
    for row in r_obj:
        if row:
            dict_[row[1]] += [row[0]]
    print(dict_)
"""write a program to group the employees based on their teams"""
dict_ = defaultdict(list)
with open(path) as csv_file:
    r_obj = csv.reader(csv_file)
    next(r_obj)
    for row in r_obj:
        if row:
            dict_[row[2]] += [row[0]]
    print(dict_)

