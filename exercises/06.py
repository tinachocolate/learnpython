"""import time

for _ in range(10):
    print('hello, world')
    time.sleep(1)

从1到100的整数求和

Version: 1.0
Author: 骆昊

total = 0
for i in range(1, 5):
    print(i)
    print(total)
    total += i
print(total)

从1到100的偶数求和
import time
total = 0
for i in range(1, 20):
    if i % 2 == 0:
        print('i=%.i' % i)
        #print('total=%.i'%total)
        print(f'total: {total:d}')
        time.sleep(1)
        total += i
print(total)
从1到100的偶数求和
Version: 1.2
Author: 骆昊
print(sum(range(2, 101, 2)))
打印乘法口诀表
for i in range(1, 10):
    for j in range(1, i + 1):
        #print(i,j)
        print(f'{i}×{j}={i * j}', end='\t')
    print()

输入一个大于1的正整数判断它是不是素数

Version: 1.0
Author: 骆昊
"""
num = int(input('请输入一个正整数: '))
end = int(num ** 0.5)
print(end)
is_prime = True
for i in range(2, end + 1):
    print(f'当前循环次数:{i}')
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')