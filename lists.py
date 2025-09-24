#COLLECTION DATA TYPES
#LISTS
# list1 = [10,20,30,40,50] #integer datatype
# fruits = ["mango", "banana", "chiku"] #string datatype
# list2 = [10.1,20.2,30.3,40.4,50.5] #float datatype
# list3 = [True, False, True, True] #boolean datatype
# list4 = [10, 20.5, "hello", True,"False"] #multiple datatype
# #output
# print(list4)

# # ACCESSING ELEMENTS:
# # EXAMPLE :  0    1    2    3    4.....(n-1)
# list1 =  [10 , 20 , 30 , 40 , 50]
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])
# print(list1[4])
# # by negative values
# print(list1[0])
# print(list1[-1])
# print(list1[-2])
# print(list1[-3])
# print(list1[-4])

# # SLICING 
# slc1 = ["BMW", "PORSCHE", "MORRIS GARAGE", "ROLLS ROYCE"]
# print(slc1[1:2])

# # ADDING ELEMENTS IN LIST
# # APPEND
# list1 = [10,20,30,40,50]
# print(list1)
# list1.append(60)
# print(list1)
# # INSERT
# list1 = [10,20,30,40,50]
# print(list1)
# list1.insert(2,60)
# print(list1)
# # EXTENDING
# list1 = [10,20,30,40,50]
# print(list1)
# list1.extend([60,70])
# print(list1)

# # REMOVING ELEMENTS IN LIST
# # 1. remove():
# # 2. pop():
# # 3. clear():
# # remove()
# list1 = [10,20,30,40,50]
# print(list1)
# list1.remove(20)
# print(list1)
# #pop()
# list1 = [10,20,30,40,50]
# print(list1)
# list1.pop(3)
# print(list1)
# clear()
# list1 = [10,20,30,40,50]
# print(list1)
# list1.clear()
# print(list1)

# # CHANGING THE ELEMENTS:
# list1 = [10,20,30,40,50]
# list1[2]= 12
# print(list1)

# # MATHEMATICAL OPERATIONS IN LIST:
# # 1. concatenation
# a = [1,2]
# b = [3,4]
# c = [a+b]
# print(c)
# Repetition
# a = [1,2]
# n = int(input("Enter the n value"))
# b = a*n
# print(b)

#SEARCHING AND CHECKING:
# using in operator
#a = [2,4,6,8,10,12,14,16,18,20]
# print(3 in a)
# if 2 in a:
#     print("YES IT EXISTS.")
# #using not in operator
# print(3 in a)    

#index():
#print(a.index(8))

#count(): 
# a = [2,4,6,8,10,12,14,16,18,20]
# print(a.count(8))
# b = [2,4,6,8,8,8,10,12,14]
# print(b.count(2))
# cnt = 0
# print(b.count(8))
# for i in range(10):
#     b.append(i)
#     if i == 8:
#         cnt = cnt + 1
# print(cnt)

# #SORTING : sort()
# st = [25,12,5,31,13,18,7,45,8,55,68]
# # # #AO = 5,7,8,12,13,18,25,31,45,55,68
# st.sort()
# print(st)
# # st.reverse()
# print(st)
# st1 = [25,8,4,7,10]
# st1.sort(reverse=True)
# print(st1)

#COPYING THE LIST:
# a1 = ["A", "C", "D", "A", "D", "B", "B", "C", "C", "A", "A"]
# a2 = a1.copy()
# a2[2] = "B"
# print(a2)

# Built-in function with loops:
# a1 = [25,12,5,31,13,18,7,45,8,55,68]
# print(max(a1))
# print(min(a1))
# print(sum(a1))

# a = "hello world to the python programming"
# b = a.split()
# print(b)
# multiply values using input data to the list
# a = input("enter the multiple values:").split()

# multiply values using input data to the list : map()
# a = list(map(int,input("enter the multiple values:").split()))
# print(a)
# a.sort()

# b = (input("enter the multiple values:").split())
# print(b)

# TRANSVERING A LIST:
# cars = ["BMW", "PORSCHE", "MORRIS GARAGE", "AUDI"]
# for car in cars:
#     print("cars=" ,car)

# Using index with for loop:
# cars = ["BMW", "PORSCHE", "MORRIS GARAGE", "AUDI"]
# a = len(cars)
# for i in range(0,a):
#     print("cars",i,cars[i])
# print(len(cars)) 
    
# ADDING ELEMENTS USING FOR LOOP : 
# list1 = []
# n = int(input("enter the number of list values: "))
# for i in range(0,n):
#     a = input("enter the list values: ")
#     list1.append(a)
#     print(list1)

# GIVE THE INPUT VALUES TO THE LISTS FROM 0 TO 10 : 
# list1 = []
# n = int(input("enter n values: "))
# for i in range(0,100):
#     list1.append(i)
# print(list1)

# SUM OF LIST ITEMS = 10 20 30 40 50 WITHOUT USING SUM()
# list_sum = [10, 20, 30, 40, 50]
# total = 0
# for num in list_sum:
#     total += num
# print("Sum of list items:", total)

#CONVERT ["p", "y", "t", "h", "o", "n"] to python
# list1 = ["y", "t", "h", "o","n"]
# word = "p"
# for i in list1 : 
#     word = word+i
# print(word)
#        (OR)
# list1 = ["P","y", "t", "h", "o","n"]
# word = ""
# for i in list1 : 
#     word = word+i
# print(word)

# FIND THE MAXIMUM AND MINIMUM NUMBER FROM LIST WITHOUT USING MAX() AND MIN() :
# list1 = [7,18,12,17,20]
# list1.sort()
# print(list1)
# print("Maximum of list :", list1[4])
# print("Minimum of list :", list1[0])

# FIND THE MAXIMUM AND MINIMUM NUMBER FROM LIST WITHOUT USING MAX(), MIN() AND SORT() : 
# list1 = [7,18,12,17,20]
# max1 = list1[0]
# min1 = list1[0]
# for num in list1:
#     if num > max1:
#         max1 = num
#     if num < min1 :
#         min1 = num
# print(max1)
# print(min1)

# SEARCHING FOR AN ELEMENT IN A LIST : 
# Names = ["AK", "ANUV JAIN", "ARIJIT SINGH", "ATHARV"]
# searching_name = input("enter the name to be found : ")
# found = False
# for i in Names : 
#     if searching_name == i:
#         found = True
# if found :
#     print("YES")
# else :
#     print("NO")
    
# COUNT EVEN AND ODD NUMBERS : 
# list = [0,1,2,3,4,5,6,7,8,9]
# even_cnt = 0
# odd_cnt = 0
# for i in range(len(list)):
#     if list[i]%2 == 0 :
#         even_cnt += 1
#     else :
#         odd_cnt += 1
# print("Number of even numbers are: ", even_cnt)
# print("Number of odd numbers are: ", odd_cnt)

# REVERSING A LIST WITHOUT REVERSE : 
# list1 = [7,10,12,17,18,23,31,45,227,229]
# l = len(list1)
# r_list = []
# for i in range (l-1, -1, -1): 
#     r_list.append(list1[i])
#     print(r_list)

# REMOVING ALL NEGATIVE VALUES USING A LOOP :
# numbers = [-56, -9, 2, -8, -30, 45, 23, -19, 72, -55, -18, 7]
# positive_list = []
# for i in range (len(numbers)):
#     if numbers[i] >= 0:
#         positive_list.append(numbers[i])
#         print(positive_list)
        
# MULTIPLY EACH ELEMENT IN THE LIST : 
# numbers = [56,9,2,8,30,45,18]
# m = int(input("Enter the number to be multiplied : "))
# after_multiplication = []
# for i in numbers :
#     after_multiplication.append(i*m)
#     print(after_multiplication)
    
# WRITE A PROGRAM TO FIND THE AVERAGE OF ALL NUMBERS IN A LIST :
# list1 = [2,4,6,8,10,12,14,16,18,20]
# average = sum(list1) / len(list1)
# print("The average of the numbers in list1 is:", average)

# COUNT HOW MANY POSITIVES,NEGATIVES AND ZERO VALUES ARE IN THE LIST :
# n = [0,1,-3,-5,9,0,8,-6,52]
# positive_count = 0
# negative_count = 0
# zero_count = 0
# for i in range(len(n)):
#     if n [i] > 0:
#         positive_count += 1
# print("Number of positive numbers are:" , positive_count)
# for i in range(len(n)):
#   if n [i] < 0:
#     negative_count += 1
# print("Number of negative numbers are:" , negative_count)
# for i in range(len(n)):
#     if n [i] == 0:
#         zero_count += 1
# print("Number of zero numbers are:" , zero_count)
