import os
from pathlib import Path

# =============== 路径配置 ==============================
base_dir = Path(__file__).parent.parent                         # 当前py在code folder下，code、input、output、others folders 平行且在base folder下
input_dir = base_dir/"input"
output_dir = base_dir/'output'
log_dir = base_dir/"logs"
os.makedirs(log_dir,exist_ok=True)
# =======================================================
