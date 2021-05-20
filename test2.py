import shutil
import os
from os import path
import matplotlib.pyplot as plt
import csv
import pandas as pd

i = 0
for root, _, files in os.walk("C:/Users/alan8/Desktop/hydro_logs/"):
    for name in files:
        if "fuzzy_result" in name:
            i = i + 1
            filename = os.path.join(name)
            peko = os.path.join(root, name)
            ina = os.path.join(root, str(i) + '.csv')
            os.rename(peko, ina)
            print(peko)
            print(filename)
            source = peko
            destination = r'C:/Users/alan8/Desktop/hydro_logs/all'
            shutil.copy(ina,destination)
            
Path = r'C:/Users/alan8/Desktop/hydro_logs/all/'          #要拼接的資料夾及其完整路徑，注意不要包含中文
SaveFile_Path = r'C:/Users/alan8/Desktop/hydro_logs/all/'       #拼接後要儲存的檔案路徑
SaveFile_Name = r'all.csv'              #合併後要儲存的檔名


# 修改當前工作目錄
os.chdir(Path)
# 將該資料夾下的所有檔名存入一個列表
file_list = os.listdir()
# print(file_list)

# 讀取第一個CSV檔案幷包含表頭
df = pd.read_csv(Path + file_list[0]) 

# 將讀取的第一個CSV檔案寫入合併後的檔案儲存
df.to_csv(SaveFile_Path + SaveFile_Name, encoding="utf_8", index=False, header=False)


# 迴圈遍歷列表中各個CSV檔名，並追加到合併後的檔案
try:
    for i in range(1, len(file_list)):
        path = Path + file_list[i]
        print(path, '    path is ok')
        df = pd.read_csv(path)
        df.to_csv(SaveFile_Path + SaveFile_Name, encoding="utf_8", index=False, header=False, mode='a+')
        
# 異常處理
except OverflowError:
    print('wrong', path)        