#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
运行AI日报生成脚本
"""

import sys
import os

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 导入并运行main函数
from main import main

if __name__ == "__main__":
    print("开始运行AI日报生成脚本...")
    main()
    print("脚本执行完成！")
