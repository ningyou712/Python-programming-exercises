# 第 5 题：输入大写打印的类
# 时间：2025 年 12 月 1 日
# 作者：许涛洋（填你的名字）

# 在这里写你的代码
class IOString:
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input().strip()
    def printString(self):
        print(self.s.upper())
ojb = IOString()
ojb.getString()
ojb.printString()
# 测试代码
# if __name__ == '__main__':
#     pass
