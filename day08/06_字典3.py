# 字典的作用
# 1.网络上传输数据，都是以字符串形式进行传输，但是字符串拥有格式，【JSON】是网络字符串中常见格式
# JSON 数据可以轻松的转成字典。【XML】格式也非常类似字典的格式
# [00:15:10]这是歌词的格式
# 2.字典可以进行同类数据多选一操作，在选取多种方案之一的时候，比if else更好用的多

# 例如我写一个程序，支持中文、英文两种文本

def translation(word, language):
    d = {
        "welcome": {
            "ENG": "Welcome to use!!",
            "CHN": "欢迎您的使用！！",
            "BID": "叽叽叽叽叽叽！！"
        },
        "over": {
            "ENG": "Thank for use!!",
            "CHN": "感谢你的使用，下次再会！！",
            "BID": "喳喳喳喳喳！！"
        }
    }
    return d[word][language]


current_language = "CHN"
print(translation("welcome", current_language))

print(translation("over", current_language))




