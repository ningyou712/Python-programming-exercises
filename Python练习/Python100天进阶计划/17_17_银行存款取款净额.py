# 第 17 题：存款取款净额
# 时间：____ 年 __ 月 __ 日
# 作者：______（填你的名字）

# 在这里写你的代码
net_amount = 0
while True:
    s = input("输入你要进行的操作：").strip()
    if s == "":
        break
    operation = s[0]
    amount_str = s[1:]
    amount = int(amount_str)
    if operation == "D":
        net_amount += amount
    elif operation == "W":
        net_amount -= amount
print(net_amount)
# 测试代码
# if __name__ == '__main__':
#     pass
