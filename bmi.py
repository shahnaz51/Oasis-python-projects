w = float(input("Enter your weight in Kg\n"))
h = float(input("Enter height in metre\n"))

x = w/(h*h)

print("Your bmi is", x)

if x < 18.5:
    print("Underweight")

if x>=18.5 and x<25:
    print("Normal")

if x >= 25 and x < 30:
   print('Overweight')

if x >= 30:
   print('Obesity')