# 第 22 题：单词出现频率
# 时间：____ 年 __ 月 __ 日
# 作者：______（填你的名字）

# 在这里写你的代码
from collections import defaultdict
text = input('请输入一段话:').strip()
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word,0) + 1 # 对单词计数
sorted_words = sorted(freq.keys()) # 排序
for word in sorted_words:
    print(f'{word}: {freq[word]}')
# 测试代码
# if __name__ == '__main__':
#     pass
