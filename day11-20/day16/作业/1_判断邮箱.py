# 判断一个输入的邮箱是正确的邮箱。支持（qq，163，126，gmail）
# 同上题，支持任何邮箱

import re

str = "2592668397@qq.com"

ret1 = re.search('@(qq|163|126|gmail)\.com',str)
print(ret1)

ret2 = re.search('\w{1,20}@\w{1,10}(.*)(\.com|\.cn|\.net|\.com\.cn)',str)
print(ret2)