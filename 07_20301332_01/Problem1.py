


def palindrome(word):
    if word == None:
        return "Not palindrome."
    n = len(word)
    i = 0
    while(i<n/2):
        if word[i] != word[n-1-i]:
            return "is Not a palindrome."
        i = i + 1
    return "is a Palindrome."


odd = 0
even = 0
palindrom = 0
non_palindrome = 0
noparity = 0

a = open("LAb1input.txt","r")
file = a.read()
file = file.split("\n")
file = file[:len(file)-1]
length =len(file)
res = open("output.txt","w")
rec = open("record.txt","w")

for i in file:
    word = i.split()
    number = float(word[0])
    word = word[1]
    if number %2==0:
        if palindrome(word) == "is a Palindrome.":
            palindrom += 1
        else:
            non_palindrome += 1
        even += 1
        res.write(str(number)+" has even parity and "+word + " "+palindrome(word)+"\n")
    elif number %2 == 1:
        if palindrome(word) == "is a Palindrome.":
            palindrom += 1
        else:
            non_palindrome += 1
        odd += 1
        res.write(str(number)+" has odd parity and "+word + " "+palindrome(word)+"\n")
    else:
        if palindrome(word) == "is a Palindrome.":
            palindrom += 1
        else:
            non_palindrome += 1
        noparity += 1
        res.write(str(number)+" has no parity and "+word + " "+palindrome(word)+"\n")



rec.write("Percentage of Odd parity: "+ str((odd/length)*100)+"%"+"\n")
rec.write("Percentage of Even parity: "+ str((even/length)*100)+"%"+"\n")
rec.write("Percentage of no parity: "+ str((noparity/length)*100)+"%"+"\n")
rec.write("Percentage of Palindrome: "+ str((palindrom/length)*100)+"%"+"\n")
rec.write("Percentage of Non Palindrome: "+ str((non_palindrome/length)*100)+"%"+"\n")
a.close()









































