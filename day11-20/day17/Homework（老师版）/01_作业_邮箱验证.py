import re
# 4.判断一个输入的邮箱是正确的邮箱。支持（qq，163，126，gmail）

def is_email_address(s):
    pattern = '\w{1,20}@\w{1,10}(\.com|\.cn|\.net|\.com\.cn)'
    return re.search(pattern, s) != None

def is_email(s):
    pattern = '[0-9]{1,20}@qq\.com|\w{1,20}@(163|126|gmail)\.com'
    return re.search(pattern, s) != None

print(is_email_address('1287945@qq.com'))
print(is_email('1287945a@qq.com'))
print(is_email('good432@163.com'))
