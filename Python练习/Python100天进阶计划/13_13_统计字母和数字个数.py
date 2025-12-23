# 第 13 题：字母和数字个数
# 时间：____ 年 __ 月 __ 日
# 作者：______（填你的名字）

# 在这里写你的代码
print("请输入一段话：")
s = input().strip()
letters = 0
digits = 0
for char in s:
    if char.isalpha(): # 检测字母数量
        letters += 1
    if char.isdigit(): # 检测数字数量
        digits += 1
print(f"LETTERS {letters}")
print(f"DIGITS {digits}")
# 测试代码
# if __name__ == '__main__':
#     pass
