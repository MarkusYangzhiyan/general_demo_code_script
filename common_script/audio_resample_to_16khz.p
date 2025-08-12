from pathlib import Path
import subprocess
from concurrent.futures import ProcessPoolExecutor,as_completed

def resample(src:Path,dst:Path,target_hz:int=16000):
    cmd = [
        "ffmpeg","-y",
        "-i",str(src),
        "-ar",str(target_hz),
        "-ac","1",
        str(dst)
    ]
    subprocess.run(cmd,check=True,
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL
                   )
    logger.info(f"已重采样:{src}")

def parallel_resample(raw_data_root:Path,resampled_root:Path,
                      max_workers:int=None):
    audio_list = list(raw_data_root.rglob("*.wav"))
    logger.info(f"发现{len(audio_list)}个音频文件，现在开始重采样")

    with ProcessPoolExecutor as executor:
        futures = {
            executor.submit(
                resample,
                src,
                resampled_root/src.relative_to(raw_data_root)
            ):src for src in audio_list
        }

        for future in as_completed(futures):
            src = futures[future]
            try:
                future.result()
            except Exception as e:
                logger.error(f"重采样失败：{src}，原因：{e}")
