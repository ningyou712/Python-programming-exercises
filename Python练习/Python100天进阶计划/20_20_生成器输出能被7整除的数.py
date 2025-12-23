# 第 20 题：器输出能被7整除的数
# 时间：____ 年 __ 月 __ 日
# 作者：______（填你的名字）

# 在这里写你的代码
def num_generator(n):
    for i in range(n+1):
        if i % 7 == 0:
            yield i
n = int(input("请输入一个整数n：").strip())
for num in num_generator(n): # 和生成器一起使用，得出正确的值
    print(num) # 生成器每得出一次结果输出一次
# 测试代码
# if __name__ == '__main__':
#     pass
