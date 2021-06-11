# #!/usr/bin/env python
# # -*- encoding: utf-8 -*-
# """
# @File   :   test_inherit.py
# @Time   :   2021/6/9 11:29
# @Contact    :
# @Author     :   WG
# @Version    :   v 0.1
# @Desc   :
# """
# class Parent:
#     def __hello(self):
#         print('我是父亲')
#
#
# class Child(Parent):
#     # child类继承与 parent类
#     def __hello(self):
#         print(dir(super))
#         super(Child, self).__hello()
#         # parent类中有hello方法，但是这里也定义了一个hello方法。
#         # 覆盖,但是父类方法不受影响
#         print('我是孩子')
#
#
# # def main():
#     # Child().__hello()  # 调用的是 子类的方法
#     # Parent().hello()  # 调用的是 父类的方法
# if __name__ == '__main__':
#     # main()
#     a = Parent()
#     b = Child()
#     a.__hello()
#     a._Parent__hello()


class A(object):
    _param1 = 1
    __param2 = 2

    def __method(self):
        print("I'm a method in class A")
        print()
    def method_x(self):
        print("I'm another method in class A\n")

    def method(self):
        self.__method()
        self.method_x()
        print(self._param1,self.__param2)


class B(A):
    _param1 = 3
    __param2 = 4

    def __method(self):
        print("I'm a method in class B")

    def method_x(self):
        print("I'm another method in class B\n")


if __name__ == '__main__':
    print("situation 1:")
    a = A()
    a.method()

    b = B()
    b.method()

    print("situation 2:")
    # a.__method()
    a._A__method()
