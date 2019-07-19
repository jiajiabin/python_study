#编写函数传入一段英文文字，没有标点，单词间用单空格隔开，求，有多少个单词
def word_list(str1):
    if " " not in str1:
        return 1
    else:
        list1 = str1.split(" ")
        while 1:
            if '' in list1:
                list1.remove('')
            else:
                break
        return len(list1)

print(word_list("awd adw   awd"))