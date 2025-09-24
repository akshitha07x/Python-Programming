# ERROR_HANDLING:
# TYPES OF EXCEPTION IN PYTHON :
# ZERO DIVISION METHOD :
# try :
#     a = int(input("Enter the numerator: "))
#     b = int(input("Enter the denominator: "))
#     c = a/b
#     print(c)
# except ZeroDivisionError :
#   print("enter: divisible by zero is not possible")
# try :
#   i=3
#   n=int(input("Enter the n value: ")) 
#   if n%n == 0 :
#    print("No, number is not multiple of", n)
#   else:
#    print("No, number's not multiple of", n)
# except ZeroDivisionError :
#   print("Error: Division is not multiple of", n)
  
# # VALUE ERROR :
# try:
#   rollno = int(input("Enter your rollno:"))
# except ValueError :
#   print("Error:Given value is not in the integer datatype.")
  
# # INDEX ERROR :
# try:
#   List =[10,20,30] 
#   print(List[5]) 
# except:
#   print("Error: The given index is not from the list.")

# #KEY ERROR:
# try:
#   Dict = {"name" : "Ak", "rollno":"M7"}
#   print(Dict["age"])
# except KeyError :
#  print("Error:The given key is not from the list.")
 
#  # TYPE ERROR :
# try:
#   List = [10,20,30]
#   Sum = List + 5
#   print(Sum)
# except TypeError:
#   print("Invalid type operation.")  
  
# NAME ERROR :
# try:
#   print(ak)
# except NameError:
#   print("Variable not declared.")

# FILE NOT FOUND ERROR :
# try:
#   file = open("detail.txt","r")
#   print(file.read())
# except:
#   print("file is not found in the system.")
# finally:
#   print("program is executed.")

