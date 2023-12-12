import re
import unittest

def load_text_from_file(filename):
    """Load text from a given file and return its content."""
    with open(filename, 'r') as file:
        return file.read()
    
def calibration(text):
    splitted = text.split('\n')
    sum = 0
    for line in splitted:
        digits = re.findall('\d', line)
        print(digits)
        if len(digits) > 0:
            sum = sum + int(digits[0] + '' + digits[-1])
    return sum


class TestCalibration(unittest.TestCase):
    def test_sum_test_value(self):
        text_test = load_text_from_file('input_test.txt')
        sum_test = calibration(text_test)
        self.assertEqual(sum_test, 142)

    def test_sum_value(self):
        text = load_text_from_file('input.txt')
        sum = calibration(text)
        self.assertEqual(sum, 56397)

if __name__ == '__main__':
    unittest.main()
