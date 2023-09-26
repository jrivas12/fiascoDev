days = int(input())
# Write your code here
#print("Enter number of days: ", input())
year = int(days/365)
weeks = int((days%365)/7)
days = int((days%365)%7)

print("years = ", year)
print("weeks = ", weeks)
print("days = ", days) 