#!python
import os
import paramiko
from stat import S_ISDIR
from colorama import Fore, Style
from tqdm import tqdm

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from colorama import init


def is_media_file(filename):
    """
    Check if the filename belongs to a media file.
    """
    # Define media file extensions
    MEDIA_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.mp4', '.avi']
    return any(filename.endswith(ext) for ext in MEDIA_EXTENSIONS)


def is_checkpoint_file(filename):
    """
    Check if the filename belongs to a media file.
    """
    # Define media file extensions
    CKPT_EXTENSIONS = ['.ckpt']
    return any(filename.endswith(ext) for ext in CKPT_EXTENSIONS)


def is_text_file(filename):
    """
    Check if the filename belongs to a media file.
    """
    # Define media file extensions
    TEXT_EXTENSIONS = ['.txt', '.md', '.yaml', '.yml']
    return any(filename.endswith(ext) for ext in TEXT_EXTENSIONS)


def is_major_file(filename):
    """
    Check if the filename belongs to a major file. A major file is a media/checkpoint/txt file.
    """
    is_major = is_media_file(filename) or is_checkpoint_file(filename) or is_text_file(filename)
    return is_major


def download_file(sftp, remote_path, local_path):
    """
    Download a file with a progress bar. Ask user whether to override if the file already exists.
    """
    # Check if the file already exists
    if os.path.exists(local_path):
        user_input = input(
            f"The file {os.path.basename(local_path)} already exists. Do you want to override it? (y/n): ").strip().lower()
        if user_input != 'y':
            print(f"Skipping download of {os.path.basename(local_path)}")
            return  # Skip downloading this file

    # Obtain file size
    file_info = sftp.stat(remote_path)
    file_size = file_info.st_size

    with tqdm(total=file_size, unit='B', unit_scale=True, desc=f"Downloading {os.path.basename(remote_path)}",
              leave=True) as pbar:
        def file_transfer_callback(transferred, to_be_transferred):
            pbar.update(transferred - pbar.n)  # Update progress bar with bytes transferred

        sftp.get(remote_path, local_path, callback=file_transfer_callback)
    print(f"{Fore.GREEN}Downloaded to {local_path}{Style.RESET_ALL}")
    print()


def download_recursive(sftp, remote_dir, local_dir, is_flat=True, option='media'):
    """
    Recursively download files from a remote directory based on file_type.
    """
    os.makedirs(local_dir, exist_ok=True)

    for entry in sftp.listdir_attr(remote_dir):
        remote_item_path = os.path.join(remote_dir, entry.filename)

        if S_ISDIR(entry.st_mode):
            if is_flat:
                download_recursive(sftp, remote_item_path, local_dir, is_flat, option)
            else:
                download_recursive(sftp, remote_item_path, os.path.join(local_dir, entry.filename), is_flat, option)
        else:
            if option == 'all' or (option == 'media' and is_media_file(entry.filename)) or (
                    option == 'major' and is_major_file(entry.filename)):
                download_file(sftp, remote_item_path, os.path.join(local_dir, entry.filename))


def download_remote_file(hostname, username, password, remote_path, local_path, is_flat=True, option='media'):
    # Connect to the server
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname, username=username, password=password)

    # Use SFTP for file transfer
    sftp = ssh_client.open_sftp()

    try:
        download_recursive(sftp, remote_path, local_path, is_flat, option)
    finally:
        sftp.close()
        ssh_client.close()

    print(f"{Fore.YELLOW}All files downloaded.{Style.RESET_ALL}")


def test():
    pass


if __name__ == "__main__":
    # test()

    # Initialize colorama
    init()

    # 创建可补全的选项列表
    function_completer = WordCompleter(["download_directory", "download_file_flat"])

    # 创建 PromptSession 对象
    session = PromptSession()

    print(f'''
   
    Operations:
    * download_directory: Download the directory from remote path recursively under a local directory.
    * download_file_flat: Download all files from remote path recursively to a local directory at the same level
    '''
          )

    # 选择要执行的函数
    function = session.prompt("Please select operation: ", completer=function_completer)

    default_hostname = os.getenv('LAB_IP')
    default_username = os.getenv('LAB_USERNAME')
    default_password = os.getenv('LAB_PASSWD')
    default_remote_path = os.getenv('LAB_DIR_PATH')
    default_local_path = os.getenv('LOCAL_DIR_PATH')
    hostname = default_hostname
    username = default_username
    password = default_password

    remote_path = session.prompt(f"Enter the remote path: ", default=default_remote_path)
    local_path = session.prompt(f"Enter the local path: ", default=default_local_path)

    option = session.prompt(f"Enter one option to choose file types to download. Options: [media, major, all]: ",
                            default='media')

    # 根据选择的函数调用相应的函数
    if function == "download_directory":
        download_remote_file(hostname, username, password, remote_path, local_path, is_flat=False, option=option)
    elif function == "download_file_flat":
        download_remote_file(hostname, username, password, remote_path, local_path, is_flat=True, option=option)

    else:
        print("Feature not supported.")
