# 关于字典的增删改查

def create_dict():
    return {"One": 1, "Two": 2, "Three": 3, "Four": 4}

# 增
d = create_dict()
d.setdefault("Five", 5)
print(d)
# d.setdefault("Two", "二")
# print(d)
d["Six"] = 6            # 这样也可添加键值对
print(d)
d["Two"] = "二"         # 如果键已存在，会修改对应的值
print(d)

# 删
d = create_dict()
# 删任意一个
d.popitem()
print(d)
# 根据键删除键值对
d.pop("Two")
print(d)
# 清空所有键值对
d.clear()

# 改
d = create_dict()
d["Two"] = "二"

# 查
print(d["One"])

