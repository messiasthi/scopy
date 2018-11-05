#! /usr/bin/env python
import os
import sys


def help():
	print("""The scopy is a alias to copy paste files with one difference, find and replace words or expressions. 
	bug report/issues on https://github.com/messiasthi/scopy
	version: 1.1
	Usage:
	\tscopy from=\"/path/to/template.file\" keywords=\"example1\" replaces=\"replace\"
	\t\tfrom\t\tThe original file
	\t\tkeywords\tWords to replace for a new word
	\t\tnewwords\tNew words
	\t\tuppercase|lowercase|title_cases|all_cases[default]\tReplace only specific cases, all cases is default, but you can pass one or more.""")
	exit(0)


def replace(line, words, replaces, lower, upper, title):
	words_in_line = line.split()
	new_line = []
	for word in words_in_line:
		if title and word.istitle() and word.lower() in words:
			# print("case: title -> " + word + " -> " + replaces[ words.index( word.lower() ) ].title())
			new_line.append( replaces[ words.index( word.lower() ) ].title() )
		elif lower and word.islower() and word.lower() in words:
			# print("case: lower -> " + word + " -> " + replaces[ words.index( word.lower() ) ].lower())
			new_line.append( replaces[ words.index( word.lower() ) ].lower() )
		elif upper and word.isupper() and word.lower() in words:
			# print("case: upper -> " + word + " -> " + replaces[ words.index( word.lower() ) ].upper())
			new_line.append( replaces[ words.index( word.lower() ) ].upper() )
		else:
			new_line.append(word)
	return " ".join(new_line)


def scp(params_from_cmdline):
	verbose = False
	if len(params_from_cmdline) == 1:
		help()

	all_cases = True
	title_cases = False
	lowercase = False
	uppercase = False

	for value in params_from_cmdline:
		if "--help" in value or "-help" in value or "help" in value:
			help()
		elif "from=" in value:
			original_file = value.replace("from=", "")
		elif "keywords=" in value:
			words = value.replace("keywords=", "").lower().split()
		elif "replaces=" in value:
			replaces = value.replace("replaces=", "").lower().split()
		elif "verbose" in value:
			verbose = True
		elif "uppercase" in value:
			uppercase = True
			all_cases = False
		elif "lowercase" in value:
			lowercase = True
			all_cases = False
		elif "title_cases" in value:
			title_cases = True
			all_cases = False
		elif "all_cases" in value:
			all_cases = True

	if all_cases:
		title_cases = True
		lowercase = True
		uppercase = True

	if verbose:
		print(params_from_cmdline)

	if len(words) != len(replaces):
		print("Error: The number of words and replaces must be equals")
		exit(1)

	if os.path.isfile(original_file):
		with open(original_file, "r") as of:
			for line in of:
				new_line = replace(line, words, replaces, lowercase, uppercase, title_cases)
				if verbose:
					print(line, " => ", new_line)
				print(new_line)

		exit(0)
	else:
		help()
		exit(0)
	exit(1)


def main():
	scp(sys.argv)
