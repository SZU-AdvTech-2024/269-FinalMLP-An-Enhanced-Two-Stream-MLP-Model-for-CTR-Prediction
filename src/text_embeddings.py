import os
import torch
from transformers import BertTokenizer, BertModel
import pandas as pd

# 初始化 BERT 模型和 Tokenizer
model_dir = "D:/PapersCode/FinalMLP2/bert-base-uncased"

# 加载本地分词器
tokenizer = BertTokenizer.from_pretrained(model_dir)

# 加载本地模型
bert_model = BertModel.from_pretrained(model_dir)

def process_and_save_text(data, column_name, save_path, tokenizer, bert_model, max_length=128, batch_size=32,
                          device='cpu'):
    """
    处理文本数据并保存为嵌入文件。

    参数:
        data (pd.DataFrame): 数据集。
        column_name (str): 文本列的名称。
        save_path (str): 嵌入保存路径。
        tokenizer: BERT Tokenizer。
        bert_model: BERT 模型。
        max_length (int): 文本最大长度。
        batch_size (int): 每批次的文本数量。
        device (str): 计算设备，'cpu' 或 'cuda'。
    """
    texts = data[column_name].tolist()
    bert_model.to(device)
    embeddings = []

    # 分批处理文本数据
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i + batch_size]
        inputs = tokenizer(
            batch_texts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=max_length
        ).to(device)

        with torch.no_grad():
            outputs = bert_model(**inputs)
            batch_embeddings = outputs.last_hidden_state[:, 0, :]  # 提取 [CLS] 标记的嵌入

        embeddings.append(batch_embeddings.cpu())  # 转回 CPU，防止显存占用

    # 拼接所有嵌入并保存到文件
    embeddings = torch.cat(embeddings, dim=0)
    torch.save(embeddings, save_path)
    print(f"Embeddings saved to {save_path}")

# 数据集路径
data_dir = r"D:\\PapersCode\\FinalMLP\\data\\Movielens\\MovielensLatest_x1"
os.makedirs(data_dir, exist_ok=True)

# 加载数据
train_data = pd.read_csv(os.path.join(data_dir, "train_nl.csv"))
valid_data = pd.read_csv(os.path.join(data_dir, "valid_nl.csv"))
test_data = pd.read_csv(os.path.join(data_dir, "test_nl.csv"))

# 嵌入保存路径
train_path = os.path.join(data_dir, "train_embeddings.pt")
valid_path = os.path.join(data_dir, "valid_embeddings.pt")
test_path = os.path.join(data_dir, "test_embeddings.pt")

# 处理训练集
process_and_save_text(
    data=train_data,
    column_name="text",
    save_path=train_path,
    tokenizer=tokenizer,
    bert_model=bert_model,
    device="cuda" if torch.cuda.is_available() else "cpu"
)

# 处理验证集
process_and_save_text(
    data=valid_data,
    column_name="text",  # 替换为实际的文本列名
    save_path=valid_path,
    tokenizer=tokenizer,
    bert_model=bert_model,
    device="cuda" if torch.cuda.is_available() else "cpu"
)

# 处理测试集
process_and_save_text(
    data=test_data,
    column_name="text",  # 替换为实际的文本列名
    save_path=test_path,
    tokenizer=tokenizer,
    bert_model=bert_model,
    device="cuda" if torch.cuda.is_available() else "cpu"
)
