#!/usr/bin/python3

import zipfile
import optparse
import os

def main():
	parser = optparse.OptionParser('Usage: -w <Wordlist> -f <zip file>')
	parser.add_option('-w', dest='wordlist', type='string', help='specify wordlist')
	parser.add_option('-f', dest='infile', type='string', help='specify zip file')
	options, args = parser.parse_args()
	wordlist = options.wordlist
	infile = options.infile
	if (wordlist == None) | (infile == None):
		print(parser.usage)
		exit(0)
	unzip(wordlist, infile)

def unzip(wordlist, infile):
	zipbool = zipfile.is_zipfile(infile)
	if zipbool == False:
		print("this file isn't a zip file, try again butthead")
		exit(0)
	z = zipfile.ZipFile(infile)
	print("These are the available zip files in this folder:")
	for name in z.namelist():
		print(name)
	zname = input("which file do you want to unzip?: ")
	wl = open(wordlist, 'r')
	found = False
	for word in wl:
		try:
			if found == False:
				os.system("clear")
				print("running through wordlist...")
				print(word, end='')
				bword = bytes(word.rstrip(), 'ascii')
				zfile = z.open(zname, 'r', bword)
				print("Password Found!")
				for zword in zfile:
					print(str(zword)[2:-1])
				found = True
		except:
			print("nope")

	z.close()

if __name__== "__main__":
	main()
	
#hi Justin
