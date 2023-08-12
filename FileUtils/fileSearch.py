import os
import shutil

def search_and_delete(folder_path, target_folders):
    '''
    在{folder_path}下寻找目标目录并且删除.
    '''
    for root, dirs, files in os.walk(folder_path):
        '''
        递归地搜索以{folder_path}为根节点的整个文件树. 
        For each directory in the directory tree rooted at top (including top
    itself, but excluding '.' and '..'), yields a 3-tuple

        dirpath, dirnames, filenames

    dirpath is a string, the path to the directory.  dirnames is a list of
    the names of the subdirectories in dirpath (including symlinks to directories,
    and excluding '.' and '..').
    filenames is a list of the names of the non-directory files in dirpath.
    Note that the names in the lists are just names, with no path components.
    To get a full path (which begins with top) to a file or directory in
    dirpath, do os.path.join(dirpath, name).
        '''
        for target_folder in target_folders:
            if target_folder in dirs:
                folder_to_delete = os.path.join(root, target_folder)
                shutil.rmtree(folder_to_delete)
                print(f"Deleted folder: {folder_to_delete}")


if __name__ == "__main__":
    # 定义要搜索和删除的目标文件夹列表
    is_backend_project = True
    is_frontend_project = False

    # 后端项目需要删除target文件夹
    if is_backend_project:
        target_folders = ['target']

    # 前端项目需要删除dist, node_modules
    if is_frontend_project:
        target_folders = ['dist', 'node_modules']

    # 定义包含项目的文件夹路径
    project_folder = '/Users/lyk/Projects/MyOfficialProjects/VolatileReborn copy'  # 替换为实际的文件夹路径

    # 调用函数搜索并删除目标文件夹
    search_and_delete(project_folder, target_folders)
