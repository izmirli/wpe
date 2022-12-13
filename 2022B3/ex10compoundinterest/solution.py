"""

"""
import arrow
import datetime


class Loan:

    def __init__(self, amount: float, interest: float, starts_on: None | datetime.date = None):
        self.loan_amount = amount
        self.interest = interest
        self.starts_on = starts_on if starts_on is not None else datetime.date.today()

    def __repr__(self):
        return f"{self.loan_amount}$ at {self.interest * 100}% (started: {self.starts_on})"

    def total_on(self, on_day: datetime.date) -> float:
        amount = self.loan_amount
        delta = on_day - self.starts_on
        years, days = divmod(delta.days, 356)
        for _ in range(years):
            amount += amount * self.interest

        amount += amount * self.interest / 356 * days
        return amount

    def total_on_each(self, range_start, range_end):
        pass


if __name__ == '__main__':
    my_loan = Loan(1000, 0.02)
    print(f"{my_loan=}")
    ad = arrow.get(2018, 1, 1)
    my_loan2 = Loan(1000, 0.01, starts_on=ad)
    print(f"{my_loan2=}")
    ad_1year = arrow.get(2018, 12, 31)
    print(f"{my_loan2.total_on(ad_1year)=}")
