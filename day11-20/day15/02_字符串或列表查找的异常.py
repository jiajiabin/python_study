s = "abcdefg"
try:
    ret = s.index("acc")
    print(ret)
except ValueError:
    print("找不到")

l = [1, 2, 3, 4, 5]
try:
    ret = l.index(8)
    print(ret)
except ValueError:
    print("找不到")

d = {"one": 1, "two": 2, "three": 3}
d["Four"] = 4
try:
    print(d["Five"])
except KeyError:
    print("没有这个键")