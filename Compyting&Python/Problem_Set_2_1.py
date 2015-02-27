balance = 4842.00
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
minimum_payment = 0
unpaid_balance = 0
interest = 0
total_paid = 0
for i in range(1,13):
    print('Month: ' + str(i))
    minimum_payment = balance * monthlyPaymentRate
    total_paid += minimum_payment
    unpaid_balance = balance - minimum_payment
    interest = annualInterestRate/12.0 * unpaid_balance
    balance = unpaid_balance + interest 
    print('Minimum monthly payment: ' + str.format('{0:.2f}', minimum_payment))
    print('Remaining balance: ' + str.format('{0:.2f}', balance))
print('Total Paid: ' + str.format('{0:.2f}', total_paid))
print('Remaining balance: ' + str.format('{0:.2f}', balance))