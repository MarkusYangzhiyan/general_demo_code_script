"""
在全局环境下设置路径
Path(__file__) 取得当下py文件的路径： xx/xx/xx.py
.parent 返回的是上一级路径： xx/xx
假设路径目录：
base
  code
    1.py
    2.py
  input
    file1
    file2
  output
    file1
    file2
  logs
    file1.log
    file2.log
    

os.makedirs： 创建目录，即使父目录不存在也能创建               ##### 推荐用这个就行
os.mkdir：    只能创建当前目录，如果父目录不存在则报错

"""

import os
from pathlib import Path

# =============== 路径配置 ==============================
base_dir = Path(__file__).parent.parent                         # 当前py在code folder下，code、input、output、others folders 平行且在base folder下
input_dir = base_dir/"input"
output_dir = base_dir/'output'
log_dir = base_dir/"logs"
os.makedirs(log_dir,exist_ok=True)
# =======================================================



