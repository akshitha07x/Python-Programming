# SETS : 
# Set is a collection of datatype which is used to store multiple values in a variable.
# Sets are unordered, unidexed, mutable and they don't allow duplicate values.
# They are useful when we want to store huge elements and performs the mathematical operations,
# Like Union, Intersection and Difference.
# SYNTAX :
# my_sets = {element1,element2,element3}

# CHARACTERISTICS OF SETS :
# UNORDERED :
# Eg : {1,2,3} and {3,2,1} are considered the same set.
# UNINDEXED :
#  you can not access set elements by the index like lists or tuples.
# a = {1,2,3}
# print(a[1])

# UNIQUE VALUES ONLY :
# Duplicate values are automatically removed from the set.
# a = {1,2,3,3,2,1,1,1,2}
# print(a)

# CREAING A SET :
# s1 = {1,2,3}
# s2 = {10,12.5,"HELLO", True}
# s31 = {}
# s3 = set()
# print(type(s3))

# ACCESSING SETS :
# We can't directly access an element using Index. We can access it using loops.
# A = {"TANJIRO KAMADO", "RENGOKU KYOJURO","TOMIOKA GIYU"}
# for role in A :
    # print(role)
    
# ADDING AN ELEMENT IN A LIST : 
# S = {12,18,20}
# S.add(25)
# S.update([34,29])
# print(S)
# DELETING AN ELEMENT IN A SET :
# #remove() :
# S ={34, 12, 18, 20, 25, 29}
# S.remove(25)
# print(S)

# DISCARD : 
# S ={34, 12, 18, 20, 25, 29}
# S.discard(26)
# print(S)
# S.pop()
# print(S)
# S.clear()
# print(S)

# MATHEMATICAL OPERATIONS IN A SET :
# UNION :
# A = {1,2,3}
# B = {4,5,6}
# print(A|B)
# INTERSECTION :
# A = {1,2,3,4,5}
# B = {4,5,6,7}
# print(A&B)

# DIFFERECE "-" = "-"
# A = {1,2,3,4}
# B = {3,4,5,6,7}
# print(A - B)
# print(B-A)

# SYMMETRIC DIFFERENCE :
# A = {1,2,3,4}
# B = {3,4,5,6}
# print(A ^ B)

# MATHEMATICAL OPERATIONS USING FUNCTIONS :
# A = {1,2,3,4}
# B = {3,4,5,6}
# 1. UNION
# print(A.union(B))
# 2. INTERSECTION
# print(A.intersection(B))
# 3. DIFFERENCE
# print(A.difference(B))
# 4. SYMMETRIC DIFFERENCE
# print(A.symmetric_difference(B))

# S = {1,2,3,4,5}
# print(len(S))
# print(max(S))
# print(min(S))
# print(sum(S))

