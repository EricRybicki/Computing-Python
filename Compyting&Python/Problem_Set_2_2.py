balance = 3926.00
annualInterestRate = 0.2
minimum_payment = 10
bbalance = balance
interest = 0
total_paid = 0
while (bbalance > 0):
    total_paid = 0
    minimum_payment += 10
    bbalance = balance
    for i in range(1,13):
        unpaid_balance = bbalance - minimum_payment
        interest = annualInterestRate/12.0 * unpaid_balance
        bbalance = unpaid_balance + interest 
        total_paid += bbalance
print('Lowest payment: ' + str.format('{0:.2f}', minimum_payment))