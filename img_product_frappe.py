import pandas as pd
import matplotlib.pyplot as plt

# 创建数据字典
data = {
    "Experiment ID": [
        "FinalMLP_frappe_x1_001_d86a2703", "FinalMLP_frappe_x1_002_ec879137", "FinalMLP_frappe_x1_003_c4ca6aa8",
        "FinalMLP_frappe_x1_004_e1ab402f", "FinalMLP_frappe_x1_005_be397d92", "FinalMLP_frappe_x1_006_4f9cbc73",
        "FinalMLP_frappe_x1_007_e7194969", "FinalMLP_frappe_x1_008_df0e6ca4", "FinalMLP_frappe_x1_009_f93456c9",
        "FinalMLP_frappe_x1_010_ce1a596b", "FinalMLP_frappe_x1_011_dd37277e", "FinalMLP_frappe_x1_012_9fb22067"
    ],
    "Test AUC": [
        0.983935, 0.984830, 0.984683, 0.985133, 0.984707, 0.984494, 0.984707, 0.984494, 0.985752,
        0.984886, 0.985516, 0.985264
    ],
    "Test Log Loss": [
        0.171006, 0.160437, 0.160745, 0.149858, 0.155331, 0.151509, 0.155331, 0.151509, 0.155754,
        0.155331, 0.154094, 0.153339
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
plt.savefig('D:\\PapersCode\\FinalMLP\\result_csv\\FinalMLP_frappe.png', dpi=300)

# 显示图表
plt.show()
