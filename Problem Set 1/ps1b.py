#6.0001 Problem Set 1b Solution - Evan Dieterich

annual_salary = float(input('What is your annual salary: '))
portion_saved = float(input('What percent of your salary do you plan to save: '))
total_cost = float(input('What is the cost of your dream home: '))
pay_increase = float(input('Enter the semi-annual raise: '))

down_payment = .25 * total_cost
current_savings = 0
months = 0
r = .04

while current_savings < down_payment:
    months += 1
    current_savings += (current_savings*r/12) + portion_saved * annual_salary/12
    if months % 6 == 0:
        annual_salary += annual_salary * pay_increase

print('Number of months: ', months)

