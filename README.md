# Extract From TXT

基于Python语言. 本脚本文件可以帮助您提取TXT文本文件中具有一定规律的信息.

## 版本

version 1.0.0

### 支持的内容

- 对具有线性关系的行数对应内容的提取(version 1.0.0)

## 库

- linecache

## 输入格式

```bash
<TXT文件路径> <首定位行数> <步长数> <循环次数>
```

## 样例输入

注：先执行```demo.py```，在脚本所在目录生成```demo.txt```文件.

```bash
demo.txt 1 5 5
```

## 样例输出

```
这是第1行.

这是第6行.

这是第11行.

这是第16行.

这是第21行.

内容共计100行.
```

## 源信息

```python
# !/usr/bin/python
# -*- coding: utf-8 -*-
# @name   : Extract_From_TXT/main.py
# @author : fly6022
# @date   : 2022/5/29
# @Email  : i@fly6022.fun
# @license: MIT
```

## 解决问题

若程序报错，则是TXT文件的文本编码不是UTF-8，请尝试将文本编码转为UTF-8.

