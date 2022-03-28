import time
from time import sleep
from requests import request
from selenium import webdriver
# driver = webdriver.Chrome(".\chromedriver.exe")
"""log decorator"""
def samp(func):
    def wraper(*args, **kwargs):
        print(f"welcome to {func.__name__}")
        func(*args, **kwargs)
    return wraper
@samp
def hdfc_bank(user_name, password):
    print(user_name)
    print(password)
# hdfc_bank('kasi','Kasi@1994')
@samp
def flipkart(search_item):
    print(search_item)
    print(search_item,"has been added to cart")

# flipkart('shoes')


"""delay decorator"""
def new_deco(func):
    def wrapper(*args, **kwargs):
        sleep(5)
        return func(*args, **kwargs)
    return wrapper

@new_deco
def link_check(link):
    res_ = request("get",link)
    return res_.status_code
# print(link_check(r"https://www.amazon.in/"))
# print(link_check(r"https://digitalseva.csc.gov.in/"))

"""caluculating execution time of a function"""
def ex_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"execution time of the {func.__name__} id {end-start}")
    return wrapper
@ex_time
def get_site(site_link, xpath):
    driver.get(site_link)
    driver.maximize_window()
    sleep(10)
    driver.find_element_by_xpath(xpath).click()
    sleep(10)
# get_site("https://digitalseva.csc.gov.in/", "//strong[text()=' Login']")
# sleep(5)
# get_site("https://www.amazon.in/","//input[@id='twotabsearchtextbox']")

"""positive decorator"""
def pos_deco(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 0:
            return abs(result)
        return result
    return wrapper
@pos_deco
def sub(a, b):
    return a-b
print(sub(10,50))
print(sub(50,60))
print(sub(50,40))


"""repeat the function n times"""
def n_time_ex(n):
    def samp_(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"{func.__name__} is executed {i+1} times")
                func(*args, **kwargs)
        return wrapper
    return samp_

@n_time_ex(5)
def upper(string_):
    print(string_.upper())

upper('MOhana kasi is from Guntur')

"""counting number of function calls"""
def count_fun_calls():
    count_fun_calls.count = 0
    def temp(func):
        def wrapper(*args, **kwargs):
            count_fun_calls.count += 1
            func(*args, **kwargs)
        return wrapper
    return temp
@count_fun_calls()
def login():
    print("welcome to login")

login()
login()
login()
print(count_fun_calls.count)
login()
print(count_fun_calls.count)
"""decorator to prefix the +91 before the number"""
