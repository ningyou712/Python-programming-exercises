# 第 19 题：段排序姓名年龄成绩
# 时间：____ 年 __ 月 __ 日
# 作者：______（填你的名字）

# 在这里写你的代码
from operator import itemgetter
result = []
print("请输入如下例子：姓名，年龄，身高")
while True:
    line = input('>>').strip()
    if line == '':
        break
    result.append(tuple(line.split(','))) # 将字符串转化为列表再转化为元组，最后加入列表
print(sorted(result, key=itemgetter(0,1,2))) # 排序按照关键点
# 测试代码
# if __name__ == '__main__':
#     pass
