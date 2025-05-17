# Math operators in order of importance 
#           ()
#           **
#          /  *
#          +  - 

bmi = int()
number1 = input("how tall are you in Meters?")
height = float(number1)
number2 = input("What do you weigh in KG?")
weight = int(number2)

bmi = ( weight / height** 2 )

print("your bmi is....")
print(round(bmi))
