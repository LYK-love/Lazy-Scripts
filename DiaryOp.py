import re


def changeTitle(filename):

    with open(filename, "r") as file:
        content = file.read()

    # Define the pattern to match subtitles (##) at the beginning of the line
    '''
    In the given regular expression pattern ^(##)(.*)$, there are two capturing groups:

    (##): This captures the "##" at the beginning of the line.
    (.*): This captures the rest of the content on the line.
    When the regular expression matches a line with a subtitle, the backreference \2 refers to the captured content of the second group, which is the remaining c   ontent on the line after the "##" subtitle.

    '''
    pattern = r"^(##)(.*)$"
    replacement = r"#\2"

    # Use regex to perform the substitution
    modified_content = re.sub(pattern, replacement, content, flags=re.MULTILINE)

    # Write the modified content back to the file
    with open(filename, "w") as file:
        file.write(modified_content)
        
        
def changeDirname(filename):
    with open(filename, "r") as file:
        content = file.read()

    # Define the pattern to match "assets2022"
    pattern = r"assets2022"
    replacement = r"assets 2022"

    # Use regex to perform the substitution
    modified_content = re.sub(pattern, replacement, content)
    
    # Write the modified content back to the file
    with open(filename, "w") as file:
        file.write(modified_content)

if __name__ == "__main__":
    '''
    Python range() function generates the immutable sequence of numbers starting from the given start integer to the stop integer. 
    The range() is a built-in function that returns a range object that consists series of **integer** numbers, which we can iterate using a for loop.
    '''
    # for month in range(4,6): # [4, 5]
    #     filename = f"Diary2023_{month}.md"
    #     print(f"Processing fiale {filename}")
    #     changeTitle(filename)
    
    # for year in range(0,3): 
    #    filename = f"../Diary 202{year}.md" # 2020, 2021, 2022
    #    changeTitle(filename)
    filename = "../Diary 2022/Diary 2022.md"
    changeDirname(filename)
   

