#!/usr/bin/env python

from turing.turing import TuringMachine
import sys

"""
Command line script to take in a file of a Turing Machine instruction set.
Prints if the word is accepted or rejected by the Turing Machine.
Client code that uses turing.py.
"""


def verify_args():
	# checks for 3 params
	if len(sys.argv) != 3:
		print("Usage: ./turing_script.py <INPUTFILE> <WORD>")
		exit(1)
	# stores params in variables
	input_file = sys.argv[1]
	input_word = sys.argv[2]
	return input_file, input_word


def main():
	input_file, input_word = verify_args()
	try:
		turing = TuringMachine(input_file)
	except ValueError as e:
		print(str(e))
		exit(1)
	except FileNotFoundError as e:
		print(str(e))
		exit(1)
	accepted = turing.run_machine(tape=input_word)
	print(f'Accepted: {input_word}' if accepted else f'Rejected: {input_word}')


if __name__ == '__main__':
	main()
