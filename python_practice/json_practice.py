import json
"""the most commonly used messege format"""


"""serialization"""
"""the process of converting a python object into network supported form or file supported form"""

"""the process of converting one data structure into a linear format that can be transmitted over a netwok\n
is called as serialization"""
"""the process is also called as marshelling"""

"""de-serialiation"""
"""the process of converting stream of bytes back into data structure is called as de-serialization"""
"this is also called as unmarshelling"

"""json"""
"""json  is a light weight data format for data intercange"""
"""it is completely langauge independent"""
"""it is commonly used for client server communication"""
"""because it is humon readable"""
"""langauage independent"""

"""json serializing"""
"""the process of converting python object into json formated string"""
"""two methods were there"""
"""dump(object, file) ----> used for file objects"""
"""dumps(object) ---> used for any python object"""

"""json serealizing python object to json string"""
empl_ = {'name':'kasi','age':25,'sal':25000}
empl2_ = {'name':'rao','age':12, 'sal':45610}
json_string = json.dumps(empl_)
# print(json_string)
# print(dir(json_string))

"""json serialization from python file object to json file format"""
with open("empl.json", 'w') as j_file:
    json.dump(empl_, j_file)


"""json de-serialization"""
"""json string into python object"""
emp_dict = json.loads(json_string)
for key,value in emp_dict.items():
    print("{}:{}".format(key,value))

"""json file format into python object"""
with open("empl.json") as json_file:
    emp_dict = json.load(json_file)
    print(emp_dict)


from requests import request
res_ = request("get","https://www.amazon.in/")
print(res_.status_code)


"""pickle"""
import pickle
emp_data = {"name":'mohana', 'desig':'qa','sal':24563}
pick_form = pickle.dumps(emp_data)
print(pick_form) # in the form of binary

with open("kasi_new.pkl", 'wb') as pk_file:
    pickle.dump(emp_data, pk_file)

"""deserialization"""
"""pickle format to python object"""
em_da = pickle.loads(pick_form)
print(em_da)

"""pickle file format to python object"""
with open("kasi_new.pkl", 'rb') as p_file:
    e_data = pickle.load(p_file)
    for key in e_data:
        print(key, e_data[key])