import re
solution_input = open("./data-1.txt", "r").read()

def process_1(input):
    numbers = []
    for line in input.strip().splitlines():
        digits = []
        for number in line:
            if number.isdigit():
                digits.append(number)
        numbers.append(int(digits[0] + digits[-1]))
    return sum(numbers)


def process_2(input):
    regex = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    replacement_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    pattern = re.compile(regex)

    numbers = []
    digits = []
    for line in input.strip().splitlines():
        for item in pattern.findall(line):
            if item.isdigit():
                digits.append(item)
            else:
                digits.append(replacement_dict[item])
        numbers.append(int(digits[0] + digits[-1]))
        digits = [] # tbh it probably could be improved, but I currently have no idea how
    return sum(numbers)


if __name__ == "__main__":
    print(f'part 1 solution: {process_1(solution_input)}')
    print(f'part 2 solution: {process_2(solution_input)}')
