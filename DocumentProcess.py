import unicodedata

def chinese_char_to_eng_char(input_file, output_file):
    '''
    将给定的文件中的所有中文标点替换为对应的英文标点.
    由于我习惯在半角符号后面多加个空格, 因此每个被转换的英文标点后都会带一个空格
    '''
    with open(input_file, 'r', encoding='utf-8') as file:
        input_text = file.read()


    table = {ord(f): ord(t) for f, t in zip(
        u'，。！？（）',
        u',.!?()'
    )}

    new_text = input_text.translate(table)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(new_text)

def eng_char_to_chinese_char(input_file, output_file):
    '''
    将给定的文件中的所有英文标点替换为对应的中文标点
    英文的百分号, 数字号, at号, 中括号和数字不能转换， 因为在Latex中要用到。
    '''
    table = {ord(f): ord(t) for f, t in zip(
        u',.!?()',
        u'，。！？（）'
        )}

    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    new_text = text.translate(table)
    # print(new_text)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(new_text)

def eng_char_to_chinese_char_print(input_text):
    '''
    将给定的文件中的所有英文标点替换为对应的中文标点。

    '''
    table = {ord(f): ord(t) for f, t in zip(
        u',.!?()@&',
        u'，。！？（）＠＆'
        )}



    # new_text = text.maketrans(table)
    new_text = input_text.translate(table)
    print(new_text)



if __name__ == "__main__":
    # 替换标点的输入文件路径和输出文件路径
    input_file = '/Users/lyk/Documents/LYK-love.github.io/source/_posts/Bodybuilding-Basic.md'
    output_file = '1.md'

    # eng_char_to_chinese_char(input_file, output_file)
    chinese_char_to_eng_char(input_file, output_file)
    
    # text = "对这种过时注释的检测存在着许多困难, 因为注释是用自然语言书写的, 没有固定的结构, 其内容也没有固定的约束. 注释可以描述代码的不同方面, 例如方法的实现步骤, 提供方法的原因, 使用方法的注释事项等等. 注释也可以对代码的不同部分进行描述,  例如描述方法的签名, 返回值, 参数等等."
    # eng_char_to_chinese_char_print(text)