import re
import unittest

def load_text_from_file(filename):
    """Load text from a given file and return its content."""
    with open(filename, 'r') as file:
        return file.read()
    
def calibration(text):
    splitted = text.split('\n')
    regex_numbers = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))' 
    sum = 0

    for line in splitted:
        digits = re.findall(regex_numbers, line)
        # print('---digits', digits)
        digits = map_regext_to_number(digits)
        # print(digits)
        if len(digits) > 0:
            print('digits', (digits[0] + digits[-1]))
            sum = sum + int(digits[0] + digits[-1])
    return sum

def map_regext_to_number(regex_list):
    regex_mapper = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    rlist = [str(regex_mapper.get(item, item)) for item in regex_list]
    # print('rList', rlist, rlist[0], rlist[-1])
    return rlist


class TestCalibration(unittest.TestCase):
    def test_sum_test_value(self):
        text_test = load_text_from_file('input_test.txt')
        sum_test = calibration(text_test)
        self.assertEqual(sum_test, 281)
        print('Test', sum_test)

    def test_sum_value(self):
        text = load_text_from_file('input.txt')
        sum = calibration(text)
        self.assertEqual(sum, 55701)
        print('Input', sum)

if __name__ == '__main__':
    unittest.main()
