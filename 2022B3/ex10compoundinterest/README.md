# WPE 2022 B3 Exercise 10: Compound interest

Create a Loan class, which will allow us to represent a bank loan.
Using the Loan class, we should be able to create a new loan: 

    my_loan = Loan(1000, 0.02)

The above means that my loan is for $1,000 (or the currency you prefer), at 2% interest. Moreover, 
it indicates that the loan period starts *today*.

If we want, we can specify that the loan will start (or already started) on a different day. 
However, we'll do that by creating a new Arrow date object. (You can use the built-in libraries, if you want, 
but then the tests won't work...) 

    ad = arrow.get(2018, 1, 1)
    my_loan = Loan(1000, 0.02, starts_on=ad)

Again: If we don't specify the starting day, then "starts_on" defaults to today.

The "Loan" class will also support two methods:

1. **"total_on"** - which takes an "ends_on" argument, in the form of an Arrow date. 
The result will be the total owed on that date. You'll get the total amount owed on the 1st of January, 2020 if you say: 

        ad = arrow.get(2020, 1, 1)
        my_loan.total_on(ad)

2. **total_on_each** - which takes *two* Arrow date arguments, "starts_on" and "ends_on". It is a generator that 
returns (with each iteration) a two-element tuple, with the date and the amount owed on that date. The amount 
returned is a float; you can cut the float off after two digits. Our bank is already making so much that we don't 
care about little things like accuracy. You'll probably find that Arrow.span_range will come in handy in 
implementing this.
