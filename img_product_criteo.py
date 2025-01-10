import pandas as pd
import matplotlib.pyplot as plt

# 创建数据字典
data = {
    "Experiment ID": [
        "FinalMLP_criteo_x1_001_ea4a337c", "FinalMLP_criteo_x1_002_7b48432e", "FinalMLP_criteo_x1_003_e8daf7cb",
        "FinalMLP_criteo_x1_004_d5d36917", "FinalMLP_criteo_x1_005_e7be6b59"
    ],
    "Test AUC": [
        0.814773, 0.814803, 0.814766, 0.814614, 0.814869
    ],
    "Test Log Loss": [
        0.437275, 0.437324, 0.437228, 0.437505, 0.437158
    ]
}

# 将数据转化为 DataFrame
df = pd.DataFrame(data)

# 使用数字代替实验ID
df['Experiment ID'] = range(1, len(df) + 1)

# 创建一个2行1列的子图，并增大整个图表的尺寸
fig, ax = plt.subplots(2, 1, figsize=(16, 18))  # 增大图表尺寸

# 设置颜色和样式
auc_color = '#1f77b4'  # 蓝色
loss_color = '#e60000'  # 红色

# 绘制 AUC 曲线，设置 linewidth 为 3，使线条更粗
ax[0].plot(df['Experiment ID'], df['Test AUC'], marker='o', label='Test AUC', color=auc_color, linestyle='-', linewidth=3, markersize=8)
ax[0].set_title('Test AUC Across Experiments', fontsize=18, fontweight='bold')  # 加粗标题
ax[0].set_xlabel('Experiment ID', fontsize=16, fontweight='bold')  # 加粗横坐标
ax[0].set_ylabel('AUC', fontsize=16, fontweight='bold')  # 加粗纵坐标
ax[0].set_xticks(df['Experiment ID'])
ax[0].grid(True, linestyle='--', alpha=0.7)  # 添加网格线

# 标注 AUC 的每个数据点，增大字体并加粗
for i, txt in enumerate(df['Test AUC']):
    ax[0].text(df['Experiment ID'][i], txt, f'{txt:.4f}', color=auc_color, ha='center', va='bottom', fontsize=16, fontweight='bold')

# 绘制 Log Loss 曲线，设置 linewidth 为 3，使线条更粗
ax[1].plot(df['Experiment ID'], df['Test Log Loss'], marker='x', label='Test Log Loss', color=loss_color, linestyle='-', linewidth=3, markersize=8)
ax[1].set_title('Test Log Loss Across Experiments', fontsize=18, fontweight='bold')  # 加粗标题
ax[1].set_xlabel('Experiment ID', fontsize=16, fontweight='bold')  # 加粗横坐标
ax[1].set_ylabel('Log Loss', fontsize=16, fontweight='bold')  # 加粗纵坐标
ax[1].set_xticks(df['Experiment ID'])
ax[1].grid(True, linestyle='--', alpha=0.7)  # 添加网格线

# 标注 Log Loss 的每个数据点，增大字体并加粗
for i, txt in enumerate(df['Test Log Loss']):
    ax[1].text(df['Experiment ID'][i], txt, f'{txt:.4f}', color=loss_color, ha='center', va='bottom', fontsize=16, fontweight='bold')

# 自动调整布局
plt.tight_layout()

# 保存图表为文件
plt.savefig('D:\\PapersCode\\FinalMLP\\result_csv\\FinalMLP_criteo.png', dpi=300)

# 显示图表
plt.show()
