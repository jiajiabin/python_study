st = open("shell.st", "r", encoding="utf-8")
st_list = st.readlines()

heros = {}
for i in st_list[:2]:
    # 创建对象
    # hero|Xingshi
    ls = i[:-1].split("|")
    mo = __import__(ls[0])
    func = getattr(mo, ls[1], None)
    if func:
        heros[ls[1]] = func()

for i in st_list[2:]:
    # 行为
    # Xingshi|tianmaliuxingquan
    ls = i[:-1].split("|")
    hero = heros[ls[0]]     # 找到一个Xingshi对象 hero是对象的引用
    func = getattr(hero, ls[1], None)   # hero.tianmaliuxingquan
    if func:
        func()
