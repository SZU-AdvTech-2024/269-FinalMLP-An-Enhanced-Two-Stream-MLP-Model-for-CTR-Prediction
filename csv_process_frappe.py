import pandas as pd

# 提取的数据
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
styled_df.to_excel('D:\\PapersCode\\FinalMLP\\result_csv\\FinalMLP_frappe_results.xlsx', engine='openpyxl', index=False)

# 输出美化后的 DataFrame
styled_df
