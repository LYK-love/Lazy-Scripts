#!python
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

def generate_image_url(object_name, bucket_name, endpoint):
    '''
    Given image path, bucket name and endpoint, print the url of the image.
    '''


    target_url = f"https://{quote(bucket_name)}.{quote(endpoint)}/{quote(object_name)}"
    return target_url


def encode_to_ascii(text):
    encoded_text = ""
    for char in text:
        encoded_text += str(ord(char)) + " "
    return encoded_text.strip()


def convert_to_url(fileName):
    encoded_fileName = quote(fileName)
    url = "https://" + encoded_fileName
    return url


if __name__ == "__main__":
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
    function_completer = WordCompleter(["generate_image_url"])

    # 创建 PromptSession 对象
    session = PromptSession()

    print(f'''
    Utils for Aliyun OSS.
    
    Operations:
    * generate_image_url: {generate_image_url.__doc__}
    '''
          )

    # 选择要执行的函数
    function = session.prompt("Please select operation: ", completer=function_completer)

    # 根据选择的函数调用相应的函数
    if function == "generate_image_url":
        BucketName = session.prompt("Please enter bucket name: ", default='lyk-love')
        Endpoint = session.prompt("Please enter your end point: ", default='oss-cn-shanghai.aliyuncs.com')
        image_path = session.prompt("Please enter your image path under the bucket: ", default='XX/XX.png')
        share_link = generate_image_url(image_path, BucketName, Endpoint)
        print(f"Link: {share_link}")

        print("The text has been copied to your clipboard")
        pyclip.copy(share_link)

    else:
        print("Feature not supported.")



