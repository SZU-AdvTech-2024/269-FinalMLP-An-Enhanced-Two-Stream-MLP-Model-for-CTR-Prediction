import pandas as pd

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
styled_df.to_excel('D:\\PapersCode\\FinalMLP\\result_csv\\FinalMLP_criteo_results.xlsx', engine='openpyxl', index=False)

# 输出美化后的 DataFrame
styled_df
