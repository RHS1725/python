#bmi=int(input("enter bmi:"))
#print("overweight" if bmi > 25   else "underweight")
age=23

eat_pizza =True

exercise = False
print(("unfit" if (eat_pizza) else "fit") if (age < 30) else ("fit" if (exercise) else "unfit"))