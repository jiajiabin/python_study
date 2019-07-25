#格式化打印

#格式化输出的父类
class FormatPrintDelegate:
    #索要表头
    def get_title(self):
        return None
    #索要数据数量
    def get_nums(self):
        return 0
    # 索要行标题
    def get_line_title(self,line):
        return "line%d" % line
    # 索要行内容
    def get_line_content(self,line):
        return ""
    # 索要结束语
    def get_end_words(self):
        return None

class FormatPrint:
    def print_data(self,data_source:FormatPrintDelegate):
        #表头
        title = data_source.get_title()
        if title:
            print(title.center(30, "="))
        #数据数量
        nums = data_source.get_nums()
        for i in range(nums):
            #打印行标题
            line_title = data_source.get_line_title(i)
            print(line_title.center(30,"-"))
            #打印行内容
            content = data_source.get_line_content(i)
            print(content)
        #打印结束语
        end_words = data_source.get_end_words()
        if end_words:
            print(end_words.center(30,"="))
















