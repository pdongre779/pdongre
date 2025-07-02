# program to enter P,T,R and calculate compound interest 

p = int(input("enter a principal amount"))
t = int(input("enter a time"))
r = int(input("enter a rate of interest"))

a=p*(1+r/100)**t
compound_interest=a-p
print("compound_interest is:",compound_interest)