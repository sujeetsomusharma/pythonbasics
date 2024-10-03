# # file to read from the database    

# # f = open("demo.txt") # by default the mode is read
# #f = open("demo.txt", "r")
# # by default the file i.e. "t" files are read and if other than text files we need to combine the mode with the the filename.
# # example -> f = opne("demo.txt","rt")

# # mode r is for the reading of the file
# # mode w is for the writing of the file
# # mode b is for the binary mode
# # mode a is for open files and write files appended to the last if file exists
# # mode t is for the text(by default)
# # mode '+' opens a disk file for updating (rading and writing)
# # mode x to create a new file

# # data = f.read(5) # read the data from the file some specific characters
# # data = f.read() # read the whole data from the file.
# # print(data)
# # print("The lenght of the data is : ",len(data))

# # line1 = f.readline() # read the line from the file
# # print(line1)
# # print("The lenght of the data is : ",len(line1))
# # f.close()
# # reading the data from the file

# # replacing the data in demo.txt file with new data using "w" mode. In "w" mode the data of the file will be overwritten. In "w" mode if the file does not exist then the new file will be created.

# # z = open("sample.txt","w")
# # z.write("I have done my graduation")
# # z.close()

# # # add the data to the sample file by using the append mode "a" and if does not exist then the new file will be created as same as in write mode.

# # x = open("sample.txt","a")
# # x.write("\nI am in the field of AI")
# # x.close()


# # open the file "with" and in this using with aliasing is being used to access the file. We do not need to specify the close as with "with" keword file is automatically closed.

# # with open("sample.txt","r") as f:
# #     data = f.read()
# #     print(data)

# # with open("sample.txt","w") as f:
# #     data = f.write("\n This is MS Dhoni house as CSK")


# # delete the  using the OS module
# import os
# os.remove("sample.txt") # remove the file


# Question  - creat a new file "practice.txt" suing python. Add the following data in it :
# Hi Everyone 
# we are learning python 
# using VS Code editior 
# I Like python programming language 
# WAP to replace all occurance of "JAVA" with "Python" in the above file and search if the word "learnig" exists in the field.
 

# with open("practice.txt","w") as f:
#     f.write("Hi Everyone \n")
#     f.write("we are learning Java \n")
#     f.write("using VS Code editior \n")
#     f.write("I Like Java programming language \n")
    
with open("practice.txt","r") as f:
    data = f.read()
    print(data)
    

new_data = data.replace("Java", "python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)


search_words = "learning"

with open("practice.txt","r") as f:
    search_data = f.read()
    data = search_data.find("learning")
    if(data == "learning"):
        print("The word 'learning' exists in the file")
    else:
        print("The word 'learning' does not exists in the file")
       
    




