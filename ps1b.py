# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 22:52:05 2019

@author: MUSTAFA
"""

semi_annual_raise=float(input("Enter the semi annual raise in decimal percent:"))
total_cost=float(input("Enter the cost of your dream home:"))
annual_salary=float(input("Enter the starting annual salary:"))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal:"))
portion_down_payment=0.25
current_savings=0.0
r=0.04
month=0

while(current_savings<=(portion_down_payment*total_cost)):
    current_savings+=current_savings*r/12 + (annual_salary/12)*portion_saved
    month+=1
    if(month%6==0):
        annual_salary+=annual_salary*semi_annual_raise
print("Number of months:",month,"Number of years:",month/12)
