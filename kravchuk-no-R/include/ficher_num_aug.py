import os
import re

increment = 155
# 设置 tempraire 文件夹的路径
folder_path = "/Users/apple/Desktop/DATASIM/Projets/sans R/kravchuk-no-R/samples2"

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    match = re.match(r"noise_(\d+)\.mat", filename)
    if match:
        num = int(match.group(1))
        new_num = num + increment
        new_filename = f"noise_{new_num}.mat"
        
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")
