# Создайте класс Loan, который хранит сумму кредита.
# Реализуйте методы __add__ для увеличения суммы кредита
# (например, добавление начисленных процентов) и __sub__
# для его уменьшения (например, при выплате).
# Реализуйте также __mul__ для расчета увеличения суммы кредита
# при умножении на процентный коэффициент.

class Loan:
    def __init__(self, sum):
        self.sum = sum

    def __add__(self, sum_interest):
        return Loan(self.sum + sum_interest)

    def __sub__(self, pay):
        result = self.sum - abs(pay)
        if result <= 0:
            raise ValueError('Переплата по счёту')
        return Loan(result)

    def __mul__(self, interest):
        return Loan(self.sum * (1 + interest))

    def __str__(self):
        return f'{self.sum}'


loan = Loan(100_000)
sum_interest = 1000
pay = -1000
interest = 0.1
total = loan + sum_interest
print(total)
