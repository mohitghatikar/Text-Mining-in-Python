"""
Reads a list of reviews and decide if each review is positive or negative,
based on the occurences of positive and negative words.
Writes the results in a file.

The script uses lists, sets, and dictionaries.

What's a list?
mylist=[1,5,1,7] 
A sequence of elements. Elements stay in the position they were inserted, so you can easily get the element in the i-th position.
Searching for a specific element is slow (linear time). Allows duplicates.
mylist.append(8) would make the list into [1,5,1,7,8] 
print mylist[0] would print 1
mylist.remove(1) would remove the first 1
mylist.index(7) would find and return the index of 7 in the list. In [1,5,1,7], the index is 3. What if the number is not in there?


What's a set?
myset=set([1,5,1,7])
A bucket of elements. Elements added to the set are kept in an unpredictable order. You can't access specific positions.
Searching for a specific element is fast (constant time). No duplicates allowed! (one of the two 1s above will be ignored.)
myset.add(8) would add 8 to the set.
myset.add(5) would do nothing, since 5 is already in there.
myset.remove(1) would remove 1
7 in myset would check if 7 is in the set. Returns True if it is and False otherwise.
Tip:Visualize a set as a list that is updated every time you add a new element, in order to stay sorted 
(it's actually not exactly sorted and a little more complex than that).


What's a  dictionary?
mydict={1:'jim', 5:'george', 1:'maria', '7':'ravi'}
Used to store pairs. The first element in the pair is the key. The second is the value. 
Searching for keys is fast (as fast as in a set). When you find a key, you can immediately gets
No duplicate keys allowed! In the above example, the second 1 key overwrites the first one. In other words, 1:'jim' disappears.
print mydict[5] would look for the key 5 and print its value. In this case it would print 'george'. What if the key doesn't exist?
mydict[8]='chris' would add the key 8, connected with the value 'chris'
del mydict[7] would delete key 7 and its associated value.
7 in mydict would check if key 7 is in the dict. Returns True if it is and False otherwise. Just like sets.

"""

#function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
    newLex=set() #make a new empty set
    lex_conn=open(fname)#open a connection to the lexicon file
    #add every word in the file to the set
    for line in lex_conn: # for every line in the file
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close() #cloes the collection

    return newLex # work is done, return the lexicon


#load the positive and negative lexicons
posLex=loadLexicon('positive-words.txt')
negLex=loadLexicon('negative-words.txt')

file_writer=open('results.txt','w') #open a write connection to the output file

data_conn=open('input.txt') # open a read connection to the input file
for line in data_conn: # for every line in the file (1 review per line)
    posList=[] #list of positive words in the review
    negList=[] #list of negative words in the review

    line=line.lower().strip()#lower-case and remove dead space from the beginning and end of the string
    
    words=line.split(' ') # split on the space to get list of words
    
    for word in words: #for every word in the review
        if word in posLex: # if the word is in the positive lexicon
            posList.append(word) #update the positive list for this review
        if word in negLex: # if the word is in the negative lexicon
            negList.append(word) #update the negative list for this review
           

    decision='Neutral'#in the beginning the decision is netural        
    if len(posList)>len(negList): # more pos words than neg
        decision='Positive' #update decision
    elif len(negList)>len(posList):  # more neg than pos
        decision='Negative' # update decision
         
    file_writer.write(line+'\n') #write the review
    file_writer.write(str(posList)+'\n') # write list of positive words
    file_writer.write(str(negList)+'\n') # write list of negative words     
    file_writer.write(decision+'\n\n') #write the decision
     
#close the two file connectionss
file_writer.close()
data_conn.close()


