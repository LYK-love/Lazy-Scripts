import os
import shutil

def get_human_readable_size(size):
    # 根据文件大小自动确定合适的单位（B、KB、MB、GB、TB）
    units = ["B", "KB", "MB", "GB", "TB"]
    index = 0
    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1
    return f"{size:.2f} {units[index]}"

def get_largest_files(folder_path, num_files):
    files = []
    for root, dirs, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            file_size = os.path.getsize(file_path)
            files.append((file_path, file_size))

    files.sort(key=lambda x: x[1], reverse=True)  # 按文件大小排序

    largest_files = files[:num_files]  # 获取最大的几个文件

    return largest_files

def delete_files(file_list):
    for file_info in file_list:
        file_path, _ = file_info
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
            print(f"Deleted folder: {file_path}")


if __name__ == "__main__":

    # 定义要搜索的文件夹路径和要删除的文件数量
    folder_path = '/Users/lyk/Projects/MyOfficialProjects/VolatileReborn copy'  # 替换为实际的文件夹路径
    num_files = 5  # 替换为要删除的最大文件数量

    # 获取最大文件列表
    largest_files = get_largest_files(folder_path, num_files)

    # 删除最大文件
    delete_files(largest_files)

