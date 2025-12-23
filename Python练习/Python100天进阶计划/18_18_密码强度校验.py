# 第 18 题：强度校验
# 时间：____ 年 __ 月 __ 日
# 作者：______（填你的名字）

# 在这里写你的代码
import re
prompt = ("请输入密码，要求如下：\n"
          "- 至少1个小写字母 [a-z]\n"
          "- 至少1个大写字母 [A-Z]\n"
          "- 至少1个数字 [0-9]\n"
          "- 至少1个特殊字符 [$#@]\n"
          "- 长度6-12位\n"
          "密码："
)
password_input = input(prompt).strip() # 输入时是字符串
password = password_input.split(',') # 转换为列表在分割
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@]).{6,12}$' # 密码规则
valid = [p.strip() for p in password if re.match(pattern, p.strip())] # 检查是否有匹配密码
print(','.join(valid))
# 测试代码
# if __name__ == '__main__':
#     pass
