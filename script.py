# testing demo stuff can go here!

file = open("sonnet_xviii.txt")

count = 0
for line in file: 
	words = line.split(' ') #This is a space delimiter, shows where the beginging and end of the word is
	for word in words: #there is a loop inside of another loop, this is called a NESTED LOOP
		count = count + 1

print(count, "words") #so now we're counting words instead of lines

#Let's try something else!

import re #this imports regex (crying brb)
file = open("sonnet_xviii.txt")

count = 0 
for line in file: 
	words = re.split("[^\w']+", line) #what does this ReGex command say? split all words seperated by punctuation?
	for word in words:
		if word !=  "" :
			count = count + 1

print(count, "words") #This prints less words not more

#what's the average of letters per line? 
#How would you do that? By counting all the letters and dividing by the total number of words! 
#So we have to count both letters and words

file = open("alice.txt")

total_ltr = 0 
count = 0 
for line in file: #important, count letters in a line, not in a word. How could we count by word? 
	total_ltr = total_ltr + len(line) #what does the len command do? 
	count = count + 1

avg_len = round((total_ltr/count), 2) 
print("Average word length:", avg_len) #this is returning an average length of 43 characters which makes no damn sense 

#looping: does it contain a word dog? 
#the challenge is that the computer needs to remember if they've found the word previously 

file = open("words_huge.txt")

target = input("Word to find: ")

found = False
for line in file: 
		if line.strip() == target: #its important to include the STRIP command, becuase otherwise the loop will read the whole line
			found = True #the strip command adds a whitespace on either side? or removes the white space on either side. One of the two
if found: 
	print(target + " is in the list!")
else:
	print("Sorry try again! ")

#the average number of letters per word? 
#this is just a frankenstein mashup of two different functions
#this is not in the lecture, aren't you special 

import re
file = open("alice.txt")

total_ltr = 0 
count = 0
for line in file: 
	word = re.split("[^\w']", line)
	for word in words: 
		if word != "":
			total_ltr = total_ltr + len(word)
			count = count + 1 

avg_len = total_ltr/count 
print("The average word length is: ", avg_len)

#ALLLLLLL words shorter than 'n' 
#in order to answer this question, we're not looking for all words SHORTER than n
#we're actuall looking for words that are longer
#so we're not looking for all words that are small, we're looking for one word that is not small

file = open("alice.txt")
max_length = int(input("Max word length? "))

all_short = True #so our automatic assumption is all that words are smaller 
for line in file: 
	if len(line) > max_length: #looking for a long word
		all_short = False #if we found one, then our initial assumption was false
		break

if all_short: 
		print("All words short")
else: 
	print("A word was long")

#LISTS
#important thing to remember about lists: all lists start at ZERO

names = ["Dick", "Penis", "Asshole", "Freud"] #important to use square brackets

print(names[0])
print(names[1])
print(names[3])


print(names[1:])

a = "banana"
b = "banana"

a is b #TRUE

"banana" == "BANANA".lower() #TRUE

"banana" is "BANANA".lower() #FALSE

#Lists can be equivlaent WitHOUT being identical 
#ITS THE A LIST
letters = ['a', 'b', 'c']

def delete_first(a_list): 
	a_list = a_list[1:] #this a_list is a local variable only! 
	#return a_list <- THIS LINE OF CODE would have the computer store and rembmer the local variable 
	print(a_list) #print local variable

delete_first(letters)
print(letters) #print global variable

#FUCK MATRICIES 