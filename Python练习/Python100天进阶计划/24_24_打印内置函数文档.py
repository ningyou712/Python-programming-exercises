# 第 24 题：内置函数文档
# 时间：____ 年 __ 月 __ 日
# 作者：______（填你的名字）

# 在这里写你的代码
print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)
def square(num):
    """
    返回输入数字的平方值。

    输入参数必须是整数或浮点数。
    示例：
        square(2) -> 4
        square(-3) -> 9
    """
    return num ** 2
print(square(2))
print(square.__doc__)
# 测试代码
# if __name__ == '__main__':
#     pass
