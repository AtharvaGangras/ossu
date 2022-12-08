"""
semi annual raise is 0.07
r = 0.04
cost of house 1M
implement for within 100 dollars only
"""
#initializing all the permanent variables
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25*total_cost
r = 0.04

#getting input from the user
annual_salary = float(input("Enter your starting annual salary:"))
annual_salary2_temp = annual_salary

#initializing all the loop variables
portion_saved = 0 #to find first in the range of 0 - 10000 and then convert to decimal
current_savings = 0 #in between variable to compare to the downpayment
min = 0 # minimum point of portion saved
max = 10000 # maximum point of portion saved
steps = 0 # steps taken for bisection search
counter_months = 0 #counter months
while(counter_months != 36 or abs(portion_down_payment-current_savings)>100):
    portion_saved = (min+max)//2 #between the two nums
    
    #gives us the number of months required for the guess
    
    counter_months = 0
    annual_salary2_temp = annual_salary
    current_savings = 0
    while(current_savings<portion_down_payment):
        current_savings = current_savings*(1+r/12) +(annual_salary2_temp/12)*(portion_saved/float(10000))
        counter_months +=1
        if(counter_months%6 == 0):
            annual_salary2_temp = annual_salary2_temp*(1+semi_annual_raise)
    
    #changing the value of min and max to cut down half the searching range every iteration
    if(counter_months>36):
        min = portion_saved
    else:
        max = portion_saved
    steps +=1
    if(max-min <= 1):
        print("It is not possible to pay the downpayment in three years.")
        break
if(counter_months == 36):
    portion_saved = portion_saved/float(10000)
    #printing everything
    print("Best saving rate:",portion_saved)
    print("Steps in bisection search:",steps)



