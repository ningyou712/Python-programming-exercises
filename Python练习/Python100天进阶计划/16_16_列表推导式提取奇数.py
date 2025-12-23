# 第 16 题：推导式提取奇数
# 时间：____ 年 __ 月 __ 日
# 作者：______（填你的名字）

# 在这里写你的代码
numbers_str = input("请输入一串数字用逗号隔开：").strip().split(',')
s = [x for x in numbers_str if int(x) % 2 != 0]
print(s)
# 测试代码
# if __name__ == '__main__':
#     pass
