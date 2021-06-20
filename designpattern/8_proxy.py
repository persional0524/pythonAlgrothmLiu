# coding : utf-8
# create by ztypl on 2017/5/26

from abc import ABCMeta, abstractmethod

class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass


class RealSubject(Subject):
    def __init__(self, filename):
        print("读取%s文件内容"%filename)
        f = open(filename)
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content


class ProxyB(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()


p = ProxyB("abc.txt")
#print(p.get_content())




# class ProxyC(Subject):
#     def __init__(self, filename):
#         self.subj = RealSubject(filename)
#
#     def get_content(self):
#         return "???"

    # 写一个set_content