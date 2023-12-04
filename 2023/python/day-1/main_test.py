import main

solution_input = open("./data-1.txt", "r").read()

test_input_1 = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

test_input_2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

def test_process_1_test_data():
    assert main.process_1(test_input_1) == 142


def test_process_2_test_data():
    assert main.process_2(test_input_2) == 281

def test_process_1_solution():
    assert main.process_1(solution_input) == 54573


def test_process_2_solution():
    assert main.process_2(solution_input) == 54591
