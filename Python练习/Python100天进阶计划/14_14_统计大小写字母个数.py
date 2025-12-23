# 第 14 题：大小写字母个数
# 时间：____ 年 __ 月 __ 日
# 作者：______（填你的名字）

# 在这里写你的代码
s = input("请输入一段英文：").strip()
upper = 0
lower = 0
for char in s :
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
print(f"UPPER CASE {upper}")
print(f"LOWER CASE {lower}")
# 测试代码
# if __name__ == '__main__':
#     pass
