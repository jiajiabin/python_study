def function01():
    print("春眠不觉晓!")

def function02():
    for i in range(3):
        print("夏天不洗澡!")

    function01()



print("before")

function02()    # 在这里调用fucntion02，如同将function02的代码，写在这里一样

print("after")