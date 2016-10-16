# -*- coding: utf-8 -*-
"""
Created on Sat Feb 06 00:02:13 2016

@author: mohit ravi ghatikar
CWID   : 10405877
BIA 660A 

Assignment 2

"""


#function that loads a text file and returns the set
def load(fname):
    new=set() #make a new empty set
    lex_conn=open(fname)#open a connection to the text file
    #add every word in the file to the set
    for line in lex_conn: # for every line in the file
        new.add(line.strip())# remember to strip to remove the line-change character
    lex_conn.close() #close the collection

    return new # work is done, return the text


#load the negative lexicons
file_writer=open('results_of_negative_freq.txt','w') #open a write connection to the output file
ip=load('input.txt')

negLex=load('negative-words.txt')

for sentiment in negLex:
    neglist = []
          
    for line in ip:
        negset = set()        
        
        line = line.lower().strip()
        words = line.split()
        # Check if the word in lexicon is equal to the word in input
        for word in words:
            if sentiment == word:
                negset.add(sentiment)
                break
        # Add the word in the set. Append the number of occurances of the word in the list     
        length = len(negset)
        neglist.append(length)
        
    # If the frequency of the word is greater than 0, write to a file.
    if sum(neglist) > 0:
        
        file_writer.write(sentiment+'\t')
        file_writer.write(str(sum(neglist)))
        file_writer.write('\n')
   
file_writer.close()          
highest = load('results_of_negative_freq.txt')

counter = 0
# Check the highest frequency of the word from the written file.
for word in highest:
    word = word.lower().strip()
    words = word.split('\t')
    
    if int(words[1]) > counter:
        a = []
        counter = int(words[1])
        a.append(words[0])

print 'The word that has the highest frequency is', a
print 'Its frequency is',counter
# The output is the word "loud" and its frequency is 8.
        
        
 


    
    
    
    



    
      

