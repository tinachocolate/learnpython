"""
print(0b100)  # 二进制整数
print(0o100)  # 八进制整数
print(100)    # 十进制整数
print(0x100)  # 十六进制整数

a = 100
b = 123.45
c = 'hello, world'
d = True
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>

a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello, world'
g = True
print(float(a))         # int类型的100转成float，输出100.0
print(int(b))           # float类型的123.45转成int，输出123
print(int(float(c)))           # str类型的'123'转成int，输出123
print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
print(int(d, base=2))   # str类型的'100'按二进制转成int，输出4
print(float(e))         # str类型的'123.45'转成float，输出123.45
print(bool(f))          # str类型的'hello, world'转成bool，输出True
print(int(g))           # bool类型的True转成int，输出1
print(chr(a))           # int类型的100转成str，输出'd'
print(ord('d'))         # str类型的'd'转成int，输出100

在 Python 中，不同类型的变量可以相互转换，但并不是所有类型的转换都是可行的。以下是一些常见的类型转换方法及其注意事项：

### 整形 (`int`)、浮点型 (`float`)、字符串型 (`str`)、布尔型 (`bool`) 之间的转换

#### 1. 整形 (`int`) 转换

- **转换为浮点型 (`float`)**：
  ```python
  a = 100
  float_a = float(a)  # 输出: 100.0
  ```

- **转换为字符串型 (`str`)**：
  ```python
  a = 100
  str_a = str(a)  # 输出: '100'
  ```

- **转换为布尔型 (`bool`)**：
  ```python
  a = 100
  bool_a = bool(a)  # 输出: True (非零为True，零为False)
  ```

#### 2. 浮点型 (`float`) 转换

- **转换为整型 (`int`)**：
  ```python
  b = 123.45
  int_b = int(b)  # 输出: 123 (截断小数部分)
  ```

- **转换为字符串型 (`str`)**：
  ```python
  b = 123.45
  str_b = str(b)  # 输出: '123.45'
  ```

- **转换为布尔型 (`bool`)**：
  ```python
  b = 123.45
  bool_b = bool(b)  # 输出: True (非零为True，零为False)
  ```

#### 3. 字符串型 (`str`) 转换

- **转换为整型 (`int`)**：
  ```python
  c = '123'
  int_c = int(c)  # 输出: 123
  ```
  - 注意：字符串必须是有效的整数表示，否则会引发 `ValueError`。
  - 可以指定进制：
    ```python
    c = '100'
    int_c_base2 = int(c, base=2)  # 输出: 4 (二进制)
    int_c_base16 = int(c, base=16)  # 输出: 256 (十六进制)
    ```

- **转换为浮点型 (`float`)**：
  ```python
  e = '123.45'
  float_e = float(e)  # 输出: 123.45
  ```
  - 注意：字符串必须是有效的浮点数表示，否则会引发 `ValueError`。

- **转换为布尔型 (`bool`)**：
  ```python
  f = 'hello, world'
  bool_f = bool(f)  # 输出: True (非空字符串为True，空字符串为False)
  ```

#### 4. 布尔型 (`bool`) 转换

- **转换为整型 (`int`)**：
  ```python
  g = True
  int_g = int(g)  # 输出: 1 (True 为 1，False 为 0)
  ```

- **转换为浮点型 (`float`)**：
  ```python
  g = True
  float_g = float(g)  # 输出: 1.0 (True 为 1.0，False 为 0.0)
  ```

- **转换为字符串型 (`str`)**：
  ```python
  g = True
  str_g = str(g)  # 输出: 'True'
  ```

### 不可行的转换

- **字符串型 (`str`) 转换为整型 (`int`)** 或 **浮点型 (`float`)**：
  - 字符串必须是有效的数字表示，否则会引发 `ValueError`。
  - 例如：
    ```python
    c = 'hello'
    int_c = int(c)  # 引发 ValueError: invalid literal for int() with base 10: 'hello'
    ```

- **字符串型 (`str`) 转换为布尔型 (`bool`)**：
  - 字符串转换为布尔型时，空字符串 `''` 为 `False`，非空字符串为 `True`。
  - 例如：
    ```python
    f = ''
    bool_f = bool(f)  # 输出: False
    ```

### 总结

- **可行的转换**：
  - `int` ↔ `float`
  - `int` ↔ `str` (字符串必须是有效的数字表示)
  - `int` ↔ `bool`
  - `float` ↔ `str` (字符串必须是有效的数字表示)
  - `float` ↔ `bool`
  - `str` ↔ `bool`
  - `bool` ↔ `int`
  - `bool` ↔ `float`
  - `bool` ↔ `str`

- **不可行的转换**：
  - 字符串必须是有效的数字表示才能转换为 `int` 或 `float`。
  - 字符串转换为 `int` 或 `float` 时，字符串必须是有效的数字表示，否则会引发 `ValueError`。

通过这些方法，你可以在 Python 中灵活地进行不同类型之间的转换。
"""

