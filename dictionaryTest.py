if __name__ == '__main__':
    dic = {"Name": "Altair", "Age": 18, "Subject": "Computing"}
    rtnKey = []
    for ele in dic.keys():
        rtnKey.append(ele)
    print(rtnKey)
    rtnValues = []

    for ele in dic.values():
        rtnValues.append(ele)
    print(rtnValues)

    print(dic["Age"])
    print(dic.get("Age"))

    dic["Age"] = 19
    print(dic.get("Age"))

    dic.update({"Sex" : "Male"})
    print(dic.get("Sex"))

    print(list(dic.items()))
