#!python
import os
import subprocess
from urllib.parse import quote

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
import pyclip

'''
https://help.aliyun.com/document_detail/39607.html

公共读Object
如果文件的读写权限ACL为公共读，即该文件允许匿名访问，则文件URL的格式为:

https://BucketName.Endpoint/ObjectName

其中，ObjectName需填写包含文件夹以及文件后缀在内的该文件的完整路径。各地域的Endpoint信息介绍，请参见访问域名和数据中心。

例如华东1（杭州）地域下名为examplebucket的Bucket下有名为example的文件夹，文件夹内有个名为example.jpg的文件。则该文件URL为：

外网访问URL：https://examplebucket.oss-cn-hangzhou.aliyuncs.com/example/example.jpg
内网访问URL（供同地域ECS实例访问）：https://examplebucket.oss-cn-hangzhou-internal.aliyuncs.com/example/example.jpg
'''


def generate_image_url(image_relative_path, bucket_name, endpoint):
    '''
    Given image path, bucket name and endpoint, print the url of the image.
    '''

    target_url = f"https://{quote(bucket_name)}.{quote(endpoint)}/{quote(image_relative_path)}"
    return target_url


def upload_image_to_oss(image_path, target_relative_image_path, bucket_name):
    '''
    ossutil cp "<image_path>" "oss://<bucket_name>/<target_relative_image_path>"
    '''
    command = f'ossutil cp "{image_path}" "oss://{bucket_name}/{target_relative_image_path}"'
    try:
        subprocess.run(command, shell=True, check=True)
        print(f'Successfully uploaded {image_path} to OSS.')
    except subprocess.CalledProcessError as e:
        print(f'Error uploading {image_path} to OSS. Error: {e}.')


def upload_images_to_oss(directory_root, directory_relative_path, bucket_name):
    '''
    ossutil cp "<directory_path>" "oss://<bucket_name>/<target_relative_dir_path>" --include "*" -r
    '''
    directory_path = os.path.join(directory_root, directory_relative_path)
    target_relative_dir_path = directory_relative_path

    command = f'ossutil cp "{directory_path}" "oss://{bucket_name}/{target_relative_dir_path}" --include "*" -r'
    try:
        subprocess.run(command, shell=True, check=True)
        print(f'Successfully uploaded images under {directory_path} to OSS.')
        image_paths = __get_image_paths(directory_path)
        for image_path in image_paths:
            print(image_path)
        print(f"Total number: {len(image_paths)}")

    except subprocess.CalledProcessError as e:
        print(f'Error uploading {directory_path} to OSS. Error: {e}.')


def __get_image_paths(directory_path):
    image_paths = []

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
            file_path = os.path.join(root, file)
            image_paths.append(file_path)

    return image_paths


def encode_to_ascii(text):
    encoded_text = ""
    for char in text:
        encoded_text += str(ord(char)) + " "
    return encoded_text.strip()


def convert_to_url(fileName):
    encoded_fileName = quote(fileName)
    url = "https://" + encoded_fileName
    return url


def test():
    BucketName = 'lyk-love'
    Endpoint = 'oss-cn-shanghai.aliyuncs.com'

    DirectoryRoot = "/Users/lyk/Pictures/HexoPics"
    DirectoryRelativePath = "Software Engineering/Tips for Remote Development"
    DirectoryPath = os.path.join(DirectoryRoot, DirectoryRelativePath)
    image_paths = __get_image_paths(DirectoryPath)
    for image_path in image_paths:
        image_relative_path = os.path.relpath(image_path, DirectoryRoot)
        share_link = generate_image_url(image_relative_path, BucketName, Endpoint)
        print(f"{share_link}")

if __name__ == "__main__":
    # test()
    '''
    https://lyk-love.oss-cn-shanghai.aliyuncs.com/Study-Abroad/WES/Xuexinwang%20Sending%20through%20Email.png
    https://lyk-love.oss-cn-shanghai.aliyuncs.com/Study-Abroad/WES/Xuexinwang%20Sending%20through%20Email.png
    '''
    # BucketName = "lyk-love"
    # Endpoint = "oss-cn-shanghai.aliyuncs.com"  # 华东2(上海)
    #
    # image_path = "Algorithm/Linkedlist Algorithms/Reverse the Linkedlist.png"
    #
    # share_link = generate_image_url(image_path, BucketName, Endpoint)
    # print(share_link)

    # 创建可补全的选项列表
    function_completer = WordCompleter(["generate_image_url", "upload_image_to_oss", "upload_images_to_oss"])

    # 创建 PromptSession 对象
    session = PromptSession()

    print(f'''
    Utils for [Aliyun OSS](https://cn.aliyun.com/product/oss?from_alibabacloud=), leveraging the [osssutil](https://www.alibabacloud.com/help/en/oss/developer-reference/overview-59) tool by Aliyun.
    
    Operations:
    * generate_image_url
    * upload_image_to_oss
    * upload_images_to_oss
    '''
          )

    # 选择要执行的函数
    function = session.prompt("Please select operation: ", completer=function_completer)

    # 根据选择的函数调用相应的函数
    if function == "generate_image_url":
        BucketName = session.prompt("Please enter bucket name: ", default='lyk-love')
        Endpoint = session.prompt("Please enter your end point: ", default='oss-cn-shanghai.aliyuncs.com')
        while True:
            image_relative_path = session.prompt("Please enter your image path under the bucket: ", default='XX/XX.png')
            share_link = generate_image_url(image_relative_path, BucketName, Endpoint)
            print(f"Link for sharing: {share_link}")

            print("The text has been copied to your clipboard")
            pyclip.copy(share_link)
    elif function == "upload_images_to_oss":
        BucketName = session.prompt("Please enter bucket name: ", default='lyk-love')
        print(f"Your image will be uploaded under the remote root: oss://{BucketName}")

        Endpoint = session.prompt("Please enter your end point: ", default='oss-cn-shanghai.aliyuncs.com')
        DirectoryRoot = session.prompt("Your local image root path: ", default="/Users/lyk/Pictures/HexoPics")
        DirectoryRelativePath = session.prompt("Your local relative path under the local root: ", default='Algorithm')
        upload_images_to_oss(DirectoryRoot, DirectoryRelativePath, BucketName)

        print("Link for sharing:")
        DirectoryPath = os.path.join(DirectoryRoot,DirectoryRelativePath)
        image_paths = __get_image_paths(DirectoryPath)
        for image_path in image_paths:
            image_relative_path = os.path.relpath(image_path, DirectoryRoot)
            share_link = generate_image_url(image_relative_path, BucketName, Endpoint)
            print(f"{share_link}")

    elif function == "upload_image_to_oss":
        BucketName = session.prompt("Please enter bucket name: ", default='lyk-love')
        print(f"Your image will be uploaded under the remote root: oss://{BucketName}")

        Endpoint = session.prompt("Please enter your end point: ", default='oss-cn-shanghai.aliyuncs.com')
        DirectoryRoot = session.prompt("Your local image root path: ", default="/Users/lyk/Pictures/HexoPics")

        while True:
            image_relative_path = session.prompt("Your local image path under the local root: ", default='XX/XX.png')
            target_relative_path = session.prompt("Your target image path under the remote root: ", default='XX/XX.png')
            image_path = os.path.join(DirectoryRoot, image_relative_path)
            upload_image_to_oss(image_path, target_relative_path, BucketName)

            # Copy the remote image path
            share_link = generate_image_url(image_relative_path, BucketName, Endpoint)
            print(f"Link for sharing: {share_link}")
            print("The text has been copied to your clipboard")
            pyclip.copy(share_link)


    else:
        print("Feature not supported.")
