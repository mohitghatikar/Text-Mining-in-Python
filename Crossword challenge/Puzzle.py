# -*- coding: utf-8 -*-
"""
Created on Sat Mar 05 19:43:50 2016

@author: mohit
"""

import re

# Open Puzzle 
fr=open('C:\Users\mohit\Desktop\Spring BIA\Web Analytics\Word search\puzzle.txt')
text=fr.read().strip()
fr.close()

print text

# Transpose puzzle 
vertical = ''
text2 = text.split()
for x in zip(*text2):
    vertical += ''.join(x) + '\n'
print vertical

# open words
tr=open('C:\Users\mohit\Desktop\Spring BIA\Web Analytics\Word search\words.txt')
words=tr.read().strip()
tr.close()

words = words.split()
words_found = []
for word in words:
    m_horizontal = re.search(word,text)
    if m_horizontal: # if a match exists then append to words_found
        words_found.append(m_horizontal.group())
    m_horizontal_reverse_word = word[::-1] 
    m_horizontal_reverse = re.search(m_horizontal_reverse_word,text)
    if m_horizontal_reverse:
        words_found.append(m_horizontal_reverse.group()[::-1])
    m_vertical = re.search(word,vertical)
    if m_vertical:
        words_found.append(m_vertical.group())
    m_vertical_reverse_word = word[::-1]
    m_vertical_reverse = re.search(m_vertical_reverse_word,vertical)
    if m_vertical_reverse:
        words_found.append(m_vertical_reverse.group()[::-1])
        
for word in words:
    if word not in words_found:
        print word,':Not found'
    else:
        print word,':It exists in the puzzle'
        
print 'the words that are present in the puzzle are', words_found
        

  
          
            
        