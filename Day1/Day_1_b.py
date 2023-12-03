f = open("res/Day_1_file.txt", "r")

string_digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def check_for_char_digit(string):
    if string in string_digits:
        return string_digits[string]
    else:
        return 0


def get_start_number(line):
    for char in range(0, len(line)):
        if line[char].isdigit():
            return line[char]
        if char > 1:
            string = line[(char - 2): char + 1]
            if string in string_digits:
                return string_digits[string]
        if char > 2:
            string = line[char - 3: char + 1]
            if string in string_digits:
                return string_digits[string]
        if char > 3:
            string = line[char - 4: char + 1]
            if string in string_digits:
                return string_digits[string]
    return 0


def get_last_number(line):
    for char in range(0, len(line)):
        char_number = len(line) - char - 1
        if line[char_number].isdigit():
            return line[char_number]
        if char > 1:
            string = line[char_number: char_number + 3]
            if string in string_digits:
                return string_digits[string]
        if char > 2:
            string = line[char_number: char_number + 4]
            if string in string_digits:
                return string_digits[string]
        if char > 3:
            string = line[char_number: char_number + 5]
            if string in string_digits:
                return string_digits[string]
    return 0


def calculate_total_number():
    total_number = 0
    for line in f.readlines():
        line = line.strip("\n")
        start_number = str(get_start_number(line))
        last_number = str(get_last_number(line))
        total_number += int(start_number + last_number)

    print(total_number)


def main():
    calculate_total_number()


if __name__ == "__main__":
    main()
