# FUNCTIONS :
# syntax:
# def function_name(parameters):
    # functions body code
# example :
# def greet():
    #print("hello world1")
# calling a function :
# def greet():
#     print("hello world")
# greet()
# # PASSING PARAMETERS AND ARGUMENTS :
# def greet(name):
#     print("Hello", name)
# greet("AK")
 # TYPES OF FUNCTIONAL ARGUMENT
 # A. POSITIONAL ARGUMENT :
# def greet(name,rollno):
#     print("Hello",name,"your rollno is", rollno)
#     greet("M7","AK")
 # B. KEYWORD ARGUMENT :
# def greet(rollno,name):
#     print("Hello",name,"your rollno is", rollno)
# greet(name="AK",rollno = "M7")

# DEFAULT ARGUMENT :
# def greet(name="Student"):
    # print("Hello", name)
# greet()
# greet(name="SHREYA")

# VARIABLE-LENGTH ARGUMENT :
# L = 10,20,30,40,50
# def sum1(*list1):
#     sum2 = 0
#     for i in range(len(list1)):
#         sum2 = sum2 + list1[i]
#     print(sum2)
#     print(type(list1))
# sum1(10,20,30,40,50)

# 2. *kwargs : KEYWORD VARIABLE-LENGTH ARGUMENT
# def details(**info):
    # for i,j in info.items():
        # print(i,":",j)
# details(Name = "AKSHITHA", Rollno = "M7", Branch = "CSM")

# SCOPE OF THE VARIABLE :
# x=10
# def var1():
#     x=5
#     print("inside var1 function", x)
# var1()
# def var2():
#     print("inside var2 function",x)
# var2()
# print("outside function",x) 

# LAMBDA FUNCTION :
# NORMAL FUNCTION :
# def sqe(a):
#     print(a*a)
# sqe(5)
# # LAMBDA FUNCTION :
# squ = lambda x:x*x
# print(squ(5))

