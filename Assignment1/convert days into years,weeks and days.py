# program to convert days into years, weeks and days

total_days = int(input("total number of days"))

years = total_days // 365
remaining_days = total_days % 365

weeks = remaining_days // 7
days = remaining_days % 7
print("years:",years)
print("weeks:",weeks)
print("days:",days)
