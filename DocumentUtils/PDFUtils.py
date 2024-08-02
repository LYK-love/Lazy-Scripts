
import PyPDF2

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

def split_pdf(input_file, output_file_1, output_file_2, index):
    '''
    Split the original PDF file to two PDF files by given {index}.
    The two split files are: [0, index), [index, ...)
    '''
    with open(input_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # 创建第一个输出文档，只包含[0, index)页
        writer_1 = PyPDF2.PdfWriter()
        writer_1.add_page(reader.pages[index])
        with open(output_file_1, 'wb') as output_1:
            writer_1.write(output_1)

        # 创建第二个输出文档，包含[index, ...)页
        writer_2 = PyPDF2.PdfWriter()
        for page in reader.pages[index:]:
            writer_2.add_page(page)
        with open(output_file_2, 'wb') as output_2:
            writer_2.write(output_2)



def merge_pdfs_together(input_files, output_file):
    '''
    合并多个PDF文件为一个PDF文件
    '''
    pdf_merger = PyPDF2.PdfMerger()

    for pdf_file in input_files:
        with open(pdf_file, 'rb') as file:
            pdf_merger.append(file)

    with open(output_file, 'wb') as output:
        pdf_merger.write(output)

def merge_pdfs(input_file_A, input_file_B, output_file, index):
    """
    Merge PDF file B to  PDF file A by given {index}.
    Merged PDF = A[0, ..., index), B, A[index, ...)

    """
    # 打开第一个输入文档
    with open(input_file_A, 'rb') as file_1:
        reader_1 = PyPDF2.PdfReader(file_1)

        # 打开第二个输入文档
        with open(input_file_B, 'rb') as file_2:
            reader_2 = PyPDF2.PdfReader(file_2)

            # 创建输出文档
            writer = PyPDF2.PdfWriter()

            # 将第一个输入文档的前index页添加到输出文档
            for page in reader_1.pages[:index]:
                writer.add_page(page)

            # 将第二个输入文档的所有页添加到输出文档
            for page in reader_2.pages:
                writer.add_page(page)

            # 将第一个输入文档的剩余页添加到输出文档
            for page in reader_1.pages[index:]:
                writer.add_page(page)

            # 保存输出文档
            with open(output_file, 'wb') as output:
                writer.write(output)


if __name__ == "__main__":


    # 创建可补全的选项列表
    function_completer = WordCompleter(["split", "merge"])

    # 创建 PromptSession 对象
    session = PromptSession()

    print(f'''Operations:
    split: {split_pdf.__doc__}
    merge: {merge_pdfs.__doc__}
    merge_pdfs_together: {merge_pdfs_together.__doc__}
    '''
          )

    # 选择要执行的函数
    function = session.prompt("Please select operation( split, merge): ", completer=function_completer)

    # 根据选择的函数调用相应的函数
    if function == "split":
        input_file = session.prompt("请输入输入文件路径: ", default='/Users/lyk/Documents/Research/毕设/诚信承诺书+三页表 签字扫描版.pdf')
        output_file_1 = session.prompt("请输入第一个输出文件路径: ", default='诚信承诺书_陆昱宽.pdf')
        output_file_2 = session.prompt("请输入第二个输出文件路径: ", default='三页表_陆昱宽_签字扫描版.pdf')
        index = int(session.prompt("请输入index: ",default="1"))

        split_pdf(input_file, output_file_1, output_file_2, index)


    elif function == "merge":
        input_file_1 = session.prompt("请输入pdf文档A的路径: ",
                                    default='/Users/lyk/Documents/Research/毕设/191820133 陆昱宽 一种基于注释分类的注释克隆检测方法.pdf')
        input_file_2 = session.prompt("请输入pdf文档B的路径: ", default='/Users/lyk/Documents/Research/毕设/诚信承诺书/诚信承诺书_陆昱宽.pdf')
        output_file = session.prompt("请输入合并后的pdf文档的路径: ", default='191820133 陆昱宽 终稿.pdf')
        index = int(session.prompt("请输入index: ", default="1"))

        merge_pdfs(input_file_1, input_file_2, output_file, index)
    elif function == "merge_pdfs_together":
        input_file_1 = session.prompt("请输入pdf文档A的路径: ",
                                      default='/Users/lyk/Desktop/Eng1.pdf')
        input_file_2 = session.prompt("请输入pdf文档B的路径: ",
                                      default='/Users/lyk/Desktop/Eng2.pdf')
        input_file_3 = session.prompt("请输入pdf文档C的路径: ",
                                      default='/Users/lyk/Desktop/Eng3.pdf')
        output_file = session.prompt("请输入合并后的pdf文档的路径: ", default='Transcript.pdf')
        input_files = [input_file_1, input_file_2, input_file_3]
        merge_pdfs_together(input_files, output_file)

    # if action == "split":
    #     # input_file = '/Users/lyk/Documents/Research/毕设/诚信承诺书+三页表 扫描版.pdf'
    #     input_file = input("请输入输入文件路径: ") or '/Users/lyk/Documents/Research/毕设/诚信承诺书+三页表 签字扫描版.pdf'
    #
    #     # 第一个输出文件路径（第一页）
    #     # output_file_1 = '诚信承诺书_陆昱宽.pdf'
    #     output_file_1 = input("请输入第一个输出文件路径: ") or '诚信承诺书_陆昱宽.pdf'
    #
    #     # 第二个输出文件路径（后三页）
    #     # # output_file_2 = '三页表_陆昱宽_签字扫描版.pdf'
    #     output_file_2 = input("请输入第二个输出文件路径: ") or '三页表_陆昱宽_签字扫描版.pdf'
    #
    #     # # 原文件的第一页是诚信承诺书, 后三页是三页表.
    #     # index = 1
    #     index = int(input("请输入index: ") or 1)
    #
    #     split_pdf(input_file, output_file_1, output_file_2, index)
    #
    # elif action == "merge":
    #     input_file_1 = input(
    #         "请输入pdf文档A的路径: ") or '/Users/lyk/Documents/Research/毕设/191820133 陆昱宽 一种基于注释分类的注释克隆检测方法.pdf'
    #     input_file_2 = input("请输入pdf文档B的路径: ") or '/Users/lyk/Documents/Research/毕设/诚信承诺书/诚信承诺书_陆昱宽.pdf'
    #     output_file = input("请输入合并后的pdf文档的路径: ") or '191820133 陆昱宽 终稿.pdf'
    #     index = int(input("请输入index: ") or 1)
    #
    #     merge_pdfs(input_file_1, input_file_2, output_file, index)

