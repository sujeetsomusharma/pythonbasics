# count = 1
# while count <=5:
#     print(count ,'hello')
#     count = count +1
    
# print(count)    


# i = 1
# while i <=10:
#     print(i*i)
#     i = i + 1
# print("EOC")

# n = int(input("Enter the value of table to be print : "))
# i = 1
# while i <=10:
#     print(n, "x", i, "=",n*i)
#     i = i + 1
# print("Table end")


# nums = [1,2,4,9,16,25,36,49,64,81,100,121,144,169,196,225]

# n = int(input("Enter the number you want to choose : "))
# i = 0
# while i < len(nums):
#     if(nums[i] == n):
#         print("Found the number : ", n, "at index number", i )
#         break
#     else:
#         print("Finding...")
#     i = i + 1
# print("Code end")

# nums = [1,2,4,9,16,25,36,49,64,81,100,121,144,169,196,225]
# n = int(input("Enter the number you want to choose : ")) 
# for i in nums:
#     print(i)
#     if(i == n):
#         print("Found the number : ", n )
#         break
#     else:
#         print("Number not found")
# print("EOC")

n = int(input("Enter the number upto which we need to sum the digits individually"))

sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1
print(sum)
        
        
        
        