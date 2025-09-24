# DICTIONARY : It is a inbuilt function(datatype) which is used to store multiple values in a single variable.
# - It stores the data in the form of key-value pairs.
# EG : A = {"name : "AKSHITHA"}
#            key   -    value
# - Each key is unique and works as index to access it's corresponding value.
# - Keys are immutable(can't be changed once created) while values can be anything(mutable).
# SYNTAX :
# l = [10,20,30,40]
# t = (10,20,(30,40),50)
# my_dict = {
#     "key1":"value1",
#     "key2":"value2",
#     "key3":"value3",
#     "key4":"value4",
# }
# print(my_dict)

# CHARACTERISTICS OF A DICTIONARY :
# KEY - VALUE PAIRS : Every entry of a dictionary's elements is a pair : 
# A = {"n" : "AK", "n1" : "PK"}
# print(A)

# CREATING A DICTIONARY :
# NORMAL DICTIONARY
# BioData = {
# "Name" : "Navaneeth Akshitha",
# "Age" : "17",
# "Branch" : "CSE-AIML",
# "Section" : "D",
# "Roll No" : "25N31A66M7"
# }

# DICTIONARY USING CONSTRUCTOR :
# BioData1 = dict(Name = "Akshitha", Roll_No = "25N31A66M7",
# Branch = "CSE - AIML", Place = "Maisammaguda")
# # EMPTY DICTIONARY :
# E_D = {}

# ACCESSING THE DICTIONARY :
# BioData = {
# "Name" : "Navaneeth Akshitha",
# "Age" : "17",
# "Branch" : "CSE-AIML",
# "Section" : "D",
# "Roll No" : "25N31A66M7"
# }

# # SQUARE BRACKETS [] :
# print(BioData["Name"])
# print(BioData["Age"])
# print(BioData["Branch"])
# print(BioData["Section"])
# print(BioData["Roll No"])

# USING GET() METHOD :
# print(BioData.get("Name"))
# print(BioData.get("Age"))
# print(BioData.get("Branch"))
# print(BioData.get("Section"))
# print(BioData.get("Roll No"))

# ADDING AND UPDATING A DICTIONARY :
# BioData = {
# "Name" : "Navaneeth Akshitha",
# "Branch" : "CSE-AIML",
# "Section" : "D",
# "Roll No" : "25N31A66M7"
# }
# BioData["Age"] = 17
# print(BioData)
# BioData["Place"] = "PUNE"
# print(BioData)

# REMOVING IN DICTIONARY :
# pop(), pop item(), clear(), del(delete)
# BioData = {
#     "NAME" : "CHARLES LECLEREC",
#     "ROLL NO." : "217",
#     "BRANCH" : "FERRARI",
#     "PLACE" : "GERMANY",
#     "ROLE" : "F1 RACER"
# }

# BioData.pop("Roll NO.")
# print(BioData)
# BioData.popitem()
# print(BioData)
# del BioData["Branch"]
# print(BioData)
# BioData.clear()
# print(BioData)
# print(BioData.keys())
# print(BioData.values())
# print(BioData.items())
# BioData.update({"Role:" "ML ENGINEER", "Place": "China"})
# print(BioData)

# LOOPS IN DICTIONARY :
# for i in BioData:
    # print(i)
    
# LOOPS FOR DICTIONARY : 
# BioData = {
    # "NAME" : "ANUV JAIN",
    # "ROLL NO." : "20S",
    # "BRANCH" : "MUSICAL",
    # "PLACE" : "MUMBAI",
    # "ROLE" : "SINGER"
# }
# for i in BioData :
    # print(i)
# for i in BioData.keys():
    # print(i)
# for i in BioData.values():
    # print(i)
    
# NESTED DICTIONARY :
# Students = {
#    "S1":{"Name":"AKSHITHA","Roll no.":"M7"},
#    "S2":{"Name":"ATHARV","Roll no.":"L7"},
#  "S3":{"Name":"SHREYA","Roll no.":"N7"},
# }
# print(Students["S1"]["Name"])
# print(Students["S2"]["Name"])
# print(Students["S3"]["Name"])
# print(Students["S1"]["Roll no."])
# print(Students["S2"]["Roll no."])
# print(Students["S3"]["Roll no."])
