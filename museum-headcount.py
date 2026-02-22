# 資料來源：https://data.gov.tw/dataset/164265
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://data.cip.gov.tw/API/v1/dump/datastore/A53000000A-112046-003'

df = pd.read_csv(url)
df = df.loc[df['民國年'] <= 109]
annual = df.groupby('民國年')['人次'].sum()

plt.figure(figsize=(25, 12), dpi=300)
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'
plt.subplot(2, 2, 1)
plt.title('年度的參觀總人次', fontsize=25)
plt.bar(annual.index, annual.values)
plt.xticks(annual.index)
for i in annual.index:
  plt.text(i, annual[i]-100000, annual[i], ha='center', color='w', fontsize=12)

plt.savefig('地方文物館參觀人數統計.png')