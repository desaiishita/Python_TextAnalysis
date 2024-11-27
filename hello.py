f=open("sample.txt", 'r')
content = f.read()
f.close()


#1_ReplaceText
textToReplace = input("Please enter the word to be replaced : ")
replacementText = input ("Please enter the replacement word : ")
lContent = content.lower()
textToReplaceLower = textToReplace.lower()

after_replacement = ""
i=0

while i < len(content):
    if lContent[i:i+len(textToReplaceLower)] == textToReplaceLower:
        after_replacement += replacementText
        i += len(textToReplace)
    else:
        after_replacement += content[i]
        i+=1

print("Text after replacement is : " + after_replacement)

f=open("sample.txt", 'w')
f. write(after_replacement)
f.close


#2_WordFrequency
words = content.split()
wordInput = input("Please enter the word frequency to be counted : ")


wordFreq = {}
for word in words:
    if word in wordFreq:
        wordFreq[word] += 1
    else:
        wordFreq[word] = 1

if wordInput in wordFreq:
    print ("The word", wordInput, "appears", wordFreq[wordInput], "times in the Text ")
else:
    print ("The word", wordInput, "is not in the text")



#3_TextAnalysis

numSentence = 0
numWords = 0
numCharacters = len(content)

numWords = len(words)

for char in content:
        if char in ['.']:
            numSentence += 1

print ("There are", numSentence, "sentences,", numWords, "words and", numCharacters, "characters in this Text" )



#4_LongestWord

longest_word = ""

for word in words:
    for punctuation in ',.':
        word = word.replace(punctuation, "")

        if len(word) > len(longest_word):
            longest_word = word

print("Longest word: ", longest_word)
print("Length of the longest word :", len(longest_word))



#5_Palindrome

palindromes = []

for word in words:
    lword = word.lower()
    if lword == lword [::-1] and len(lword) > 1:
        palindromes.append(word)

print("Palindrome words:",", ".join(palindromes))
