# def debug(func):
#     def wrapper():
#         print('[DEBUG]: enter {}()'.format(func.__name__))
#         return func()
#
#     return wrapper
#
#
# @debug
# def say_hello():
#     print('hello!')
#
#
# @debug
# def say_goodbye():
#     print('goodbye!')
#
#
# say_hello()
# say_goodbye()
#
#
# def logging(level):
#     def wrapper(func):
#         def inner_wrapper(*args, **kwargs):
#             print("[{level}]: enter function {func}()".format(level=level, func=func.__name__))
#             return func(*args, **kwargs)
#
#         return inner_wrapper
#
#     return wrapper
#
#
# @logging("INFO")
# def say(something):
#     print("say {}!".format(something))
#
#
# # 如果没有@
# # 相当于say=logging(level='INFO')(say)
#
# @logging("DEBUG")
# def do(something):
#     print("do {}!".format(something))
#
#
# if __name__ == '__main__':
#     say('hello')
#     do("eat")

class logging(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(level=self.level, func=func.__name__))
            return func(*args, **kwargs)

        return wrapper


@logging(level='DEBUG')
def say(something):
    print("say {}!".format(something))


@logging()
def do(something):
    print("do {}!".format(something))


say('hello')
do('sleep')

print(say.__name__)


class C(object):
    def __init__(self):
        self._x = 0

    @property
    def x(self):
        print("XXXXXXXXX")
        return self._x

    @x.setter
    def x(self, value):
        print("set")
        self._x = value

    @x.deleter
    def x(self):
        print("del")
        del self._x


c = C()
print(c.x)
c.x = 1
print(c.x)
del c.x
