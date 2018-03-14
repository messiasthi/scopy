#! /usr/bin/env python
import os
import sys

params = [
	'from',
	'to',
	'keywords',
	'newwords',
	'uppercase',
	'lowercase',
	'bothcase'
]

def help():
	print("The scopy is a alias to copy paste files")
	print("with one difference, find and replace words or expressions.")
	print("version: 1.0")
	print("bug report/issues on https://github.com/messiasthi/scopy")
	print("Usage:")
	print("\tscopy from=\"/path/to/template.file\" to=\"/path/to/new.file\" keywords=\"example1\" replaces=\"replace\"")
	print("\t\tfrom\tThe original file")
	print("\t\tto\tThe new file")
	print("\t\tkeywords\tWords to replace for a new word")
	print("\t\tnewwords\tNew words")
	exit(0)

def replace(line, words, replaces):
	newLine = line
	for word in words:
		if word.lower() in newLine:
			newLine = newLine.replace(word, replaces[words.index(word)].lower())
		if word.upper() in newLine:
			newLine = newLine.replace(word.upper(), replaces[words.index(word)].upper())
		if word.title() in newLine:
			newLine = newLine.replace(word.title(), replaces[words.index(word)].title())
	return newLine

def scp(paramsFromCommandline):
	verbose = False
	if len(paramsFromCommandline) == 1:
		help()

	for value in paramsFromCommandline:
		if "--help" in value or "-help" in value or "help" in value:
			help()
		elif "from=" in value:
			originalFile = value.replace("from=", "")
		elif "to=" in value:
			newFile = value.replace("to=", "")
		elif "keywords=" in value:
			words = value.replace("keywords=", "").split()
		elif "replaces=" in value:
			replaces = value.replace("replaces=", "").split()
		elif "verbose" in value:
			verbose = True

	if verbose:
		print(paramsFromCommandline)

	if len(words) != len(replaces):
		print("Error: The number of words and replaces must be equals")
		exit(1)

	if os.path.isfile(originalFile):
		if not os.path.isfile(newFile):
			with open(originalFile, "r") as of, open(newFile, "w") as nf:
				for line in of:
					newLine = replace(line, words, replaces)
					if verbose:
						print(line, " => ", newLine)
					nf.write(newLine)

			exit(0)
		else:
			print("Error: The new file already exists")
			exit(1)
	else:
		help()
		exit(0)
	exit(1)

def main():
	scp(sys.argv)
