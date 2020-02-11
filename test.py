import os
import time
import datetime
tasks=[]


def te(input):

   out = os.path.basename(input)
   tasks.append("Name of the file:")
   tasks.append(out)

   return(tasks)
def mod(input):




   tt=os.stat(input)[-2]
   to=os.stat(input).st_mtime
   out=os.path.getmtime(input)
   tasks.append("Modified:")
   tasks.append(out)
   #tasks.append(to)
   #tasks.append(tt)
   return(tasks)


def cre(input):



   tt=os.stat(input)[-2]
   to=os.stat(input).st_mtime
   out = os.path.getctime(input)
   tasks.append("Created:")
   tasks.append(out)
   #tasks.append(to)
   #tasks.append(tt)
   return (tasks)


def trm(input):
   modified = os.path.getctime(input)
   tasks.append("Created Date is:")
   t=time.ctime(modified)
   tasks.append(t)
   return (tasks)
  # print("Date modified: %02d/%02d/%d %02d:%02d:%02d"%(day,month,year,hour,minute,second))
def md(input):
   modified = os.path.getmtime(input)
   tasks.append("Modified Date is:")
   t=time.ctime(modified)
   tasks.append(t)
   return (tasks)
def size(input):
   b = os.path.getsize(input)
   tasks.append("File Size is:")
   tasks.append(b)
   return (tasks)
def direc(input):
   tasks.append("Type")
   if os.path.isdir(input):

      tasks.append("It is a Directory")
   else:
      tasks.append("It is a File")
   return (tasks)
