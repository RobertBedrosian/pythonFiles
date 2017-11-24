userNumber=int(input("Enter a number you want to find all divisors of: "))
allNumbers=range(2,userNumber+1)
allDivisors=[]
for number in allNumbers:
	if (userNumber%number == 0):
		allDivisors.append(int(userNumber/number))

for divisor in allDivisors:
	print (divisor)

