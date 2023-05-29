#!/usr/bin/env python

from turing.turing import TuringMachine
import sys

"""
Command line script to take in a file of a Turing Machine instruction set, and also converts a given word into a tape.
Prints if the word is accepted or rejected by the Turing Machine.
Client code to easily use turing.py.
"""


def verify_args():
	# checks for 3 params
	if len(sys.argv) != 3:
		print("Usage: ./turing_script <INPUTFILE> <WORD>")
		exit(1)
	# stores params in variables
	ifile = sys.argv[1]
	iword = sys.argv[2]
	return ifile, iword


def main():
	ifile, iword = verify_args()
	max_length = 1000
	tape = [letter for letter in iword] + (['_'] * (max_length - len(iword)))
	try:
		turing = TuringMachine(ifile, max_length=max_length)
	except ValueError:
		print('Invalid turing machine file')
		exit(1)
	except FileNotFoundError:
		print('File not found')
		exit(1)
	accepted = turing.run(tape=tape)
	out_str = f'Accepted: {iword}' if accepted else f'Rejected: {iword}'
	print(out_str)


if __name__ == '__main__':
	main()
