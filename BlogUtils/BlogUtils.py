import os
import frontmatter
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

def filter_md_files(directory_path, key_in_meta_data, value_of_corresponding_key):
    md_files = __filter_md_files(directory_path, key_in_meta_data, value_of_corresponding_key)

    if md_files:
        print(f"Find markdown files in {directory_path} with {key_in_meta_data}: {value_of_corresponding_key}.")
        for md_file in md_files:
            print(md_file)
        print(f"Total number: {len(md_files)}")
    else:
        print(f"No Markdown files found.")

def __filter_md_files(directory, key, value):
    markdown_files = []
    paths = __list_md_files(directory)
    for file_path in paths:
        with open(file_path, 'r') as file:
            post = frontmatter.load(file)
            metadata = post.metadata
            if key in metadata and metadata[key] is not None:
                values_of_that_key = collect_elements(metadata[key])
                if value in values_of_that_key:
                    markdown_files.append(file_path)
    return markdown_files


def list_md_files(directory_path):
    md_files = __list_md_files(directory_path)

    if md_files:
        print(f"Find markdown files in {directory_path}:")
        for md_file in md_files:
            print(md_file)
        print(f"Total number: {len(md_files)}")
    else:
        print(f"No Markdown files found in {directory_path}.")


def __list_md_files(directory):
    markdown_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                markdown_files.append(file_path)

    return markdown_files

def update_md_files(directory_path, key_in_mata_data, old_value, new_value):
    md_files = __update_md_files(directory_path, key_in_mata_data, old_value, new_value)


    if md_files:
        print(f"Updated markdown files in {key_in_mata_data}. Paths: ")
        for md_file in md_files:
            print(md_file)
        print(f"Total number: {len(md_files)}")
    else:
        print("No Markdown files updated in the specified category.")

def __update_md_files(directory, key, old_value, new_value):
    changed_markdown_files = []

    paths = __list_md_files(directory)
    for file_path in paths:
        should_be_updated = False
        with open(file_path, 'r+', encoding='utf-8') as file:
            post = frontmatter.load(file)
            metadata = post.metadata

            if key in metadata and metadata[key] is not None:
                values_of_that_key = collect_elements(metadata[key])
                if old_value in values_of_that_key:
                    should_be_updated = True
                    values_of_that_key.remove(old_value)
                    values_of_that_key.append(new_value)
                    metadata[key] = values_of_that_key
                    changed_markdown_files.append(file_path)

        if should_be_updated is True:
            with open(file_path, 'wb') as file:
                frontmatter.dump(post, file)

    return changed_markdown_files

# def sort_md_files(directory):




def collect_elements( obj):
    '''
    Given obj, it may be a list of string/int, may be a list of lists of string, may be a list of lists of lists of ...
    Return the string/int value(s) in obj in a 1-D array
    '''
    result = []

    if not isinstance(obj, list):
        result.append(obj)
    else:
        for item in obj:
            if not isinstance(obj, list):
                result.append(item)
            else:
                result.extend(collect_elements(item)) # This func returns a 1-D array. So we append all it's return elements to the end of "result".

    return result

def test():
    DirectoryPath = "/Users/lyk/Documents/LYK-love.github.io/source/_posts"
    KeyToFilter = 'categories'
    OldValue = "Affairs"
    NewValue = "Life Affairs"
    update_md_files(DirectoryPath, KeyToFilter, OldValue, NewValue)

if __name__ == "__main__":
    test()

    # 创建可补全的选项列表
    function_completer = WordCompleter(["list_md_files", "filter_md_files", "update_md_files"])

    # 创建 PromptSession 对象
    session = PromptSession()

    print(f'''
    Utils for Hexo Blog Files.
    Every file has a [frontmatter](https://pypi.org/project/python-frontmatter/):

    ---
    title: Design Pattern
    tags: Software Engineering
    categories: Computer Science
    date: 2022-03-15 12:00:00
    ---
    
    Operations:
    * list_md_files
    * filter_md_files
    * update_md_files
    '''
          )

    # 选择要执行的函数
    function = session.prompt("Please select operation: ", completer=function_completer)

    DirectoryRoot = "/Users/lyk/Documents/LYK-love.github.io/source"
    DefaultDirectoryPath = DirectoryRoot + "/_posts"
    # 根据选择的函数调用相应的函数
    if function == "list_md_files":

        DirectoryPath = session.prompt("Directory path: ", default=DefaultDirectoryPath)
        list_md_files(DirectoryPath)

    elif function == "filter_md_files":
        DirectoryPath = session.prompt("Directory path: ", default=DefaultDirectoryPath)
        KeyToFilter = session.prompt("Key to filter: ", default='categories')
        ValueToFilter = session.prompt("Value of the key to filter: ", default='Computer Science')

        filter_md_files(DirectoryPath, KeyToFilter, ValueToFilter)
    elif function == "update_md_files":
        DirectoryPath = session.prompt("Directory path: ", default=DefaultDirectoryPath)
        KeyToFilter = session.prompt("Key to filter: ", default='categories')
        OldValue = session.prompt("Old Value of the key to update: ")
        NewValue = session.prompt("New Value of the key: ")
        update_md_files(DirectoryPath, KeyToFilter, OldValue, NewValue)
    else:
        print("Feature not supported.")
