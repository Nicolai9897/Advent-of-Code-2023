def extract_points(line):
    correct_number = 0
    card = line.split(":")
    numbers = card[1].split("|")

    drawn_numbers = _format_string(numbers[0])
    winning_numbers = _format_string(numbers[1])

    for dnumber in drawn_numbers:
        if dnumber in winning_numbers:
            correct_number += 1
    return correct_number

def _format_string(arr):
    arr = str(arr).strip()
    arr = arr.split(" ")

    while "" in arr:
        arr.remove("")

    return arr

def start_calc():
    lines = []
    f = open('res/Day4_text.txt')

    for line in f.readlines():
        lines.append([[len(lines)+1, 1], line])

    total_cards = 0
    for line in lines:
        # line[0][0] Game number
        # line[0][1] Poeng
        line_points = extract_points(line[1])

        for i in range(line_points):
            lines[line[0][0] + i][0][1] += line[0][1]
        total_cards += line[0][1]

    print(total_cards)

def main():
    start_calc()

if __name__ == "__main__":
    main()
