import pandas as pd

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

# 计算每列的平均值和标准差
mean_values = df[["Test AUC", "Test Log Loss"]].mean()
std_values = df[["Test AUC", "Test Log Loss"]].std()

# 创建统计数据行
summary = pd.DataFrame({
    "Experiment ID": ["Average", "Standard Deviation"],
    "Test AUC": [mean_values["Test AUC"], std_values["Test AUC"]],
    "Test Log Loss": [mean_values["Test Log Loss"], std_values["Test Log Loss"]]
})

# 合并原始数据和统计数据
final_df = pd.concat([df, summary], ignore_index=True)

# 使用 pandas Styler 美化表格
styled_df = final_df.style.format({
    "Test AUC": "{:.4f}",
    "Test Log Loss": "{:.4f}"
}).set_table_styles([
    {"selector": "thead th", "props": [("background-color", "#f2f2f2"), ("font-weight", "bold"), ("text-align", "center")]},
    {"selector": "tbody td", "props": [("text-align", "center")]},
    {"selector": "tr:nth-child(even)", "props": [("background-color", "#f9f9f9")]},
    {"selector": "tr:nth-child(odd)", "props": [("background-color", "#ffffff")]},
    {"selector": "tfoot td", "props": [("font-weight", "bold"), ("background-color", "#f2f2f2")]},
])

# 将结果保存为 Excel 文件
styled_df.to_excel('D:\\PapersCode\\FinalMLP\\result_csv\\FinalMLP_movielenslatest_results.xlsx', engine='openpyxl', index=False)

# 输出美化后的 DataFrame
styled_df

