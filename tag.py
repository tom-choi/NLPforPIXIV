import json
from msilib.schema import Directory
import pandas as pd
import csv

with open('./result-#succubus Drawings, Best Fan Art on pixiv, Japan-1647491083659.json', 'r',encoding="utf-8") as f:
  data = json.load(f)
Tags_Directory = {}
print(f"已經捕捉到{len(data)}條信息，準備將tag新增到字典……")
n = len(data)
for i in range(0,n):
  #print(f"idNum:{data[i]['idNum']} tag數量:{len(data[i]['tagsWithTransl'])}")
  for j in range(0,len(data[i]['tagsWithTransl'])):
    if (data[i]['tagsWithTransl'][j] in Tags_Directory):
      Tags_Directory[data[i]['tagsWithTransl'][j]] += 1
    else:
      Tags_Directory[data[i]['tagsWithTransl'][j]] = 1
# print(f"Tags_Directory 字典收錄了以下tags: ")
# for key in Tags_Directory.keys():
#   print(f"{key} : {Tags_Directory[key]}")

pd_Tags_Directory = []
pd_Tags_Directory_ID = {}
i = 0
print("製作字典序……")
for key in Tags_Directory.keys():
  pd_Tags_Directory.append(key)
  pd_Tags_Directory_ID[key] = i
  i += 1
with open('./pd_Tags_Directory_ID.json', 'w+',encoding="utf-8") as f:
  json.dump(pd_Tags_Directory_ID,f)
print(f"字典序完成(一共 {len(Tags_Directory)} 個tags)")
# for i in range(0,n):
#   for j in range(0,len(data[i]['tagsWithTransl'])):
#     if (data[i]['tagsWithTransl'][j] in Tags_Directory):
#       Tags_Directory[data[i]['tagsWithTransl'][j]] += 1
#     else:
#       Tags_Directory[data[i]['tagsWithTransl'][j]] = 1
# k = 0
# times = 1
# print(f"進程:統計Tags二元組…… ({k}/{n})")
# Count_Tags = {"kEySSS": pd_Tags_Directory}
# for key in pd_Tags_Directory_ID:
#   Count_Tag = [0 for _ in range(len(pd_Tags_Directory_ID))]
#   for i in range(0,n):
#     if (key not in data[i]['tagsWithTransl']):
#       continue
#     else:
#       for j in range(0,len(data[i]['tagsWithTransl'])):
#         Count_Tag[pd_Tags_Directory_ID[data[i]['tagsWithTransl'][j]]] += 1
#   Count_Tags[key] = Count_Tag
#   k += 1
#   if (k % (n//100) == 0):
#     print(f"進程:統計Tags二元組…… ({k}/{n}) 已完成{times}%")
#     times += 1
# print(f"統計完成!準備輸出excel檔案")
# #print(pd_Tags_Directory)
# df = pd.DataFrame(Count_Tags)
# df.to_csv('trainning.csv')
# print(df)

