import os
import sys
import time
import datetime
import codecs
from subprocess import check_output

####################################################################################################
# Version 1.01
#
# review script designed to check each file in a data set, and open the files in gedit if they have
# not already been reviewed.
# 
# Functions: N/A
# 
#
# INVOKING INSTRUCTIONS:
# python check_files.py sets/<filename>.txt
#
#
# Updates from Version 1.00:
# -Documentation
####################################################################################################


if __name__ == "__main__":
  if (len(sys.argv)!=2):
      print("usage: {0} <count>".format(sys.argv[0]))
      sys.exit(1)
#  start = time.clock()
  x_file = open(str(sys.argv[1]),'r')
  print ("Exploring: ", x_file)
#  initSize=0
  log=open("reviewed.txt",'r+')
  for line in x_file:
    if line in log:
      pass
    else:
      log.write(line)
      os.system("gedit "+line.strip())
      
  print("All Files Reviewed")
  x_file.close()
  log.close()
