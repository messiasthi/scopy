#! /usr/bin/env python
import os
import sys

def help():
	print("The scopy is a alias to copy paste files")
	print("with one difference, find and replace words or expressions.")
	print("version: 1.1")
	print("bug report/issues on https://github.com/messiasthi/scopy")
	print("Usage:")
	print("\tscopy from=\"/path/to/template.file\" keywords=\"example1\" replaces=\"replace\"")
	print("\t\tfrom\tThe original file")
	print("\t\tkeywords\tWords to replace for a new word")
	print("\t\tnewwords\tNew words")
	print("\t\tuppercase|lowercase|titlecase|allcases[default]\tReplace only specific cases, all cases is default, but you can pass one or more.")
	exit(0)

def replace(line, words, replaces, lower, upper, title):
	wordsInLine = line.split()
	newLine = []
	for word in wordsInLine:
		if title and word.istitle() and word.lower() in words:
			# print("case: title -> " + word + " -> " + replaces[ words.index( word.lower() ) ].title())
			newLine.append( replaces[ words.index( word.lower() ) ].title() )
		elif lower and word.islower() and word.lower() in words:
			# print("case: lower -> " + word + " -> " + replaces[ words.index( word.lower() ) ].lower())
			newLine.append( replaces[ words.index( word.lower() ) ].lower() )
		elif upper and word.isupper() and word.lower() in words:
			# print("case: upper -> " + word + " -> " + replaces[ words.index( word.lower() ) ].upper())
			newLine.append( replaces[ words.index( word.lower() ) ].upper() )
		else:
			newLine.append(word)
	return " ".join(newLine)

def scp(paramsFromCommandline):
	verbose = False
	if len(paramsFromCommandline) == 1:
		help()

	allcases = True
	titlecase = False
	lowercase = False
	uppercase = False

	for value in paramsFromCommandline:
		if "--help" in value or "-help" in value or "help" in value:
			help()
		elif "from=" in value:
			originalFile = value.replace("from=", "")
		elif "keywords=" in value:
			words = value.replace("keywords=", "").lower().split()
		elif "replaces=" in value:
			replaces = value.replace("replaces=", "").lower().split()
		elif "verbose" in value:
			verbose = True
		elif "uppercase" in value:
			uppercase = True
			allcases = False
		elif "lowercase" in value:
			lowercase = True
			allcases = False
		elif "titlecase" in value:
			titlecase = True
			allcases = False
		elif "allcases" in value:
			allcases = True

	if allcases:
		titlecase = True
		lowercase = True
		uppercase = True

	if verbose:
		print(paramsFromCommandline)

	if len(words) != len(replaces):
		print("Error: The number of words and replaces must be equals")
		exit(1)

	if os.path.isfile(originalFile):
		with open(originalFile, "r") as of:
			for line in of:
				newLine = replace(line, words, replaces, lowercase, uppercase, titlecase)
				if verbose:
					print(line, " => ", newLine)
				print(newLine)

		exit(0)
	else:
		help()
		exit(0)
	exit(1)

def main():
	scp(sys.argv)
