#!/usr/bin/python
import os
import csv
import time

tupHeaders = [('File Name', 'Created')]

print "***** Program for listing all files in a directory recursively ******"
strOutFile = ''
while strOutFile.strip() == '':
	strOutFile = raw_input("What is the base name of the output file? (Don't add any extension): ")


def directoryTree(listOutFiles, directory, files):
	for strFile in files:
		strFullName = directory + os.sep + strFile
		if os.path.isfile(strFullName):
			objTime = time.strftime('%d/%m/%Y', time.localtime(os.stat(strFullName).st_ctime))
			print strFullName , "\t\t" ,  objTime
			tupOut = (strFullName[2:], objTime)
			listOutFiles.append(tupOut)

listFiles = []
os.path.walk(".", directoryTree, listFiles)

listFiles = tupHeaders + listFiles


with open(strOutFile + '.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerows(listFiles)
print ">>> File " + strOutFile + '.csv' + " was created" 

with open(strOutFile + '.txt', 'w') as f:
	for tupRow in listFiles:
		f.write( "\t".join(tupRow) + "\n")
print ">>> File " + strOutFile + '.txt' + " was created" 



raw_input("Press enter to exit ... ")

