import pandas as pd
import matplotlib.pyplot as plt

# 假設的數據
data = {
    'Stage': ['Awareness', 'Interest', 'Consideration', 'Intent', 'Purchase'],
    'Number of Customers': [5000, 3000, 2000, 1000, 500]
}

# 轉換成 DataFrame
df = pd.DataFrame(data)

# 繪製漏斗圖
plt.figure(figsize=(10, 6))
plt.barh(df['Stage'], df['Number of Customers'], color='skyblue')
plt.xlabel('Number of Customers')
plt.title('Marketing Funnel')
plt.gca().invert_yaxis()  # 顛倒Y軸，讓漏斗從上到下
plt.show()


###section 
#%%
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns   
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
plt.style.use('seaborn-dark')
plt.rcParams['font.sans-serif'] = ['pingfang SC']
plt.rcParams['axes.unicode_minus'] = False  

visiror_num  = 135043
data  =[ 135043,  100000,  50000,  20000,  10000]
phase = ['訪客數', '註冊數', '開通數', '交易數', '付費數']  
data1 = [visiror_num/2 - i/2 for i in data] 
data2 = [i+j for i,j in zip(data1,data)]    
color_list = ['#FFA07A', '#FF6347', '#FF4500', '#FF0000', '#DC143C']    

fig, ax = plt.subplots(figsize=(10, 6),facecolor='w')   
ax.barh(phase[::-1], data2[::-1], color=color_list,height=0.7)
ax.barh(phase[::-1], data1[::-1], color='w',height=0.7) 
ax.axis('off')  


polygons = []   
for i in range(len(data)):
    ax.text(
        data2[0]/2,
        i,
        f'{data2[::-1][i]}' + '(' + str(round(data[::-1][i]/data[0]*100, 1)) + '%)',
        color='black', alpha=0.7, fontsize=12, ha='center', va='center'
    )
    if i < len(data) - 1:  # 確保 i+1 不會超出 data 的長度
        ax.text(
            data2[0]/2,
            4.4 - i,
            str(round(data[i+1]/data[i]*100, 3)*100) + '%',
            color='black', alpha=0.7, fontsize=12, ha='center', va='center'
        )
        polygons.append(Polygon(
            xy=np.array([[data1[i+1], 4+0.35-i], [data2[i+1], 4+0.35-i], [data2[i], 5-0.35-i], [data1[i], 5-0.35-i]]),
        ))
ax.add_collection(PatchCollection(polygons, facecolor='w', edgecolor='k', linewidths=1, alpha=0.6))

# %%
import pandas as pd
import matplotlib.pyplot as plt 
data = {
    '物流拖車': [8677, 959, 502, 90],
    '智能監控': [167294, 2793, 435, 346],
    '活動辦理': [177026, 2165, 445, 21],
    '建材': [11815, 928, 238, 25],
    '產險': [108710, 7228, 4298, 897],
    '商務中心': [7288, 273, 122, 49],
    '工程公司': [386178, 4922, 1289, 236]
}

index = ['Stage1/廣告曝光', 'Stage2/點擊', 'Stage3/瀏覽內容', 'Stage4/詢價、購買']

df = pd.DataFrame(data, index=index)


import plotly.express as px 
# fig = px.funnel(df, title='Funnel Chart', labels={'index':'Stage', 'value':'Number of Customers'})
# fig.show()

import plotly.subplots as sp

# 要繪製漏斗圖的變數
variables = ['物流拖車', '智能監控', '活動辦理', '建材', '產險', '商務中心', '工程公司']

# 創建一個子圖的布局，每行顯示2個漏斗圖
fig = sp.make_subplots(rows=len(variables)//2 + len(variables)%2, cols=2, subplot_titles=variables)

# 為每個變數創建一個漏斗圖
for i, var in enumerate(variables):
    df_var = df[[var]]  # 選擇特定變數的數據
    funnel_fig = px.funnel(df_var, title=var, labels={'index':'Stage', 'value':'Number of Customers'})
    fig.add_trace(funnel_fig.data[0], row=i//2+1, col=i%2+1)

# 設定整個圖形的大小和子圖的間距
fig.update_layout(height=800, width=1200, title_text="Funnel Chart", showlegend=False)

fig.show()



# %%
