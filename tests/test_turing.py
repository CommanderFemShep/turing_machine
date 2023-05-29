from turing.turing import TuringMachine
import unittest


class TuringTests(unittest.TestCase):
    """
    Simple test class to test both files (palindrome.txt and doublea.txt) to verify implementation.
    """
    def test_palindrome_valid(self):
        machine = TuringMachine('../palindrome.txt')
        # True if word is palindrome (str(word).reverse() == str(word)), else false
        self.assertTrue(machine.run_machine('aba'))
        self.assertTrue(machine.run_machine('abba'))
        self.assertTrue(machine.run_machine('ababa'))
        self.assertTrue(machine.run_machine('aa'))

    def test_palindrome_invalid(self):
        machine = TuringMachine('../palindrome.txt')
        self.assertFalse(machine.run_machine('ba'))
        self.assertFalse(machine.run_machine('bba'))
        self.assertFalse(machine.run_machine('abab'))
        self.assertFalse(machine.run_machine('ab'))

    def test_doublea_valid(self):
        machine = TuringMachine('../doublea.txt')
        # True if the word has two contiguous a's, else false
        self.assertTrue(machine.run_machine('aaba'))
        self.assertTrue(machine.run_machine('abbaa'))
        self.assertTrue(machine.run_machine('abaaba'))
        self.assertTrue(machine.run_machine('aa'))

    def test_doublea_invalid(self):
        machine = TuringMachine('../doublea.txt')
        self.assertFalse(machine.run_machine('ba'))
        self.assertFalse(machine.run_machine('bba'))
        self.assertFalse(machine.run_machine('abab'))
        self.assertFalse(machine.run_machine('aba'))


if __name__ == '__main__':
    unittest.main()
