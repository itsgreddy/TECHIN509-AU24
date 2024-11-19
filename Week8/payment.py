class PayPal:
    def charge(self, amount):
        pass

class ApplePay:
    def charge(self, amount):
        pass

class GooglePay:
    def charge(self, amount):
        pass

payment_method = input("Please select a payment method (PayPal, ApplePay, CreditCard)")
payment_method.charge(100)