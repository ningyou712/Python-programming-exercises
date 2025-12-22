# 第 11 题：制数被5整除
# 时间：____ 年 __ 月 __ 日
# 作者：______（填你的名字）

# 在这里写你的代码
binary_nums = input().strip().split(',')
result = []
for num in binary_nums:
    decimal_num = int(num, 2) # int(s,base),base = 2 表示二进制
    if decimal_num % 5 == 0:
        result.append(num)
print(result)
# 测试代码
# if __name__ == '__main__':
#     pass
