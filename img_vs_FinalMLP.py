import matplotlib.pyplot as plt
import numpy as np

# 数据
datasets = ['Criteo', 'Avazu', 'MovieLens', 'Frappe']
author_auc = [81.49, 76.66, 97.2, 98.61]
self_auc = [81.49, 76.61, 97.23, 98.69]
author_logloss = [43.7, 36.58, 19.66, 14.84]
self_logloss = [43.72, 36.59, 20.92, 15.58]

# 新的颜色（更美观）
color_author_auc = '#4C72B0'  # 深蓝色
color_self_auc = '#55A868'    # 绿色
color_author_logloss = '#F07F68'  # 橙红色
color_self_logloss = '#6A4D7D'    # 紫色

# 创建图形和两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# 设置柱子宽度（进一步加宽柱子）
bar_width = 0.6  # 进一步增加柱子宽度，调整为0.6
index = np.arange(len(datasets))

# 设置数据集之间的空隙
gap_between_datasets = 1  # 数据集之间的空隙
x_offset = np.arange(len(datasets)) * (bar_width + gap_between_datasets)

# 画 AUC 的柱状图（不同的颜色）
bars1 = ax1.bar(x_offset - bar_width/2, author_auc, width=bar_width, label='Author AUC', color=color_author_auc)
bars2 = ax1.bar(x_offset + bar_width/2, self_auc, width=bar_width, label='Self AUC', color=color_self_auc)
ax1.set_xlabel('Datasets')
ax1.set_ylabel('AUC')
ax1.set_title('AUC Comparison for FinalMLP on Different Datasets')  # 修改标题
ax1.set_xticks(x_offset)
ax1.set_xticklabels(datasets)
ax1.legend()

# 在 AUC 柱状图上标注具体数值，黑色加粗
for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height + 0.5, f'{height:.2f}', ha='center', va='bottom', color='black', fontweight='bold')
for bar in bars2:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height + 0.5, f'{height:.2f}', ha='center', va='bottom', color='black', fontweight='bold')

# 画 Logloss 的柱状图（不同的颜色）
bars3 = ax2.bar(x_offset - bar_width/2, author_logloss, width=bar_width, label='Author Logloss', color=color_author_logloss)
bars4 = ax2.bar(x_offset + bar_width/2, self_logloss, width=bar_width, label='Self Logloss', color=color_self_logloss)
ax2.set_xlabel('Datasets')
ax2.set_ylabel('Logloss')
ax2.set_title('Logloss Comparison for FinalMLP on Different Datasets')  # 修改标题
ax2.set_xticks(x_offset)
ax2.set_xticklabels(datasets)
ax2.legend()

# 在 Logloss 柱状图上标注具体数值，黑色加粗
for bar in bars3:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height + 0.2, f'{height:.2f}', ha='center', va='bottom', color='black', fontweight='bold')
for bar in bars4:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, height + 0.2, f'{height:.2f}', ha='center', va='bottom', color='black', fontweight='bold')

# 调整布局以避免重叠
plt.tight_layout()
plt.savefig('D:\\PapersCode\\FinalMLP\\result_csv\\FinalMPL.png', dpi=300)
# 显示图形
plt.show()
