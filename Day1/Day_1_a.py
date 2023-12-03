import re
f = open("res/Day_1_file.txt", "r")

digits = ['1','2','3','4','5','6','7','8','9','0']

def check_for_numbers(string):
    if string in digits:
        return True


def get_start_number(line):
    for char in range(0, len(line)):
        if check_for_numbers(line[char]):
            return line[char]
    return 0

def get_last_number(line):
    for char in range(0, len(line)):
        char_number = len(line)  - char - 2
        if check_for_numbers(line[char_number]):
            return line[char_number]
    return 0


def calculate_total_number():
    total_number = 0
    for line in f.readlines():
        start_number = get_start_number(line)
        last_number = get_last_number(line)
        total_number += int(start_number + last_number)

    print(total_number)

def main():
    calculate_total_number()

if __name__ == "__main__":
    main()
