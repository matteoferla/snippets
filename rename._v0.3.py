#Script to sort photo variants into folders based on the DSC\d+ label.
#Note. os.path.isfile(x) was saying falsely saying some files were false.
# No idea why.

import os
import os.path
#import sys
import glob
import re


#name=sys.argv[0]
#print("The command-line argument passed for the example is "+name+"\n")
n="ERROR"
for file in sorted(glob.glob("*")):
  if file.find('.py')>0:
    pass
  else:
    if os.path.isdir("file") == False:
      #DSC06272
      if file.find(n)==-1:
        try:
          new=re.search('DSC[0-9]+',file).group(0)
          print('Mkdiring '+new)
          if os.path.isdir(new):
            pass
          else:
            os.mkdir(new)
          n=new
        except AttributeError:
          pass
      else:
        print(file+' changed to '+n)
        os.rename(file,n+'\\'+file)
    else:
     print(file+' is not a file')
print("DONE")
