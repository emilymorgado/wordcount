# put your code here.

def file_to_list(filename):
# open file
    file_contents = open(filename)
# loop through lines of file
    # print file_contents
    word_list = []
    for line in file_contents:
       #print line
        line = line.strip().split(" ")
        for word in line:
            word_list.append(word.lower()) #beautiful hack by Emily to make all words lowercase
       #print words
       # word_list.append(line)
    file_contents.close() #crazy!  we have to close our variable, not the filename!
   # print word_list
    return word_list
# split each line using spaces
# now we have a list of all the words
#close file
# return a list




def list_to_dictionary(list_of_words):
    D = {}
    for word in list_of_words:

# create an empty dictionary
# loop over the word list 
# feed dictionary:
        if word not in D:
           # print word
           D[word] = 1
        else:
            D[word] += 1 
    return D
    # if the word is already in the dictionary increment the value for that word

# print dictionary

L = file_to_list("test.txt")
output = list_to_dictionary(L)

print output


