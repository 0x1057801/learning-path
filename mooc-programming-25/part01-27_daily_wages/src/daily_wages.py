hourly = float(input("Hourly wage:"))
worked = int(input("Hours worked:"))
day = input("Day of the week:")

if day == "Sunday":
    hourly *= 2

print(f"Daily wages: {hourly * worked} euros")