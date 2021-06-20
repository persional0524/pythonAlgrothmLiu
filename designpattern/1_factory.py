# coding : utf-8
# create by ztypl on 2017/5/24

from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        raise NotImplementedError


class Alipay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei:
            print("花呗支付%s元" % money)
        else:
            print("支付宝支付%s元" % money)


class ApplePay(Payment):
    def __init__(self, s):
        pass

    def pay(self, money):
        print("苹果支付%s元" % money)



class PaymentFactory:
    def create_payment(self, method):
        if method == "alipay":
            return Alipay()
        elif method == "applepay":
            return ApplePay()
        elif method == 'huabei':
            return Alipay(use_huabei=True)
        else:
            raise NameError(method)


pf = PaymentFactory()
p = pf.create_payment('huabei')
p.pay(100)