word = raw_input("Enter word:")

vowels = ['a','e','i','o','u','y']

count = 0
for i in range(0,len(word)):
	if(word[i] in vowels and (i+1>=len(word) or word[i+1] not in vowels)):
		count+=1

print("{0} has {1} syllables.".format(word,count))