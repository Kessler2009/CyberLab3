import os


from Controller import *

def menu():
    while True:
        try:
            print("1 - open file", "2 - create file", "3 - encrypt", "4 - decrypt", "5 - hack", "6 - activation",
                  "7 - days until expiration", "8 - hack file", "9 - show files/dirs", "10 - create dir", "11 - exit")
            a = int(input("Enter number: "))
            if (a == 1): print(read(str(input("Enter path: "))))
            if (a == 2): write(str(input("Enter file name: ")), "")
            if (a == 3): encryptor()
            if (a == 4): decrypter()
            if (a == 5): hacker()
            if (a == 6):
                from Activation import activator
                activator()
            if (a == 7):
                from Activation import days_until_expiration
                print(days_until_expiration())
            if (a == 8): hacker_file()
            if (a == 9): print(os.listdir())
            if (a == 10): os.mkdir(str(input("Enter dir name: ")))
            if (a == 11): exit("Have a nice day!")
        except Exception as e:
            print(e)
            continue