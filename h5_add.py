import h5py
import torch
import os

# 确保.h5文件的路径存在
h5_file_path = 'D:\\PapersCode\\FinalMLP\\data\\Movielens\\movielenslatest_x1_233328b6\\test.h5'
if not os.path.dirname(h5_file_path):
    os.makedirs(os.path.dirname(h5_file_path), exist_ok=True)

# 加载.pt文件中的嵌入数据
try:
    embeddings = torch.load('D:\\PapersCode\\FinalMLP\\data\\Movielens\\MovielensLatest_x1\\test_embeddings.pt')
except FileNotFoundError:
    print("Error: The file 'test_embeddings.pt' does not exist.")
    exit(1)
except Exception as e:
    print(f"An error occurred while loading the embeddings: {e}")
    exit(1)

# 打开.h5文件，如果文件不存在则创建
try:
    with h5py.File(h5_file_path, 'a') as h5f:
        # 检查.h5文件中是否已经存在text列，如果不存在则创建
        if 'text' not in h5f:
            # 创建一个新的数据集，形状为(0, embeddings.shape[1])，dtype为float32
            # 这里假设embeddings的形状为(num_samples, embedding_dim)
            dataset = h5f.create_dataset('text', (0, embeddings.shape[1]), maxshape=(None, embeddings.shape[1]),
                                         dtype='float32')
        else:
            dataset = h5f['text']

        # 将嵌入数据追加到数据集
        current_size = dataset.shape[0]
        dataset.resize((current_size + embeddings.shape[0], embeddings.shape[1]))
        dataset[current_size:, :] = embeddings.numpy()
except Exception as e:
    print(f"An error occurred while writing to the HDF5 file: {e}")
    exit(1)

print(f"Embeddings saved to {h5_file_path}")