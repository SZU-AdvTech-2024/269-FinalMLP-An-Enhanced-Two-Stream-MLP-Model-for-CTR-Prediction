import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.table import Table

# 创建数据
data = {
    'Model': ['FinalMLP Author', 'FinalMLP Self', 'DualMLP Author', 'DualMLP Self'],
    'Criteo AUC': [81.49, 81.49, 81.42, 81.41],
    'Criteo Logloss(%)': [43.7, 43.72, 43.77, 43.79],
    'Avazu AUC': [76.66, 76.61, 76.57, 76.52],
    'Avazu Logloss(%)': [36.58, 36.59, 36.66, 36.71],
    'MovieLens AUC': [97.2, 97.23, 96.98, 97.1],
    'MovieLens Logloss(%)': [19.66, 20.92, 21.07, 20.91],
    'Frappe AUC': [98.61, 98.69, 98.47, 98.45],
    'Frappe Logloss(%)': [14.84, 16.12, 14.71, 15.22]
}

# 创建DataFrame
df = pd.DataFrame(data)

# 设置表格样式
fig, ax = plt.subplots(figsize=(10, 6))  # 设置图形大小
ax.set_frame_on(False)  # 不显示框架
tbl = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')

# 调整表格样式
tbl.auto_set_font_size(False)
tbl.set_fontsize(12)
tbl.scale(1.3, 1.3)  # 调整表格大小

# 隐藏坐标轴
ax.axis('off')

# 显示表格
plt.show()