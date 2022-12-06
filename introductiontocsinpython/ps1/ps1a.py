#getting inputs from the user
annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percentage saved: "))
total_cost = float(input("Cost of Dream home:"))
#amt of downpayment 1/4 the total cost
portion_down_payment = 0.25*total_cost
#amt saved everymonth through salary
saved = (annual_salary/12)*portion_saved
current_savings = 0
r = 0.04

counter_months = 0
while(current_savings<portion_down_payment):
    current_savings = current_savings*(1+r/12) +saved
    counter_months +=1
print("Number of months:",counter_months)

