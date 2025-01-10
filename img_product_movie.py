import pandas as pd
import matplotlib.pyplot as plt

# 创建数据字典
data = {
    "Experiment ID": [
        "FinalMLP_movielenslatest_x1_001_25b6333c", "FinalMLP_movielenslatest_x1_002_72fddffa",
        "FinalMLP_movielenslatest_x1_003_321426fe", "FinalMLP_movielenslatest_x1_004_498f3e4f",
        "FinalMLP_movielenslatest_x1_005_c4fb69b1", "FinalMLP_movielenslatest_x1_006_d3e7c3b6",
        "FinalMLP_movielenslatest_x1_007_d5f5ef88", "FinalMLP_movielenslatest_x1_008_c7c48c68",
        "FinalMLP_movielenslatest_x1_009_2f3f200b", "FinalMLP_movielenslatest_x1_010_76b63456",
        "FinalMLP_movielenslatest_x1_011_937df0b7", "FinalMLP_movielenslatest_x1_012_4bd3069e"
    ],
    "Test AUC": [
        0.970520, 0.969598, 0.969072, 0.972273, 0.970139, 0.969313,
        0.968396, 0.971676, 0.968757, 0.969410, 0.967629, 0.971345
    ],
    "Test Log Loss": [
        0.215097, 0.213058, 0.207250, 0.209233, 0.267519, 0.211724,
        0.247412,0.226484, 0.214278, 0.268805, 0.212654, 0.226768
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
plt.savefig('D:\\PapersCode\\FinalMLP\\result_csv\\FinalMLP_movielenslatest.png', dpi=300)

# 显示图表
plt.show()
