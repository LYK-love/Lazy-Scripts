def convert_punctuation(text):
    # 将英文逗号转换为中文逗号
    text = text.replace(", ", "，")
    # 将英文句号转换为中文句号
    text = text.replace(". ", "。")
    # 防止有一些未带空格的英文标点未被替换
    text = text.replace(",", "，")
    text = text.replace(".", "。")
    return text


# 示例文本

english_text = """
"""
# 调用函数转换标点
chinese_text = convert_punctuation(english_text)

print(chinese_text)
