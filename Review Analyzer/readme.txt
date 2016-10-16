1) reviewAnalyzer.py - Reads a list of reviews and decide if each review is positive or negative, based on the occurences of positive and negative words.
Writes the results in a file.

2) Assignment-2.py - The solution to the problem descibed below:

Consider the following  4 reviews:

The food was very bad 
Bad food, bad service
I like the food there
The food is not terrible


The REVIEW COUNT of 'bad' is the number of reviews (lines) that include the word 'bad'. The answer in this case is 2.

Step 1: Write a script that prints the REVIEW COUNT of each negative word that appears in 'input.txt' that we used in class.  For the simple example provided above, the answer would be:

bad 2

terrible 1

Step 2: Extend your script so that it prints the negative word with the highest REVIEW COUNT in 'input.txt'. If more than 1 words have the top count, then just print any one of them. In the above example, the winner is the word 'bad'