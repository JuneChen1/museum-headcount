# 資料來源：https://data.gov.tw/dataset/164265
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = 'https://data.cip.gov.tw/API/v1/dump/datastore/A53000000A-112046-003'

df = pd.read_csv(url)
df = df.loc[df['民國年'] <= 109]
annual = df.groupby('民國年')['人次'].sum()
month = df.groupby('月份')['人次'].sum()

plt.figure(figsize=(25, 12), dpi=300)
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'
#1
plt.subplot(2, 2, 1)
plt.title('年度的參觀總人次', fontsize=25)
plt.bar(annual.index, annual.values)
plt.xticks(annual.index)
for i in annual.index:
  plt.text(i, annual[i]-100000, annual[i], ha='center', color='w')
#2
plt.subplot(2, 2, 2)
plt.title('各個月份的總參觀人次', fontsize=25)
plt.plot(month.index, month.values, color='darkorange')
plt.xticks(month.index, ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'])
plt.yticks(np.arange(200000, 440001, 30000))
plt.grid()
for i in month.index:
  if month[i] >= month.median():
    plt.text(i, month[i]-10000, month[i], ha='center')
  else:
    plt.text(i, month[i]+10000, month[i], ha='center')

plt.savefig('地方文物館參觀人數統計.png')