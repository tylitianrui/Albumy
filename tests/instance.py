# -*-coding:utf-8-*-
# AUTHOR:tyltr
# TIME :2018/11/27

class Mixin():
    @classmethod
    def at(cls,**kv):
        print(kv)
        instance = cls()
        s= instance.la()
        print(s)
        return s



class A(Mixin):
    def la(self):
        return 1+2

if __name__ == '__main__':
    A().at(a=1)
