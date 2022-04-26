# A program is required to calculate the annual cost of running a motor car. Costs include monthly installments, the annual fuel cost and insurance. The annual insurance rate is 3% of the car's value.
# Required input values are:
# value of the motor car
# Monthly installment amount
# Annual fuel cost
# The output is the annual cost of running the car.'''

import math

car_value = float(input("What is the value of your vehicle? "))

monthly_installment = float(input("What is the monthly installment? "))

annual_fuel_cost = float(input("How much do you pay for fuel per year? "))

annual_insurance = car_value * 0.03
annual_installment = monthly_installment * 12
annual_cost_of_car = annual_installment + annual_fuel_cost + annual_insurance

message = " The annual cost of running your car is R"
print((message), round(annual_cost_of_car, 2))
