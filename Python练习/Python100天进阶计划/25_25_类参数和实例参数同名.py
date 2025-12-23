# 第 25 题：数和实例参数同名
# 时间：____ 年 __ 月 __ 日
# 作者：______（填你的名字）

# 在这里写你的代码
class Person:
    name = "Person"
    def __init__(self,name=None):
        if name is not None:
            self.name = name
# 测试代码
jeffrey = Person("Jeffrey")             # 传入参数，创建实例参数
print("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()                         # 不传参数，实例无自己的 name
nico.name = "Nico"                      # 手动为实例创建并设置 name
print("%s name is %s" % (Person.name, nico.name))
# 测试代码
# if __name__ == '__main__':
#     pass
