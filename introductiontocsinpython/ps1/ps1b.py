#getting inputs from the user
annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percentage saved: "))
total_cost = float(input("Cost of Dream home:"))
semi_annual_raise = float(input("Enter the semi_annual Raise:"))

#amt of downpayment 1/4 the total cost
portion_down_payment = 0.25*total_cost



current_savings = 0
r = 0.04

counter_months = 0
while(current_savings<portion_down_payment):
    current_savings = current_savings*(1+r/12) +(annual_salary/12)*portion_saved
    counter_months +=1
    if(counter_months%6 == 0):
        annual_salary = annual_salary*(1+semi_annual_raise)
print("Number of months:",counter_months)#no of months required to afford the down-payment