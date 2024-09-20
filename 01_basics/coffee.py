from hello_coffee import coffee

coffee("ginger tea")

# when we import a file called __pycache__ automatically gets installed


# behind the scenes

# a. when we create a python program we need python software or interpretor to run our python program
# b. then we write our script or python program 
# c. when we run our program our code was converted into the BYTE code in most cases its hidden but when we use something like import byte file is visible like in our upper case byte code file pycahe is created
# d. after BYTE code when we install python software one more thing is installed that is python VM on this our code which is converted into byte code is actually run on this VM


# 1. Compile to BYTE code but it doesnt means its compile level language
# 2. Byte code is low level code platform independent code
# 3. Byte code runs faster
# .pyc is compiled pyhton called frozen binarics
# __pycache__: when we create this froen binarics we make lot of changes so we dont make this file again and again so pyhton make us a system folder to save all the coming new version and changes made in the files
# when we see __<file-Name>__ its means that file is important for python like in above case __pycache__ which stores all the changes thats why there are files which has many inportance 
# SOURCE CHANGE && PYTHON VERSION : hello_coffee.cpyhton-38.pyc
# source change is hello_Coffee: pyhton uses many differeniating factor which means the changes we make in our file it compares our previous changes to the new changes in the file using many factor bheind
# .cypthon-38 : means 38 is its version because its version is important for pyc byte code file
# these file is only created in imported fikes not for top level file
# 
# 
# 
# 
# 
# pyhon VM:
# PVM : software in which loop is there in which we feed our file its gets executed
# thats why its called INTERPRETOT language because it run line by line in loop in our PVM
#  we can also give our files directly instead of byte code file thats why byte code file is not generated for all the files

# PVM is runtime engine 
# Byte code is NOT a machine code
# machine code is direct instrunction to the hardware but byte code is not a direct instrunction to the hardware
# byte code is python specific we cant use JVM to run this
# cpython we uses this in most cases there is jyphton , Ironpyhton , stackess , pypy

# python in shell
# PS D:\coffee_aur_python\01_basics> python
# Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32Type "help", "copyright", "credits" or "license" for more information.
# >>>
# >>> 
# >>> print("coffee")
# coffee
# >>> 2*2            
# 4
# >>> 3+5
# 8
# >>> "coffee "*4
# 'coffee coffee coffee coffee '
# >>> score = 101
# >>> score 
# 101
# >>> tea
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'tea' is not defined
# >>> import os
# >>> os.getcwd()
# 'D:\\coffee_aur_python\\01_basics'
# >>> for c in "coffee":
# ... print(c)
#   File "<stdin>", line 2
#     print(c)
#     ^
# IndentationError: expected an indented block      
# >>> for c in "coffee":
# ...       print(c)
# ...
# c
# o
# f
# f
# e
# e
# >>> import sys
# >>> sys.platform
# 'win32'
# >>>     



# Mutable and Imutable in Python

# >>> username ="Sabby"
# >>> username         
# 'Sabby'
# >>> username ="coffee"
# >>> 
# >>> username
# 'coffee'
# >>> x = 10
# >>> y = x
# >>> x
# 10
# >>> y
# 10
# >>> x = 15
# >>> y
# 10
# >>> 

# one memory box is allocated called username 
# in python user doest directly points to username 
# python everything is object

# memory reference is made its name is Sabby this is object
# value ka reference  create hota hai when we write coffee uska bhi alag is box bana tha
# username first points to sabby when we change the value we dont actually chaged the we just points to different Block
