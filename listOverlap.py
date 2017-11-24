import random
def makelists(random_int):
	numList=[]
	for count in range(random_int):
		numList.append(random.randint(1,100))
	return numList

def main():
	a=random.randint(1,51)
	print(a)
	actualA=makelists(a)
	print(actualA)
	a=random.randint(1,51)
	print(a)
	actualB=makelists(a)
	print(actualB)
	intersection=[]

	for number in actualA:
		if number in actualB:
			intersection.append(number)

	print(intersection)

main()