#! /usr/bin/env python
import os
import sys

def main():
	scp(sys.argv)

params = [
	'from',
	'to',
	'keywords',
	'newwords',
	'regex',
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
	print("\tscopy from=\"/path/to/template.file\" to=\"/path/to/new.file\" keyword=\"example1\" replace=\"replace\"")
	print("\t\tfrom\tThe original file")
	print("\t\tto\tThe new file")
	print("\t\tkeywords\tWords to replace for a new word")
	print("\t\tnewwords\tNew words")

def replace(line):
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
	originalFile=""
	newFile=""
	words=""
	replaces=""

	for value in paramsFromCommandline:
		if "--help" in value or "-help" in value or "help" in value:
			help()
			exit(0)
		elif "from=" in value:
			originalFile = value.replace("from=", "")
		elif "to=" in value:
			newFile = value.replace("to=", "")
		elif "keywords=" in value:
			words = value.replace("keywords=", "").split()
		elif "replaces=" in value:
			replaces = value.replace("replaces=", "").split()

	if len(words) != len(replaces):
		print("Error: The number of words and replaces must be equals")
		exit(1)

	if os.path.isfile(originalFile):
		if not os.path.isfile(newFile):
			with open(originalFile, "r") as of, open(newFile, "w") as nf:
				for line in of:
					newLine = replace(line)
					nf.write(newLine)


		else:
			print("Error: The new file already exists")
			exit(1)
	else:
		help()
		exit(0)
