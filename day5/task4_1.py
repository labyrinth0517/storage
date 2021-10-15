dict0 = {"k1": "v1", "k2": "v2", "k3": "v3"}

# 循环遍历出所有的key
keys = []
for j in dict0.keys():
    keys.append(j)
print("循环遍历出所有的key:", keys)

# 循环遍历出所有value
values = []
for i in dict0.values():
    values.append(i)
print("循环遍历出所有value:", values)

# 请在字典中增加一个键值对, "k4":"v4"
dict0["k4"] = "v4"
print("字典：", dict0)
