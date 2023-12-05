

def extract_points(f):
    total_points = 0
    for line in f.readlines():
        correct_number = 0
        points = 0
        card = line.split(":")
        numbers = card[1].split("|")


        numbers[0] = numbers[0].strip()
        numbers[1] = numbers[1].strip()

        winning_numbers = numbers[0].split(" ")
        drawn_number = numbers[1].split(" ")

        i = 0
        for num in winning_numbers:
            if num == "":
                winning_numbers.pop(i)
            i += 1

        i = 0
        for num in drawn_number:
            if num == "":
                drawn_number.pop(i)
            i += 1



        for dnumber in drawn_number:
            if dnumber in winning_numbers:
                correct_number += 1

        if correct_number > 0:
            points = 2**(correct_number-1)

        total_points += points

    print(total_points)














def main():
    f = open('res/Day4_text.txt')
    extract_points(f)



if __name__ == "__main__":
    main()
