f = open("res/Day_1_file.txt", "r")

def get_start_number(line):
    for char in range(0, len(line)):
        if line[char].isdigit():
            return line[char]
    return 0

def get_last_number(line):
    for char in range(0, len(line)):
        char_number = len(line)  - char - 1
        if line[char_number].isdigit():
            return line[char_number]
    return 0


def calculate_total_number():
    total_number = 0
    for line in f.readlines():
        line = line.strip("\n")
        start_number = get_start_number(line)
        last_number = get_last_number(line)
        total_number += int(start_number + last_number)

    print(total_number)


def main():
    calculate_total_number()

if __name__ == "__main__":
    main()
