import matplotlib.pyplot as plt
import numpy as np

# 实验ID
ids = np.arange(1, 11)

# 复现改进结果的AUC值
improved_auc = [97.57, 97.63, 97.59, 97.60, 97.52, 97.65, 97.46, 97.63, 97.63, 97.68]

# 原始复现结果的AUC值
original_auc = [97.05, 96.96, 96.91, 97.23, 97.01, 96.93, 96.84, 97.17, 96.88, 96.94]

# 创建图形和轴
fig, ax = plt.subplots()

# 绘制复现改进结果的折线图
ax.plot(ids, improved_auc, marker='o', color='b', label='Improved AUC')

# 绘制原始复现结果的折线图，使用点线样式
ax.plot(ids, original_auc, marker='x', color='r', linestyle=':', label='Original AUC')

# 添加图例
ax.legend()

# 添加标题和标签，包括数据集名称
ax.set_title('Comparison of AUC on Movielens Dataset')
ax.set_xlabel('Experiment ID')
ax.set_ylabel('AUC (%)')

# 设置y轴的范围，稍微扩大一些
ax.set_ylim(96.5, 98.0)

# 显示网格
ax.grid(True)

# 保存图表到指定路径
plt.savefig(r'D:\PapersCode\FinalMLP\result_csv\Movielens_improved.png', dpi=300, bbox_inches='tight')

# 显示图形
plt.show()