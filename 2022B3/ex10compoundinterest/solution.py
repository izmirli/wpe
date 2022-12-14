"""Loan.

Represent a bank loan.
Using date class Arrow (wrapper of datetime.date)

Based on given formula: amount * ((1 + interest_rate) ** years)
"""
import arrow
import datetime
from typing import Generator

DAYS_IN_YEAR = 365


class Loan:
    """Bank loan."""

    def __init__(self, amount: float, interest: float, starts_on: None | datetime.date = None):
        self.loan_amount = amount
        self.interest_rate = interest
        self.starts_on = starts_on if starts_on is not None else datetime.date.today()

    def __repr__(self) -> str:
        return f"{self.loan_amount}$ at {self.interest_rate * 100}% (started: {self.starts_on})"

    def total_on(self, on_day: datetime.date) -> float:
        """Return total amount owed on given date.

        :param on_day: the date to check
        :return: total amount owed
        """
        delta = on_day - self.starts_on
        return self.loan_amount * ((1 + self.interest_rate) ** (delta.days / DAYS_IN_YEAR))

    def total_on_each(self, range_start: arrow.Arrow, range_end: arrow.Arrow) -> Generator[tuple[arrow.Arrow, float]]:
        """Span a range of dates and the amounts owed on each.

        :param range_start: range start date
        :param range_end: range end date
        :return: generator that yield tuples of date and amount owed on that date
        """
        if range_start > range_end:
            raise ValueError(f"range_start should be earlier than range_end")
        cur_date = range_start
        one_day = datetime.timedelta(days=1)
        while cur_date <= range_end:
            yield cur_date, self.total_on(cur_date)
            cur_date += one_day


if __name__ == '__main__':
    my_loan = Loan(1000, 0.02)
    print(f"{my_loan=}")
    ad = arrow.get(2018, 1, 1)
    my_loan2 = Loan(1000, 0.01, starts_on=ad)
    print(f"{my_loan2=}")
    ad_1year = arrow.get(2018, 12, 31)
    print(f"{my_loan2.total_on(ad_1year)=}")
    for d, a in my_loan2.total_on_each(arrow.get(2018, 6, 1), arrow.get(2018, 6, 10)):
        print(f"\t{d}: {a:.2f}$")

