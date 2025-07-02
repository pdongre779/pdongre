# program to enter P,T,R and calculate simple interest

p = int(input("enter a principal amount"))
t = int(input("enter a time"))
r = int(input("enter a rate of interest"))

simple_interest = (p*t*r)/100
print("simple_interest is:", simple_interest)