import sys

# Calculate Simple Interestit 

if len(sys.argv) == 4:
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
else:
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time in years: "))

simple_interest = (principal * rate * time) / 100

print("Principal Amount:", principal)
print("Rate of Interest:", rate, "%")
print("Time:", time, "years")
print("Simple Interest:", simple_interest)