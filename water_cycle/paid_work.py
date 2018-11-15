daysInMoth = 28
weekends = 4 * 2 # 4 weeks multiplying by 2 days ( saturday, sunday )
wage = int(input("Your wage per day - ")) # we pay daily


workingDays = daysInMoth - weekends

print(wage * workingDays)
for i in range(workingDays):
    i+=1
    print(f'{i} day: {wage * i}') # income every day