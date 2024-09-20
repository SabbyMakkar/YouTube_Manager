print("Hello Sabby I love coffee")

def coffee(n):
    print(n)
coffee(4)

coffee("lemon tea")

coffee_one = "lemon coffee"
coffee_two = "Masala coffee"
coffee_three = "simple coffee"

# python in shell
# # >>> import sys
# >>> sys.platform
# 'win32'
# >>> import hello_coffee
# Hello Sabby I love coffee
# 4
# lemon tea
# >>>
# SyntaxError: invalid syntax
# >>> hello_coffee.coffee("mint tea") 
# mint tea
# >>> hello_coffee.coffee.coffee_oe  
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'function' object has no attribute 'coffee_oe'
# >>> hello_coffee.coffee.coffee_one
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'function' object has no attribute 'coffee_one'
# >>>  This error occurs because when we access this file in the terminal the coffee_one was not defined we wrote after it is running on terminal so byte code doesnt contains this lines of code you can get this lines by opening new terminal
# >>> from importlib import reaload
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: cannot import name 'reaload' from 'importlib' (C:\Users\samri\AppData\Local\Programs\Python\Python38\lib\importlib\__init__.py)
# >>> from importlib import reaload
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: cannot import name 'reaload' from 'importlib' (C:\Users\samri\AppData\Local\Programs\Python\Python38\lib\importlib\__init__.py)
# >>> from importlib import reaload 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: cannot import name 'reaload' from 'importlib' (C:\Users\samri\AppData\Local\Programs\Python\Python38\lib\importlib\__init__.py)
# >>> from importlib import reload  
# >>> this import relaod our files
# >>> reload(hello_coffee) 
# Hello Sabby I love coffee
# 4
# lemon tea
# <module 'hello_coffee' from 'D:\\coffee_aur_python\\01_basics\\hello_coffee.py'>
# >>> hello_coffee.coffee_one      
# 'lemon coffee'
# >>>
