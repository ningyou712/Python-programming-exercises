# 第 10 题：去重并排序
# 时间：____ 年 __ 月 __ 日
# 作者：______（填你的名字）

# 在这里写你的代码
print("请输入一段有重复的单词：")
words = input().strip().split()
unique_words = sorted(set(words)) # set去重（转化为集合） sort排序
print(','.join(unique_words))
# 测试代码
# if __name__ == '__main__':
#     pass
