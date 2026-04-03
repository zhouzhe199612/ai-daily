# 测试所有Python文件的语法
import sys
import os

# 要检查的文件
files = ['main.py', 'fetch.py', 'clean.py', 'process.py', 'render.py', 'config.py']

for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            code = f.read()
        compile(code, file, 'exec')
        print(f"{file}: 语法正确")
    except SyntaxError as e:
        print(f"{file}: 语法错误 - {e}")
    except Exception as e:
        print(f"{file}: 其他错误 - {e}")

print("语法检查完成")
