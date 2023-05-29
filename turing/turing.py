import os

"""
This code was initially created for CS 4110 Formal Languages and Algorithms. It has been updated to be more 
usable by clients and better reflect good software practices.

Given the set of instructions from the given input file, the transition map is built with input keys 
from_state & from_char, and maps to a dictionary of values to_char, direction, to_state. Running the 
Turing Machine essentially takes the transition map and runs the tape (given word) against it by checking the 
present state and char the tape is on and seeing if it moves left, right, or halts. If it halts, the word is accepted.
Otherwise the word is rejected.
"""


class TuringMachine:
	def __init__(self, filepath: str, max_length: int = 1000):
		"""
		The class TuringMachine builds a transition map from the given input file 'filepath' and runs the
		given tape against it to see if the word is accepted or rejected by the Turing Machine.

		:param filepath: Text file in current directory, i.e. 'doublea.txt' or 'palindrome.txt'
		:param max_length: Integer for maximum length of tape
		"""
		self.filepath = filepath
		self.max_length = max_length
		if not os.path.isfile(self.filepath):
			raise FileNotFoundError(f'`{self.filepath}` is not a valid filepath')
		if not isinstance(max_length, int) or max_length <= 0:
			raise ValueError('Invalid max_length, must be a positive integer')
		self.transition_map, self.start_state = None, None
		self.build_transition_map()

	def build_transition_map(self):
		"""
		Builds the transition map
		{
			'from_stateA': {
				'from_charA1': {
					'to_char': str,
					'to_state': str,
					'direction': str
				},
				'from_charA2': ...
			},
			'from_stateB': ...
		}
		by reading the given file `self.filepath`, and maps the input keys from_state & from_char to a
		dictionary of values to_char, direction, and to_state to set up the structure of the Turing Machine.
		"""
		transition_map = {}
		with open(self.filepath, 'r', newline='') as f:
			next(f)
			while line := (f.readline().strip()):  # read lines and strip whitespace
				# File format is FromState, FromChar, ToChar, Direction, ToState (so we set up that structure)
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

		# Checks that provided tape has a start state
		if not any('start' in x.lower() for x in transition_map):
			raise ValueError("Invalid tape start state")
		self.transition_map = transition_map
		self.start_state = start_state

	def get_tape(self, word: str):
		"""
		Takes input word and returns a tape digestible by TuringMachine

		:param word: String to be turned into a tape
		:return: List of chars from input 'word' followed by underscores up to max_length
		"""
		return [letter for letter in word] + (['_'] * (self.max_length - len(word)))

	def run_machine(self, tape):
		"""
		Iterative function to check each letter of the provided word until it's accepted or rejected.

		:param tape: List of chars, or string
		:return: Boolean on whether the tape was accepted or rejected
		"""
		if isinstance(tape, str):
			# converts a given word into a tape if it is just a string
			tape = self.get_tape(tape)
		if '_' not in tape:
			raise ValueError(f'Tape length is longer than {self.max_length}')
		tape_position = 0  # updated with index of tape list as it moves (aka the head)
		from_state = self.start_state
		for trans_count in range(self.max_length):
			if tape_position < 0:
				return False
			from_char = tape[tape_position]
			# check if both keys are in transition map (one at a time)
			if from_state in self.transition_map:
				if from_char in self.transition_map[from_state]:

					to_state = self.transition_map[from_state][from_char]['to_state']
					to_char = self.transition_map[from_state][from_char]['to_char']
					direction = self.transition_map[from_state][from_char]['direction']
					from_state = to_state
					tape[tape_position] = to_char

					if direction.upper() == 'R':
						tape_position += 1
					if direction.upper() == 'L':
						tape_position -= 1

					if "halt" in from_state.lower():
						return True
					else:
						trans_count += 1
				else:
					return False
			else:
				return False
		return False
