import random

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$&*_%"
while True:
    pass_len = int(input("Enter length of password: "))
    pass_count = int(input("Enter the number of required passwords: "))

    for i in range(0, pass_count):
        password = ""
        for j in range(0, pass_len):
            pass_char = random.choice(char)
            password = password+pass_char
        print(f"Generated password is ", password)
    repeat = input("Do you want to generate more passwords? ")
    if repeat == 'n' or repeat == 'N':
        break
print("Thank you !!!")
