#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

# 设置输出编码
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

# 运行main.py
exec(open('main.py', encoding='utf-8').read())
