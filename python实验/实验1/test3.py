import string

def analyze_text(filename):
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    space_count = 0
    other_count = 0
    word_count = 0
    first_letter_string = ""

    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        
        # (1) 统计大写字母、小写字母、数字、空格和其他字符的数量
        for char in text:
            if char.isupper():
                uppercase_count += 1
            elif char.islower():
                lowercase_count += 1
            elif char.isdigit():
                digit_count += 1
            elif char.isspace():
                space_count += 1
            else:
                other_count += 1

        # (2) 统计单词数量，缩写的两个单词按2个单词计数
        words = text.replace("’", "'").replace("'", " ").split()
        word_count = len(words)

        # (3) 拼接每个单词的首字母
        for word in words:
            if word:  # 确保不为空
                first_letter_string += word[0]

    # 输出结果
    print(f"(1) 大写字母数量: {uppercase_count}")
    print(f"    小写字母数量: {lowercase_count}")
    print(f"    数字数量: {digit_count}")
    print(f"    空格数量: {space_count}")
    print(f"    其他字符数量: {other_count}")
    print(f"(2) 单词数量: {word_count}")
    print(f"(3) 首字母拼接字符串: {first_letter_string}")

# 调用函数，分析文件 my.txt
analyze_text("my.txt")
