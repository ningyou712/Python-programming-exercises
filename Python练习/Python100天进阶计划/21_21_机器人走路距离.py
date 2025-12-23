# 第 21 题：人走路距离
# 时间：____ 年 __ 月 __ 日
# 作者：______（填你的名字）

# 在这里写你的代码
import math
x = 0
y = 0
print('请输入移动的方向：')
while True:
    line = input('>>>').strip()
    if line == '':
        break
    direction, step_str = line.split( )
    step = int(step_str)
    if direction == 'UP':
        y += step
    elif direction == 'DOWN':
        y -= step
    elif direction == 'LEFT':
        x -= step
    elif direction == 'RIGHT':
        x += step
distance = int(round(math.sqrt(x**2 + y**2)))
print(distance)

# 测试代码
# if __name__ == '__main__':
#     pass
