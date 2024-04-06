import filecmp

import download
# path of this script
dir1 = "<path to where the original file was stored>"
dir2 = "<path to where the file downlaoded from cloud is stored>"

# get fileNames from user
f = input("\nEnter the file to be checked for modifications: ")
f1 = dir1 + f
f2 = dir2 + f

# deep comparison
result = filecmp.cmp(f1, f2, shallow=False)

if result == True:
	a = input("No modiciations detected, do you wish to decrypt the file? (Y/n)")
	if a == "Y":
		import aes_dec
	elif a == "n":
		print("Okay. Thank you!")
	else:
		print("Invalid option!")
else:
	print("Error! Modifications detected in file")
