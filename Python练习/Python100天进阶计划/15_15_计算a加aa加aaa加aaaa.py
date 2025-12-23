# 第 15 题：a加aa加aaa加aaaa
# 时间：____ 年 __ 月 __ 日
# 作者：______（填你的名字）

# 在这里写你的代码
a = input("请输入一个0 - 9的数：").strip()
sum = 0
for i in range(1,5):
    num = int(a * i) # 拼接并转成整数
    sum += num # sum = sum + num
print(sum)
# 测试代码
# if __name__ == '__main__':
#     pass
