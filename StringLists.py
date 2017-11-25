while True:
	word = input("Please give me a word or sentence you'd like reversed: ")
	nospace = word.replace(" ", "").lower()
	if nospace == nospace[::-1]:
		print("'{}' is a palindrome.".format(word))
	else:
		print("'{}' spelled backwards is '{}'".format(word,word[::-1]))
