

file_name = input("Filename: ")

search_text = input("What you want to be replaced?\n")


replace_text = input("What you want to replace it with?\n")

# 使用 open() 函数以只读模式打开我们的文本文件
with open(file_name, 'r',encoding='UTF-8') as file:

	# 使用 read() 函数读取文件内容并将它们存储在一个新变量中
	data = file.read()

	# 使用 replace() 函数搜索和替换文本
	data = data.replace(search_text, replace_text)

# 以只写模式打开我们的文本文件以写入替换的内容
with open(file_name, 'w',encoding='UTF-8') as file:

	# 在我们的文本文件中写入替换的数据
	file.write(data)

# 打印文本已替换
print("文本已替换")