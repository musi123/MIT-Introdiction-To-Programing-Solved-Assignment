# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 22:52:48 2019

@author: MUSTAFA
"""
total_cost=1000000
semi_annual_raise=0.07
annual_salary=float(input("Enter the starting annual salary:"))
a=annual_salary
p_s_low=0
p_s_high=10000
portion_saved=(p_s_low + p_s_high)//2
portion_down_payment=0.25
current_savings=0.0
r=0.04
month=0
guesses=0

while abs(current_savings- portion_down_payment*total_cost) >= 100:
    if month==36:
       month=0
       current_savings=0
       annual_salary=a
    current_savings+=current_savings*r/12 + (annual_salary/12)*portion_saved/10000
    month+=1
    if month%6==0:
        annual_salary+=annual_salary*semi_annual_raise
    if month==36:
        if current_savings<(portion_down_payment*total_cost):
            p_s_low=portion_saved
        else:
            p_s_high=portion_saved
        portion_saved=(p_s_low + p_s_high)//2
        guesses+=1
    if guesses>13:
        break
if guesses>13:
    print('It is not possible to pay the down payment in three years.')
else:
    print('Best savings rate:',portion_saved/10000)
    print('Steps in bisection search:',guesses)
