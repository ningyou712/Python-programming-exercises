# 第 9 题：文字转大写
# 时间：____ 年 __ 月 __ 日
# 作者：______（填你的名字）

# 在这里写你的代码
print("请输入一段英文文字：")
lines = []
while True:
    line = input().rstrip() # rstrip是用于去除右侧的空白的
    if line == "": # 检测到空就停止
        break
    lines.append(line.upper()) #
for l in lines:
    print(l)


# 测试代码
# if __name__ == '__main__':
#     pass
