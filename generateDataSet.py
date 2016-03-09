import os
import sys
import codecs
import random
import time
import datetime
import subprocess
from subprocess import check_output
####################################################################################################
# version 3.01
#
# Script designed to take 4 parameters, the corpus directory, the number of authors, the number
# the number of emails per author, and the number of words per email.  Prints out to terminal, a
# files that fit the specified criteria.
# 
# Functions:
# wc(filename)                             - Takes in a filepath and returns the word count as an
#                                            integer.
#
# authorValid(author, minNum, msgs)        - Takes in the name of the author, the minimum number of 
#                                            words each email must have, and an empty list of
#                                            messages.  The function tests whether the word count
#                                            of a message meets the minimum threshold.  if so, the 
#                                            the message is added to the message list.  If the
#                                            author has enough messages at the given word count,
#                                            (the count of messages > minNum) the funciton returns 
#                                            true. The author is valid.
#
# getAuthors(root,num,emails,words)        - Passes in a root directory, the number of authors expected
#                                            the number of emails per author, and the number of words
#                                            per email.  Creates a list of authors and shuffles them
#                                            to ensure randomness.  Then until the requisite authors
#                                            have been found, the funciton tests to see if the authors
#                                            in the list are valid by calling authorValid. If the author
#                                            is valid, the funciton prints num file paths to the
#                                            terminal.
#
# INVOKING INSTRUCTIONS:

# From the command line, type: python generateDataSet_v2.py <root> <authors> <emails> <wordCount> > docName.txt
#
# Updates from v2:
# - added parameter to specify minimum word count
# - returns to a list format to ensure randomization and no repeats
# - wc, authorValid, and getAuthors funcitons
# - Documentation
####################################################################################################

def wc(filename):
  return int(check_output(["wc", "-w", filename]).split()[0])

def authorValid(author, minNum, msgs): # checks to see if author has requisite number of emails with words per email
  counter=0
  for subdirs,dirs,files in os.walk(root+author):
    for item in files:
      f_path=root+author+'/'+item
      w_count=wc(f_path)
      if (w_count>=minNum):
        counter+=1
        msgs.append(f_path)
  if (counter>minNum): 
    return True
  else: 
    return False

def getAuthors(root,num,emails,words):
  authLis= os.listdir(root)
  random.shuffle(authLis)
  ansLis=list()
  while (len(ansLis)<=num):
    #Begin author selection process
    for auth in authLis:
      messageLis=list()
      path=root+auth+'/'
      flag = authorValid(auth,words,messageLis)
      if (flag):
        ansLis.append(auth)
        random.shuffle(messageLis)
        for x in range(0,emails):
          print(messageLis[x])
        if (len(ansLis)==num):
          break
    break
  return 0
      


if __name__ == "__main__":
   if (len(sys.argv)!=5):
      print("usage: {0} <count>".format(sys.argv[0]))
      sys.exit(1)
   root = sys.argv[1]
   author = int(sys.argv[2])
   emails = int(sys.argv[3])
   words = int(sys.argv[4])
   getAuthors(root,author,emails,words)



# ALGORITHM->
# Tasks:  Get a random author
#         get all their emails of a given word count
#         if there are less emails of a given word count than what's asked, find a new author
#         randomize the list of emails for the author
#         pick the top x emails
#         repeat for given number of authors, ensuring that authors are not repeated.

