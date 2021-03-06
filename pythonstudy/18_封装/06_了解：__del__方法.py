# 对象的生命周期;
# 生命开始：从对象名 = 类名时，创建对象，生命周期开始
# 生命结束：一旦调用了__del__方法，该对象结束调用
# 生命周期内，该对象可以访问类中的属性，调用类中的方法

# __del__方法的作用：
# 当用户想在被销毁前，在做一些事情时，可以调用该方法


class Animal:

    def __init__(self):
        print('这是一个初始化方法')

    def __del__(self):
        print('这个是对象被销毁前最后执行的方法')


dog = Animal()
# del也可以删除一个对象，如果使用del dog删除了对象，那么代码走到这一步时，就会先去执行__del__,之后才会执行下面的print
# 如果没有下面这句，那么将会先去执行print，最后去执行__del
del dog

print('-'*50)
# 因此输出结果为：
# 这是一个初始化方法
# 这个是对象被销毁前最后执行的方法
# --------------------------------------------------
