# EXCEPTIONS

class CurrenciesDoNotMatchError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return repr((self.currency, self.amount))

    def __add__(self, other):
        if self.currency != other.currency:
            #raise Exception('Currencies do not match!')
            raise CurrenciesDoNotMatchError(f'{self.currency} and {other.currency} do not match.')
        total_amount = self.amount + other.amount
        return Currency(self.currency, total_amount)


c1 = Currency('EUR', 20)
c2 = Currency('USD', 30)
print(c1 + c2)