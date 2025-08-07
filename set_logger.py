import logging
from logging.handlers import TimedRotatingFileHandler
import os

# ================ 配置日志 ======================
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = (
    "%(asctime)s [%(levelname)s] %(messages)s"
    "%Y-%m-%d %H:%M:%S"
)

#                   控制台日志
ENABLE_CONSOLE_LOG = os.getenv("ENABLE_CONSOLE_LOG","true") == "true"                #ENABLE_CONSOLE_LOG 的值在code/.env 中预设置好
if ENABLE_CONSOLE_LOG:
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)


#                  文件日志
fh = TimedRotatingFileHandler(
    filename = log_dir/"mylogs.log",
    when = "midnight",
    interval = 1,
    backupCount=0,
    encoding='utf-8',
)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)
