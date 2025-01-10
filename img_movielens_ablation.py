import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
from matplotlib.lines import Line2D
# 创建数据
methods = ['DualMLP', 'w/o FS', 'Sum', 'Concat', 'EWP', 'FinalMLP']
movielens_author = [96.98, 97.03, 96.95, 96.92, 97.02, 97.2]
movielens_self = [97.10, 97.24, 97.05, 96.84, 97.14, 97.23]

# 设置绘图风格，去掉网格
plt.style.use('seaborn-white')

# 创建图表
fig, ax = plt.subplots(figsize=(10, 6))

# 设置宽度
bar_width = 0.3  # 调整柱子的宽度
index = np.arange(len(methods))  # X轴标签位置

# 使用更鲜艳的颜色（例如蓝色和红色）
author_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']  # Author 柱子的颜色，添加 FinalMLP 的颜色
self_colors = ['#17becf', '#ff9896', '#98df8a', '#ffbb78', '#c5b0d5', '#e377c2']  # Self 柱子的颜色，添加 FinalMLP 的颜色



# 绘制柱状图
for i, method in enumerate(methods):
    # 为 'Author' 绘制柱状图
    ax.bar(index[i] - bar_width / 2, movielens_author[i], bar_width, color=author_colors[i],
           label=f'Author' if i == 0 else "")  # 仅第一次绘制时添加标签

    # 为 'Self' 绘制柱状图
    ax.bar(index[i] + bar_width / 2, movielens_self[i], bar_width, color=self_colors[i],
           label=f'Self' if i == 0 else "")  # 仅第一次绘制时添加标签

# 设置标题和标签
ax.set_title('Movielens AUC Comparison', fontsize=16, weight='bold')  # 加粗标题
ax.set_xlabel('Method', fontsize=12, weight='bold')  # 加粗X轴
ax.set_ylabel('AUC', fontsize=12, weight='bold')  # 加粗Y轴
# 设置X轴标签
ax.set_xticks(index)
ax.set_xticklabels(methods, fontsize=12, weight='bold')  # 设置X轴标签加粗
ax.tick_params(axis='x', rotation=0)  # 将横坐标标签设置为水平
# 设置纵坐标细粒度范围
ax.set_ylim(96.7, 97.4)
ax.yaxis.set_major_locator(MaxNLocator(integer=True, prune='lower', nbins=6))

# 标注 AUC 值
for i in range(len(methods)):
    ax.text(i - bar_width / 2, movielens_author[i] + 0.005, f'{movielens_author[i]:.2f}', ha='center', fontsize=10)
    ax.text(i + bar_width / 2, movielens_self[i] + 0.005, f'{movielens_self[i]:.2f}', ha='center', fontsize=10)

# 设置坐标轴加粗
ax.spines['top'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)

# 设置刻度加粗
ax.tick_params(axis='both', width=2)

legend_elements = []
for i, method in enumerate(methods):
    # 为每个方法创建自定义图例
    legend_elements.append(Line2D([0], [0], color=author_colors[i], lw=4, label=f'Author: {method}'))
    legend_elements.append(Line2D([0], [0], color=self_colors[i], lw=4, label=f'Self: {method}'))

# 添加自定义图例，放置在图的上方，横向排列
ax.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, 1), ncol=5, fancybox=True, shadow=True)

# 自动调整布局
plt.tight_layout()

# 保存图像
plt.savefig('D:\\PapersCode\\FinalMLP\\result_csv\\movielens_auc_comparison.png', dpi=300)

# 显示图表
plt.show()
