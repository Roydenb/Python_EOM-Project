import random

Lotto_No = []

for i in range(0, 6):
    number = random.randint(1, 49)
    while number in Lotto_No:
        number = random.randint(1, 49)

    Lotto_No.append(number)

    Lotto_No.sort()




User_inout = []
for i in range(0, 6):
    number = int(input("Please enter number between 1 and 49: "))
    while (number in User_inout or number<1 or number>50):
        print("invailid number, please try again")
        number = int(input("Please enter number between 1 and 49: "))

    User_inout.append(number)

count = 0
for number in User_inout:
    if number in Lotto_No:
        count += 1


print(str(count))
print(Lotto_No)
print(User_inout)
