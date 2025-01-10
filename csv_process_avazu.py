import pandas as pd

# 提取的数据
data = {
    "Experiment ID": [
        "FinalMLP_avazu_x1_001_c4b833c5", "FinalMLP_avazu_x1_002_307dfeae", "FinalMLP_avazu_x1_003_9b06b11d",
        "FinalMLP_avazu_x1_004_363dec26", "FinalMLP_avazu_x1_005_55ba240d"
    ],
    "Test AUC": [
        0.765725, 0.765919, 0.763614, 0.765927, 0.766034
    ],
    "Test Log Loss": [
        0.376487, 0.366085, 0.367718, 0.365873, 0.365935
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
styled_df.to_excel('D:\\PapersCode\\FinalMLP\\result_csv\\FinalMLP_avazu_results.xlsx', engine='openpyxl', index=False)

# 输出美化后的 DataFrame
styled_df
