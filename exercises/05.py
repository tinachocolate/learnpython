
"""
BMI计算器

Version: 1.0
Author: 骆昊

height = float(input('身高(cm)：'))
weight = float(input('体重(kg)：'))
bmi = weight / (height / 100) ** 2
print(f'{bmi = bmi:d}')
#print(f'{bmi = :.2f}')
if 18.5 <= bmi < 24:
    print('你的身材很棒！')
    print('你的体重正常。')
print('BMI = {:.2f}'.format(bmi))
a =12.34
print(a)

print(f'{a:d}')
print(f'{a:f}')
print(f'{a:.2f}')
"""
num = 10.123
print(f'{int(num):d}')  
print(int(num)) 
print(num) 