from Ceasar import encrypt, decrypt, hacking
from json_handler import *


def encryptor():
    res = encrypt(str(input("Enter text to encrypt: ")), int(input("Enter s: ")))
    print(res)
    save(res)


def decrypter():
    res = decrypt(str(input("Enter text to decrypt: ")), int(input("Enter s: ")))
    print(res)
    save(res)


def hacker():
    res = hacking(str(input("Enter text to hack: ")), str(input("Enter language: ")))
    for el in res:
        print(el)
    save(res)


def hacker_file():
    res = hacking(str(read(str(input("Enter path: ")))), str(input("Enter language: ")))
    for el in res:
        print(el)
    save(res)


def save(res):
    a = str(input("Save to file?: Y/N\n"))
    if (a == "Y"):
        write(str(input("Enter file name: ")), res)
    if (a == "N"): return
    else: print("Wrong letter")
