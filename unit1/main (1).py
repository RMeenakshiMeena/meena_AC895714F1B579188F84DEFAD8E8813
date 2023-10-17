#To find the leap year
y=2005
y=int(input("Enter valid year"))
if(y % 4 == 0):
  print("Given year is leap year")
else:
  print("Given year is not a leap year")