import json


def read(path: str):
    try:
        with open(path, "r+", encoding="utf8") as file:
            res = json.load(file)
            return res
    except Exception as e:
        print(e)


def write(path: str, data):
    try:
        with open(path, "w+", encoding="utf8") as file:
            json.dump(data, file, ensure_ascii=False)
    except Exception as e:
        print(e)
