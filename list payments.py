payments  = []
i = 0
number_employees = float(input("Please enter the number of employees : "))
while i < number_employees:
    payment = float(input(" Employee number " + str(len(payments) + 1) + " Please enter the hours worked: "))
    payments = payments + [payment]
    gross_pay = payment * 20
    print(gross_pay)
    i += 1
    payments.append(input("Enter anything"))
    print(payments)


