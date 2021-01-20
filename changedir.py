"""Python program to change directories from home folder"""
import os
import time
from glob import *

cwd = os.getcwd()

os.system("color 0a")
print("You're in " + cwd)
# for each time you want to change a directory from hoe directory
def chdir_from_home(nextDir):
	cwdLocal = os.getcwd()
	if cwdLocal != 'C:\\Users\\Oliver':
		os.chdir('C:\\Users\\Oliver')
	else:
		pass

	os.system("color 0c")
	os.chdir(os.getcwd() + "\\" + nextDir)
	print("You were in " + cwdLocal + "\nYou have hopped to " + os.getcwd())
	time.sleep(7)


print("Here's a list with files and folders in the Home directory and their respective indices: (C:\Users\Oliver)")
# ls = os.listdir('C:\\Users\\Oliver')

#this thread has been copy pasted directly
for root, dirnames, filenames in os.walk('C:\\Users\\Oliver'):
	ls = dirnames
	break

for i in range(len(ls)):
	print(i, ls[i])

nextDir = input("what directory in Home folder d'you wanna move to? ")

chdir_from_home(nextDir)