#6.0001 Problem Set 1a Solution - Evan Dieterich

annual_salary = float(input('What is your annual salary: '))
portion_saved = float(input('What percent of your salary do you plan to save: '))*.01
total_cost = float(input('What is the cost of your dream home: '))

down_payment = .25 * total_cost
current_savings = 0
monthly_savings = portion_saved * annual_salary/12
months = 0
r = .04

while current_savings < down_payment:
    months += 1
    current_savings += current_savings*r/12
    current_savings += monthly_savings

print('Number of months: ', months)
