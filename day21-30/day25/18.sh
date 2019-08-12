# 格式符输入密码
# -p 提示文字
# -n 允许输入的最大字符数
# -t 允许输入最大耗时
# -s 隐藏输入的内容
read -p "请输入您的密码" -n 6 -s passwd

echo （$passwd）


