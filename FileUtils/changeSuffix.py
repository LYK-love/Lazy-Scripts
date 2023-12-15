import os

def rename_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.HEIC'):
                old_filepath = os.path.join(root, filename)
                new_filepath = os.path.join(root, filename.rsplit('.', 1)[0] + '.jpeg')
                os.rename(old_filepath, new_filepath)


directory_path = '/Users/lyk/Library/Mobile Documents/com~apple~CloudDocs/Medical Info/Examination Record'

rename_files_in_directory(directory_path)
