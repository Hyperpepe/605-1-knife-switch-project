# FilesBatchRename.py
# 导入os库
import os

# 图片存放的路径,不能有中文。
path = r"C:\Users\Lenovo\Desktop\closed"

# 遍历更改文件名
num = 1
for file in os.listdir(path):
    os.rename(os.path.join(path, file), os.path.join(path, "ztf"+str(num)) + ".jpg")# .join 的参数中”ztf“改为各位的首字母缩写
    num = num + 1