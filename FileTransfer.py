import os
import paramiko
from stat import S_ISDIR
from colorama import Fore, Style
from tqdm import tqdm

def download_file(sftp, remote_path, local_path):
    """
    Download a file with a progress bar.
    """
    # Obtain file size
    file_info = sftp.stat(remote_path)
    file_size = file_info.st_size

    with tqdm(total=file_size, unit='B', unit_scale=True, desc=f"Downloading {remote_path}", leave=True) as pbar:
        def file_transfer_callback(transferred, to_be_transferred):
            pbar.update(transferred - pbar.n)  # Update progress bar with bytes transferred

        sftp.get(remote_path, local_path, callback=file_transfer_callback)
    print(f"{Fore.GREEN}Downloaded to {local_path}{Style.RESET_ALL}")
    print()

def download_recursive(sftp, remote_dir, local_dir):
    """
    Recursively download files from a remote directory that match specified extensions.
    """
    # Ensure the local directory exists
    os.makedirs(local_dir, exist_ok=True)

    # List all items in the remote directory
    for entry in sftp.listdir_attr(remote_dir):
        remote_item_path = os.path.join(remote_dir, entry.filename)
        local_item_path = os.path.join(local_dir, entry.filename)

        # Check if the entry is a directory
        if S_ISDIR(entry.st_mode):
            # Recursively navigate into the directory
            download_recursive(sftp, remote_item_path, local_item_path)
        elif remote_item_path.endswith('.mp4') or remote_item_path.endswith('.png'):
            # Download the file with a progress bar
            download_file(sftp, remote_item_path, local_item_path)

if __name__ == "__main__":
    import paramiko
    from colorama import init

    # Initialize colorama
    init()

    hostname = os.getenv('LAB_IP')
    username = os.getenv('LAB_USERNAME')
    password = os.getenv('LAB_PASSWD')
    remote_path = input(f"{Fore.CYAN}Enter the remote path: {Style.RESET_ALL}") or os.getenv('LAB_DIR_PATH')
    local_path = input(f"{Fore.CYAN}Enter the local path: {Style.RESET_ALL}") or os.getenv('LOCAL_DIR_PATH')


