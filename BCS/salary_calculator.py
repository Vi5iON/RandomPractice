print('Welcome to salaray calculator.\n')

salary = float(input('Enter the salary of employee.\n'))
num_working_days = int(input('Enter the number of working days.\n'))
days_worked = int(input('Enter the number of days employee worked for.\n'))

salary_for_day = float(salary / 30)

if days_worked > num_working_days : 
    salary_gain = salary_for_day * (days_worked - num_working_days)
    salary = salary + salary_gain
elif days_worked < (num_working_days - 2):
    loss_days = num_working_days - 2 - days_worked
    salary = salary - (salary_for_day * loss_days)

print('Salary of employee is',salary)