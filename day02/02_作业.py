name = '胡家彬'
print('大家好，我是：',name)

诗 = '春眠不觉晓，\n处处闻啼鸟。\n夜来风雨声，\n花落知多少。'
print(诗)

a1 = '*************\n欢迎学习Python\n************* '
print(a1)

a2 = '\n	          	*\n \n               ***\n \n              *****\n \n             *******'
print(a2)

#进制转换
'''
十进制转二进制
    78 = 0b1001110
    97 = 0b1100001
    193 = 0b11000001
    17.125 = 
十进制转八进制
    22 = 0o26
    59 = 0o73
    98 = 0o142
二进制转八进制
    1 000 101 110 111 001 010(2) = 0o1056712
    0 101 111 000 110(2) = 0o5706
    111 000 101 001 010(2) = 0o70512
二进制转十六进制
    1 0101 0111 0101 0101(2) = 0x15755
    1000 0011 1010 1101 0101(2) = 0x83ad5
    110 0001 0101 0101 0101(2) = 0x61555
    011 0101 0101 0101 0011(2) = 0x35553
    0011 0101 0101 0111 0101(2) = 0x35575   
'''
'''
计算出下面数值的补码【以8位为准】
77  原码：0 100 1101
    补码：0 100 1101
18  原码：0 001 0010
    补码：0 001 0010
22  原码：0 001 0110
    补码：0 001 0110
-22  原码：1 001 0110
     补码：1 110 1010
-19  原码：1 001 0011
     补码：1 110 1101
-32  原码：1 010 0000
     补码：1 110 0000
-45  原码：1 010 1101
     补码：1 101 0011
'''
'''
利用补码原理计算出结果【以二进制格式计算，要求有过程 以8位为准】
18+19:
    18原码：0 001 0010    19原码：0 001 0011
      补码：0 001 0010      补码：0 001 0011
    18+19 = 0 001 0010 + 
            0 001 0011
          = 0 010 0101 (正数补码等于原码，转换10进制）
          = 37
22+（-10）:
    22原码：0 001 0110    （-10）原码：1 000 1010
      补码：0 001 0110           补码：1 111 0110
    22+（-10）= 0 001 0110 +
                1 111 0110
              = 0 000 1100 (正数补码等于原码，转换10进制）
              = 12
(-32) + 18 :
    (-32)原码：1 010 0000     18原码：0 001 0010
         补码：1 110 0000       补码：0 001 0010
    (-32) + 18= 1 110 0000 +
                0 001 0010
              = 1 111 0010（补码）
              = 1 000 1110（原码）
              =（-14）
(-45) + (-12):
    (-45)原码：1 010 1101     (-12)原码：1 000 1100
         补码：1 101 0011          补码：1 111 0100
    (-45) + (-12)= 1 101 0011 +
                   1 111 0100
                 = 1 100 0111（补码）
                 = 1 011 1001（原码）
                 =（-57）
17 + 19
    17原码：0 001 0001    19原码：0 001 0011
      补码：0 001 0001      补码：0 001 0011
    17+19 = 0 001 0001 + 
            0 001 0011
          = 0 010 0100 (正数补码等于原码，转换10进制）
          = 36
'''
'''
写出下列数字的二进制八进制十六进制形式
110010101(2) = 625(8) = 195(16)
296(10) = 100101000(2) = 450(8) = 128(16)
156a(16) = 1010101101010(2) = 12552(8)
2387(10) = 100101010011(2) = 4523(8) = 953(16)
1103(8) = 1001000011(2) = 243(16)
195(16) = 11010101(2) = 625(8)
0625(8) = 110010101(2) = 195(16)
405 = 110010101(2) = 625(8) = 195(16)
'''
'''
写出以下数字的补码，在2字节的情况下
35   原码：0000 0000 0010 0011
     补码：0000 0000 0010 0011
12   原码：0000 0000 0000 1100
     补码：0000 0000 0000 1100
-7   原码：1000 0000 0000 0111
     补码：1111 1111 1111 1001
-18  原码：1000 0000 0001 0010
     补码：1111 1111 1110 1110
-13  原码：1000 0000 0000 1101
     补码：1111 1111 1111 0011
'''