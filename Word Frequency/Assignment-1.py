# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 22:57:18 2016

@author: mohit
"""

"""
Assignment - 1
Counts the maximum occurance of a word that shows up in all the posts in the file

"""

#Make a new empty dictionary. This will hold the number of occurences per word
word_freq=dict() # Can aslo use {}

file_conn=open('C:\Users\mohit\Desktop\Spring BIA\Web Analytics\Week 2\data')#open a connection to the input file

for line in file_conn: # for every line in the input
    
    # the strip() function removes spaces, tabs, and 'line change' 
    # character from the start and end of a piece of text. 
    #Look at what happens to the count of the word 'house' if we don't do this strip.
    line=line.strip() # it removes deadspace from the beginning to the end of the line
    
    columns=line.split('@') # split according to the delimeter
    # If we use .split() then it will split from the space
  
    user=columns[0] # get the user
    day=columns[1] # get the day   
    post=columns[2] #get the post

    words=post.split(' ')#split the post on the space to get a list of the words
    for word in words: # for each word in the post
        if word in word_freq:# the word has been seen before, add +1 to its count.
            word_freq[word]=word_freq[word]+1
        else:
            word_freq[word]=1 # first time we see this word, initialise its count to 1.
    

file_conn.close() # always remember to close the connection once your are done working with a file


# Find the maximum count from the dictionary
# Store the maximum count value in max_count
max_count = max(word_freq.values())

print max_count

# Store all the words from the dictionary in a list which has the maximum count value

list = []
for item in word_freq:
    if max_count == word_freq[item]:
        list.append(item)

# Print the list with all the words with the highest count

print list

# The list contains the words: 'house', 'is' and 'to'. Print any one of these words

print list[0] or list[1] or list[2]