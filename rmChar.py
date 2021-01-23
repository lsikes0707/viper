i#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# Read a text file, remove specific set of characters

def main():
def rm_fn(trgt,dsrd):
	directory=raw_input("Your text files contain false data. To remove them, enter path/your_directory: ")
	for f in directory:
		fopen=open(f, 'r')
		for word in fopen:
			if word.startswith(trgt):
				replace(dsrd, '')
		fopen.close()
