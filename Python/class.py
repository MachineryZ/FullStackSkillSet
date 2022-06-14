class Test(object):
    # 先 __new__创建一个对象
    # __new__ 返回的对象，传输给 __init__ 的 self
    def __new__(cls):
        print(f"new {cls}")
        return object.__new__(cls)
    
    def __init__(self):
        print(f"init {self}")
        object.__init__(self)

tt = Test()

class TestMeta3(type):
    def __new__(cls, name, bases, attrs):
        print(f"TestMeta3 cls {cls}")
        print(f"TestMeta3 bases {bases}")
        print(f"TestMeta3 attrs {attrs}")
        return type.__new__(cls, name, bases, attrs)

class Pa3:
    pass

class Eg3(Pa3, metaclass=TestMeta3):
    @classmethod
    def get(self):
        kkk = []
        kkk.append(self.__skiless__)
        return kkk
    
    def acc2(self):
        return 'a2'
