try:
    i = int(input())
    print(5 / i)        # 解释器无法处理这个操作，会抛出一个异常，ZeroDivisionError
except ZeroDivisionError as e:       # 监听并捕获异常, 捕获到异常信息，就会执行except下面的代码，异常信息也是对象，携带着对异常的描述
    print("除数为0", e)              # 捕获异常，给他一个引用e
except ValueError:                    # 一个try可以对应多个except
    print("输入的数据不是数字")
finally:
    print("不论异常与否，都会执行，最后执行")


