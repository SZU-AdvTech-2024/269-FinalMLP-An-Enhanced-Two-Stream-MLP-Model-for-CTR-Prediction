import h5py

# 假设 'your_data_file.h5' 是你的HDF5文件路径
with h5py.File('D:\\PapersCode\\FinalMLP2\\data\Frappe\\frappe_x1_47e6e0df\\test.h5', 'r') as f:
    print(list(f.keys()))  # 打印出所有键

    # 检查 'item' 键是否存在
    if 'item' in f:
        print("'item' key exists in the HDF5 file.")
    else:
        print("'item' key does not exist in the HDF5 file.")