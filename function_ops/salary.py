def main() :
    salary = float(input('Enter base pay.\n'))
    num_working_days = int(input('Enter the number of working days.\n'))
    days_worked = int(input('Enter the days worked.\n'))

    print('Salary of employee is',calculate_salary(salary, num_working_days, days_worked))

def calculate_salary(
    salary, num_working_days, days_worked) :
    
    salary_for_day = salary / 30

#this can again be spilt into smaller functions but too many arguments will be passed around

    if days_worked > num_working_days :
        salary += salary_for_day * (days_worked - num_working_days)
    elif days_worked < num_working_days - 2 :
        salary -= salary_for_day * (num_working_days - 2 - days_worked)
    
    return salary

if __name__ == '__main__' :
    main()