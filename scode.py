import random
msg = input("Enter the message ")
ope = int(input("Enter operation to perform  \n1 . Encode \n2. Decode \n"))
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if (len(msg) > 3):
    if (ope == 1):
        # msg1 = msg.split()
        msg1 = ([*msg])
        msg2 = msg1.pop(0)
        msg1.append(msg2)

        for i in range(3):
            msg1.append(random.choice(alpha))
            msg1.insert(0, random.choice(alpha))
        print(''.join(msg1))
        # print(str(msg1))
        # for i in msg1:
        #     print(i, end="")
    elif (ope == 2):
        msg3 = ([*msg])
        for i in range(2, -1, -1):
            msg3.pop(i)
        le = len(msg3)
        for i in range(le-1, le-4, -1):
            msg3.pop(i)

        x = msg3.pop(-1)
        msg3.insert(0, x)
        print(''.join(msg3))
    else:
        print(f"Invalid operation")
else:
    print(f"{msg[::-1]}")
