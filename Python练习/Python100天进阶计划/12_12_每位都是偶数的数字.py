# 第 12 题：都是偶数的数字
# 时间：____ 年 __ 月 __ 日
# 作者：______（填你的名字）

# 在这里写你的代码
result = []
for i in range(1000,3001):
    s = str(i) # 必要转换，将整数转换成字符串
    if all(int(digit) % 2 == 0 for digit in s): # 检查每一个字符是否为偶数
        result.append(s)
print(','.join(result))

# 测试代码
# if __name__ == '__main__':
#     pass
