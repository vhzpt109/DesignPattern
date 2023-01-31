class Handler:
    def __init__(self):
        self.next_handler = None

    def setNext(self, handler):
        self.next_handler = handler

    def handle(self, req):
        if self.next_handler:
            return self.next_handler.handle(req)
        else:
            return None


class CashHandler(Handler):
    def handle(self, req):
        if req['method'] == 'cash':
            print(f"processing cash {req['amount']} won")
        else:
            print(f"CashHandler cannot process")
            super().handle(req)


class CreditCardHandler(Handler):
    def handle(self, req):
        if req['method'] == 'creditCard':
            print(f"processing creditCard {req['amount']} won")
        else:
            print(f"CreditCardHandler cannot process")
            super().handle(req)


class DebitCardHandler(Handler):
    def handle(self, req):
        if req['method'] == 'debitCard':
            print(f"processing debitCard {req['amount']} won")
        else:
            print(f"DebitCardHandler cannot process")
            super().handle(req)


if __name__ == "__main__":
    cash_handler = CashHandler()
    creditcard_handler = CreditCardHandler()
    debitcard_handler = DebitCardHandler()

    cash_handler.setNext(creditcard_handler)
    creditcard_handler.setNext(debitcard_handler)

    payment = {
        "method": "paypal",
        "amount": 10000
    }

    cash_handler.handle(payment)