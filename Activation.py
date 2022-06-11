import datetime

from datetime import date
from os import environ

from Ceasar import decrypt
# from activationForm import app
from activationForm import app
from json_handler import *


path = "config_activation.json"


def check_activation():
    date_today = date.today()
    config = read(path)
    First_Start = config.get("First_Start")

    if First_Start == "":
        config["First_Start"] = str(date_today)
        write(path, config)
    else:
        a = First_Start.split("-")
        b = (int(str(date_today - datetime.date(int(a[0]), int(a[1]), int(a[2]))).split()[0]))
        if (b > 10 and config.get("activated") == False):
            print("EXPIRED")
            print("Follow the link and solve captcha to enter the activation code:\nhttp://127.0.0.1:5000\n\n\n")
            app.run(host="0.0.0.0", port= environ.get("PORT", 5000))
            # exit("expired")

def days_until_expiration():
    date_today = date.today()
    config = read(path)
    if (config.get("activated")):
        return "Product is Activated"
    else:
        First_Start = config.get("First_Start")
        a = First_Start.split("-")
        b = (datetime.date(int(a[0]), int(a[1]), int(a[2])))
        c = date_today
        return (10 - int(str(b - c).split("-")[1].split(" ")[0]))


def activator():
    config = read(path)
    code = str(input("Enter activation code: "))
    if (code == decrypt(config.get("code"), 3)):
        print("Activation Success!")
        config["activated"] = True
        write(path, config)
        menu()
        return True
    else:
        print("Invalid activation code!")
        activator()




def expiration_date():
    date_today = date.today()
    config = read(path)
    First_Start = config.get("First_Start")
    a = First_Start.split("-")
    b = (datetime.date(int(a[0]), int(a[1]), int(a[2])))
    c = str(date.today()).split("-")
    d = (datetime.date(int(c[0]), int(c[1]), int(c[2])))
    print(b - d)






