def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char) + s))
    return result


def decrypt(text, s):
    return encrypt(text, -s)


def hacking(text, language):
    res = []
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    LETTERSru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    lan = ""
    if language == "en":
        lan = LETTERS
    else:
        if language == "ru":
            lan = LETTERSru
        else:
            print("unsupported language")
            return
    for key in range(len(lan)):
        translated = ''
        for symbol in text:
            if symbol in lan:
                num = lan.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(lan)
                translated = translated + lan[num]
            else:
                translated = translated + symbol
        res.append('Hacking key #%s: %s' % (key, translated))
    return res
