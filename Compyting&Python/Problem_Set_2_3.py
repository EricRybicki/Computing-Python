balance = 320000.00
annualInterestRate = 0.2

lower = balance / 12.0
upper = (balance * (1 + annualInterestRate / 12.0)**12) / 12.0
minimum_payment = (upper+lower)/2.0
bbalance = balance
for i in range(1,13):
    bbalance = (bbalance - minimum_payment) *(1+ annualInterestRate/12.0)
while abs(bbalance) > 0.01:
    if bbalance < 0:
        upper = minimum_payment
    else:
        lower = minimum_payment
    minimum_payment = (upper+lower)/2.0 
    bbalance = balance
    for i in range(1,13):
        bbalance = (bbalance - minimum_payment) *(1+ annualInterestRate/12.0)
print('Lowest payment: ' + str.format('{0:.2f}', minimum_payment))