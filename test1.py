import random

# name=input(str("Please input your name: "))

# age= int(input("Please input your age: "))
# if age < 18:
#    print("Attention!!, you are not allowed to play")
# elif age >= 18:
#     print("Welcome \n" + name )

# input_number_1=int(input("Please enter first number: "))
# input_number_2=int(input("Please enter second number: "))
# input_number_3=int(input("Please enter third number: "))
# input_number_4=int(input("Please enter fourth number: "))
# input_number_5=int(input("Please enter fifth number: "))
# input_number_6=int(input("Please enter last number: "))
# #This is where i need to get the information
#
# input_list= [input_number_1,input_number_2,input_number_3,input_number_4,input_number_5,input_number_6]
# print(input_list)



random_list = random.sample(range(1, 49), 6) # winning lotto numbers
print(random_list)

