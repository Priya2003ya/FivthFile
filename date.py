days=int(input("Enter the number of days:"))
year=days//365
days=days%365
month=days//30
days=days%30
week=days//7
days=days%7
print(year,"Year",month,"Month",week,"Week",days,"Days")

