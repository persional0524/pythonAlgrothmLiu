# coding : utf-8
# create by ztypl on 2017/5/25

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
    def pay(self, money):
        print("苹果支付%s元"%money)


class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass


class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(use_huabei=False)

class ApplePayFactory(PaymentFactory):
    def create_payment(self):
        return ApplePay()

class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(use_huabei=True)




# 用户输入
# 支付宝，120

af = HuabeiFactory()
ali = af.create_payment()
ali.pay(120)