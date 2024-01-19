import paramiko
import os

if __name__ == "__main__":
    '''
    Trainslate files on remote server to local machine.
    You need to set following env variables:
    LAB_IP = <you server's hostname or ip>
    LAB_USERNAME = <the username of your user account on your server>
    LAB_PASSWD = <the passwd of your user account on your server>
    LAB_DIR_PATH = <the dir where the file you desire to download lies>
    LOCAL_DIR_PATH = <destination of downloaded file>
    '''
    hostname = os.getenv('LAB_IP')
    username = os.getenv('LAB_USERNAME')
    password = os.getenv('LAB_PASSWD')
    remote_path = os.getenv('LAB_DIR_PATH')
    local_path = os.getenv('LOCAL_DIR_PATH')

    # Connect to the server
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname, username=username, password=password)

    # Use SFTP for file transfer
    sftp = ssh_client.open_sftp()

    try:
        # List all files in the remote directory
        files = sftp.listdir(remote_path)
        for file in files:
            if file.endswith('.mp4'):  # assuming video files are in mp4 format
                remote_file_path = os.path.join(remote_path, file)
                local_file_path = os.path.join(local_path, file)
                print(f"Downloading {file}...")
                sftp.get(remote_file_path, local_file_path)
                print(f"Downloaded {file} to {local_file_path}")
    finally:
        sftp.close()
        ssh_client.close()

    print("All files downloaded.")

