# In a directory with hundreds of files in it,look for the right ones with specific key
import glob


# print(glob.glob("*")) # to check files in current folder


key = input("Enter your keyword: ") #Enter any key word in that file

# glob.glob("*.txt") returns a list of files in current directory with .txt extension

for file in glob.glob("*.txt"): 
	with open(file,"r") as f:
		if key in f.read():
			print(file)
