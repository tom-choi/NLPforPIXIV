import json
from msilib.schema import Directory
import os
import pandas as pd
import csv
import os
import time

clear = lambda: os.system('cls')  # On Windows System
print(f"載入數據庫中……")
df=pd.read_csv("trainning.csv")
with open('./pd_Tags_Directory_ID.json', 'r',encoding="utf-8") as f:
  pd_Tags_Directory_ID = json.load(f)
V = len(pd_Tags_Directory_ID)
print(f"|V| = {V}")
Target = ""
while(1):
  Target = input("輸入要預測的tag(輸入'exit'退出): ")
  if (Target == 'exit'):
    break
  elif (Target not in pd_Tags_Directory_ID):
    print("查無此tag")
    continue
  print(f"預測 '{Target}' 之後可能同時擁有以下tags:")
  scores = df.values[pd_Tags_Directory_ID[Target]]
  C_word = df.values[pd_Tags_Directory_ID[Target],pd_Tags_Directory_ID[Target]]
  for i in range(2,len(scores)):
    if (i == pd_Tags_Directory_ID[Target]):
      scores[i] = -1
    scores[i] = (int(scores[i])+1) / (int(C_word)+V)
  sorted_id = sorted(range(2,len(scores)), key=lambda k: scores[k], reverse=True)
  for i in range(10):
    print(f"[{i+1}] : {df.values[sorted_id[i]][1]} 出現概率為: {scores[sorted_id[i]]*100}%")
  time.sleep(30)

  