# TUPLES :
# Tuple is a collection datatype, which is used to store multiple values in a single variable. 
# Tuple is a ordered, immutable, it also allows the duplicate values. It can store mixed datatypes in values.
# Eg : coordinates("x","y")
# my_tuple = (10,20,30,40)
# print(my_tuple)
# print(type(my_tuple))

# CREATING A TUPLE :
# EMPTY TUPLE
# et = ()
# TUPLE WITH NUMBERS :
# N = (1,2,3,4,5,6)
# TUPLE WITH STRINGS :
# S = ("AK", "ATHARV","ANUV JAIN")
# TUPLE WITH MIXED DATATYPE :
# M = (24,3.14,"A","a")
# TUPLE WITH A SINGLE ELEMENT :
# a = 10
# print(type(a))
# b = [10]
# print(type(b))
# c = (10)
# print(type(c))
# d = (10,)
# print(type(d))

# ACCESSING ELEMENT :
# A = (10,20,30,40)
# print(A[0])
# print(A[1])
# print(A[2])
# print(A[3])
# print(A[-1])
# print(A[-2])
# print(A[-3])
# print(A[-4])

# SLICING : 
# A = (10,20,30,40)
# print(A[1:3])
# print(A[ :2])
# print(A[2:3])
# print(A[-3:-1])

# CHANGING THE VALUES :
# A = (10,20,30,40)
# A[1] = 50
# print(A)
# TypeError: 'tuple' object does not support item assignment  
# IT DOESN'T SUPPORT APPEND,REMOVE,POP,CLEAR.

# LENGTH:
# A = (10,20,30,40)
# print(len(A))
# print(max(A))
# print(min(A))
# print(sum(A))

# CONCATENATION :
# a = (10,20)
# b = (40,60)
# c = (a + b)
# print(c)

#REPETITION
# a = (1,2)
# n = int(input("enter n value: "))
# b = a*n
# print(b)

# SEARCHING AND CHECKING :
# A = (2,4,6,8,10,12,14,16,18)
# print(5 in A)
# if 2 in A:
#  print("YES, IT EXISTS.")

# INDEXING :
# A = (12,14,16,18,20)
# print(A.index(14))

# COUNT :
# A = (11,13,15,17,19)
# print(A.count(11))

# COPYING :
# a1 = ["A", "D", "C", "D", "D", "B" ]
# a2 = a1.copy()
# a2[2] = "B"
# print(a2)       ## LIST[] WORKS FOR COPYING BUT TUPLE() DOESN'T.

# ITERATING TUPLE USING FOR LOOP :
# A = ("BMW", "BUGGATI", "ROLLS ROYCE", "PORSCHE")
# for i in A:
#  print(A)

# NESTED TUPLE :
# T = (10,(20,30),(40,50))
# print(T[2][1])
