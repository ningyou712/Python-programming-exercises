# 第 29 题：串拼接
# 时间：____ 年 __ 月 __ 日
# 作者：______（填你的名字）

# 在这里写你的代码
def printValue(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        print(s1)
    elif len2 >len1:
        print(s2)
    elif len1 == len2:
        print(s1,s2)
printValue("one", "three")
printValue("one", "two")
# 测试代码
# if __name__ == '__main__':
#     pass
