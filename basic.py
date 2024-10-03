# # # print("Hello Sujeet", "Kumar Sharma", "From LPU")
# # # print("College is in Jalandhar")

# # # name = "Dhoni"
# # # age = 41
# # # bid_price_of_csk = 15.50
# # # account_balance = -10

# # # print(type(name))
# # # print(type(age))
# # # print(type(bid_price_of_csk))
# # # print(abs(account_balance))


# # # print(5/3)
# # # print(5//3)

# # # print(not (age<40))
# # # print(not True)
# # # print(age != 43)
# # # print(float(age))

# # # # #val = input("Enter the val")
# # # # #print(val)

# # # # val1 = input(45)
# # # # print(val1)

# # # val2 = int(input("Enter the words"))
# # # print(val2)
# # # print(len(name))

# # full_name = "my name is Sujeet Kumar Sharma and my name is Sujeet"
# # print(full_name[11:len(full_name)])

# # print(full_name.endswith('ma'))  # it will give true/false
# # print(full_name.capitalize())
# # print(full_name.replace("Sujeet","Neha"))
# # print(full_name.find('e')) # it will give the index number
# # print(full_name.find("Sujeet")) # it will give the index number

# # print(full_name.count('e')) # it will give the count of the letter.
# # print(full_name.count('Sujeet')) # it will give the count of the word.  


# # str = input("Enter the Full name and the collge name \n")
# # print("The Name is :", str)

# # str_length = len(str)
# # print("The length of the name is : ", str_length)

# # count_the_occurance_of_letter = str.count('Sujeet')
# # print("The occurance of the letter 'Sujeet' : ", count_the_occurance_of_letter)

# # light = "pink"

# # if(light == "green"):
# #     print("go")
# # elif(light == "red"):
# #     print("Stop")
# # elif(light == 'orange'):
# #     print("Wait")
    
# # print("No Light availbale to check")

# # marks = [87, 64, 33, 95, 76]
# # print(marks[-3:-1])
# # marks.sort()

# # print(marks)

# # marks.sort(reverse=True)
# # print(marks)

# # tup = (1,3,3,2,5,2,)
# # print(tup.index(2))
# # print(tup.count(2))
# # movie = []
# # movie1 = input("Enter the movie name")
# # movie2 = input("Enter the movie name")
# # movie3 = input("Enter the movie name")

# # movie.append(movie1)
# # movie.append(movie2)
# # movie.append(movie3)

# # print(movie)

# # num1= [1,2,1]
# # num2= num1.copy()
# # num2.reverse()
# # print(num1)
# # print((num2))

# # if(num1 == num2):
# #     print("its a pllindomr")



# student = {
#     "name" : "Sujeet",
#     "age"  : 27,
#     "group" : {
#         "class_A" : "A",
#         "class_B" : "B",
#         "class_C" : "C"
#     },
#     "subject" : ['a','b','c'],
#     "marks" : (10,20,30,),
#     "age":34
# }
# print(student)
# print(type(student))

# print(type(student["name"]))

# student["surname"] = "Sharma"
# print(student)
# print(student["group"])
# print(student["group"]["class_B"])
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get("age"))
# print(len(student))
# print(list(student))
# print(list(student.keys()))

# print(len(list(student.values())))
# student.update({"location":"mohali"})
# print(student)

set1 = {1,2,3,4}
set2 = {4,5,6,7}

print(set1.union(set2))
print(set1.intersection(set2))