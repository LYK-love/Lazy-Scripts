import re

text = """
06-需求基础.pdf
07-需求分析方法.pdf
08-需求文档化与验证.pdf
09-软件设计基础.pdf
10-软件体系结构基础.pdf
11-软件体系结构设计与构建.pdf
12-人机交互.pdf
13-详细设计.pdf
14-模块化与信息隐藏.pdf
15-面向对象的模块化.pdf
16-面向对象的信息隐藏.pdf
17-设计模式.pdf
18-软件构造.pdf
19-软件测试.pdf
20-软件交付.pdf
21-软件维护与演化.pdf
22-软件开发过程模型.pdf
23-代码设计.pdf
"""

# Replace "XX-" with "* XX" and remove ".pdf" suffix using regular expressions
text_modified = re.sub(r'(\d+)-', r'\1. ', text)

text_modified = re.sub(r'\.pdf\b', '', text_modified, flags=re.IGNORECASE)

# 打印去除后缀后的文本
print(text_modified)
