"""
semi annual raise is 0.07
r = 0.04
cost of house 1M

"""
#getting inputs from the user
annual_salary = float(input("Enter your annual salary:"))
portion_saved = 0 #to find
total_cost = 1000000
semi_annual_raise = 0.07

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
                                        #we want to fix it to 36 months.
#methodlogy- guess on basis of salary without factoring in the rate of increment and raise.
#this might give us either more or less than the required soln
saving_guess = 0
while(saving_guess<portion_down_payment):
    portion_saved +=0.01
    saving_guess = 
