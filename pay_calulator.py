work_time = float(input("how many hours did employee work? "))
pay_rate =  float(input("how much is employee paid per hour? "))
average_work_week = 40
overtime_rate = 1.5

if work_time > average_work_week:
    pay = average_work_week * pay_rate
    overtime_pay_rate = pay_rate * overtime_rate
    overtime_hours = work_time - average_work_week
    overtime_pay = overtime_pay_rate * overtime_hours
    overtime_pay_total = pay + overtime_pay
    print(f'your total pay for the week is ${overtime_pay_total}.')
else:
    pay = work_time * pay_rate
    print(f'your total pay for the week is ${pay}.')
