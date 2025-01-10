import matplotlib.pyplot as plt
import numpy as np

# 实验ID
ids = np.arange(1, 11)

# 第一组数据（改进后的AUC值）
improved_auc = [98.79, 98.63, 98.66, 98.75, 98.69, 98.99, 99.10, 98.99, 99.17, 99.12]

# 第二组数据（原始AUC值）
original_auc = [98.39, 98.48, 98.47, 98.51, 98.47, 98.45, 98.47, 98.45, 98.58, 98.49]

# 创建图形和轴
fig, ax = plt.subplots()

# 绘制改进后的AUC值折线图
ax.plot(ids, improved_auc, marker='o', color='b', label='Improved AUC')

# 绘制原始AUC值折线图
ax.plot(ids, original_auc, marker='x', color='r', linestyle='--', label='Original AUC')

# 添加图例
ax.legend()

# 添加标题和标签，包括数据集名称
ax.set_title('Comparison of AUC on Frappe Dataset')
ax.set_xlabel('Experiment ID')
ax.set_ylabel('AUC (%)')

# 设置y轴的范围，稍微扩大一些
ax.set_ylim(98, 99.5)

# 显示网格
ax.grid(True)

# 保存图表到指定路径
plt.savefig(r'D:\PapersCode\FinalMLP\result_csv\Frappe_improved.png', dpi=300, bbox_inches='tight')

# 显示图形
plt.show()