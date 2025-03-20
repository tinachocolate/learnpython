"""
赋值运算符和复合赋值运算符

Version: 1.0
Author: 骆昊

a = 10
b = 3
print(a,b)   
a += b        # 相当于：a = a + b
print(a,b) 
a *= a + 2    # 相当于：a = a * (a + 2)
print(a,b)       # 大家算一下这里会输出什么

print(a := 10+10)
a -= 110
print(a)

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag0
print('flag0 =', flag0)     # flag0 = True
print('flag1 =', flag1)     # flag1 = True
print('flag2 =', flag2)     # flag2 = False
print('flag3 =', flag3)     # flag3 = False
print('flag4 =', flag4)     # flag4 = True
print('flag5 =', flag5)     # flag5 = False
print(flag1 and not flag2)  # True
print(1 > 2 or 2 == 3)      # False

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.d华氏度 = %.i摄氏度' % (f, c)) 
# % 符号用于格式化字符串。具体来说，
# % 符号在格式化字符串中的作用是将后面的元组中的值插入到格式说明符的位置。
#第一个 % 是格式化字符串的一部分，表示格式说明符的开始。
#第二个 % 是格式化操作符，用于将后面的元组中的值插入到格式化字符串中的格式说明符位置。
"""