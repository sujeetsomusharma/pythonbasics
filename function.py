# def add(a,b):
#     sum = a+b
#     print(sum)
# add(4,9) 


# def return_fun(a,b): # function definition
#     return a + b

# sum_return = return_fun(10,3) # function calling
# print(sum_return)

# def hello_print():
#     print("Hello")

# hello_print()

# def hello_return():
#     print("Hello_Return")

# value_of_hello_return = hello_return()
# print(value_of_hello_return)

# def cal_avg(a,b,c,d,e):
#     avg = (a+b+c+d+e)/5
#     return avg
# final_avg = cal_avg(67,90,78,99,99)
# print(final_avg)


# my_list = []

# my_list.append("Sujeet")
# my_list.append("Kumar")
# my_list.append("Sharma")

# print("The final items in the list are after inserting :", my_list)

# def list_len(list_len):
#     print("The items in list are : ", list_len)
#     return len(list_len)

# list_lenght = list_len(my_list)
# print(list_lenght)

# n = int(input("Enter the number to find the factorial : "))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# print("The factorial of", n, "is", factorial(n))


# n = int(input("Enter the number to find the factorial : "))

# def cal_factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact

# factorial_value = cal_factorial(n)
# print("factorial_value", factorial_value)

# n = int(input("Enter the number to check its ODD or EVEN : "))

# def check_even_odd(n):
#     if n % 2 == 0:
#         return "The number is even"
#     else:
#         return "The number is odd"

# print(check_even_odd(n))


# recursive function using call stack

# def show_number(n):
#     if n > 0:
#         print(n)
#         show_number(n-1)
#     else:
#         return

# show_number(5)



# Write a recursive function to calculate the sum of the first n natural numbers.

# def sum_natural(n):
#     if n == 1:
#         return 1
#     else:
#         print(n)
#         return n + sum_natural(n-1)
    
# total_sum = sum_natural(5)
# print("The sum of the first 5 natural numbers is:", total_sum)