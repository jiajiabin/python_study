# ※※7.编写函数传入一个字符串，将重要信息放在[]之间，找出重要信息
# 传入 我是一个[好人]
# 返回 好人
def question7(s:str):
    # 查找[
    index1 = s.find('[')
    # 查找]
    index2 = s.find(']')
    if index2 < 0 or index1 < 0 or index2 < index1:
        return None
    return s[index1 + 1: index2]

print(question7("我是一个[粉刷匠]，粉刷本领强"))