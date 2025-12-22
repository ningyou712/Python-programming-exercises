# 第 7 题：二维数组i乘j
# 时间：____ 年 __ 月 __ 日
# 作者：______（填你的名字）

# 在这里写你的代码
print("请输入俩个用逗号隔开的整数：")
x_str, y_str = input().strip().split(',')
X = int(x_str)
Y = int(y_str)
matrix = []
for i in range(X):
    row = []
    for j in range(Y):
        row.append(i*j)
    matrix.append(row)
print(matrix)
# 测试代码
# if __name__ == '__main__':
#     pass
