#!/usr/bin/env python

import sys

# CS 4110 Formal Languages and Algorithms
# Command line script to take in a file of a Turing Machine Tape, and run a given word
# against it to see if the word is accepted or rejected by the Turing Machine.
# Marley Stark


# checks for 3 params
if len(sys.argv) != 3:
	print("Usage: ./turing <INPUTFILE> <WORD>")
	exit(1)


# stores params in variables
ifile = sys.argv[1]
iword = sys.argv[2]
tape = []
tpos = 0 	# updated with index of tape list as it moves (aka the head)
trans_count = 0
from_state = ""


# Adds the provided word into the tape, followed by blanks
for letter in iword:
	tape.append(letter)
for i in range(1000):
	tape.append("_")

transition_map = {}

# Reads Turing Machine file and sets up our Turning Machine structure
with open(ifile, 'r', newline='') as f:
	next(f)
	while line := (f.readline().strip()):  # read lines and strip whitespace
		# File is FromState, FromChar, ToChar, Direction, ToState (so we set up that structure)
		try:
			from_state, from_char, to_char, direction, to_state = line.split(',')
			from_state = from_state.strip().lower()
			to_state = to_state.strip().lower()
			from_char = from_char.strip().lower()
			to_char = to_char.strip().lower()
			direction = direction.strip().upper()
		except Exception:
			continue
		if 'start' in from_state.lower():
			start_state = from_state
		if from_state not in transition_map:
			transition_map[from_state] = {}
		# Create transition map with input from_state & from_char, to output a dictionary to_char, direction, to_state
		transition_map[from_state][from_char] = {'to_char': to_char, 'direction': direction, 'to_state': to_state}


# Checks that provided tape has a start state!
if not any('start' in x.lower() for x in transition_map):
	print("Rejected: " + iword + "\n")


# recursive function to check each letter of the provided word until it's accepted or rejected
def turing(tape, tpos, trans_count, start_state):

	from_state = start_state
	for trans_count in range(1000):
		from_char = tape[tpos]
		# check if both keys are in transmap (one at a time)
		if from_state in transition_map:
			if from_char in transition_map[from_state]:
				to_vals = transition_map[from_state][from_char]
				to_state = to_vals['to_state']
				to_char = to_vals['to_char']
				direction = to_vals['direction']


				if direction.upper() == "L":
					# check if valid tape move (can't go left at start)
					if tpos < 0:
						print("Rejected: " + iword + "\n")
					else:
						from_char = to_char
						tape[tpos] = to_char
						tpos -= 1
						from_state = to_state

				elif direction.upper() == "R":
					from_char = to_char
					tape[tpos] = to_char
					tpos += 1
					from_state = to_state

				elif direction.upper() == "S":
					from_char = to_char
					tape[tpos] = to_char
					from_state = to_state

				if "halt" in from_state.lower():
					print("Accepted: " + iword + "\n")
					return
				else:
					trans_count += 1

			else:
				print("Rejected: " + iword + "\n")
				return

		else:
			print("Rejected: " + iword + "\n")
			return

	if trans_count == 1000:
		print("Rejected: " + iword + "\n")
		return  # or exit(0)


turing(tape, tpos, trans_count, start_state)

