f = open('res/Day3_text.txt')

arr = []
for line in f.readlines():
    line = line.strip()
    tmp_arr = []
    tmp_arr.append([".", False])
    for char in line:
        tmp_arr.append([char, False])
    tmp_arr.append([".", False])

    arr.append(tmp_arr)


def check_numbers():
    sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j][0] == "*":
                temp_numbers = []
                temp_numbers.append(check_char(i-1, j))
                temp_numbers.append(check_char(i - 1, j - 1))  # Over til venstre
                temp_numbers.append(check_char(i, j - 1))  # Til venstre
                temp_numbers.append(check_char(i + 1, j - 1))  # Under til venstre
                temp_numbers.append(check_char(i + 1, j))  # Under
                temp_numbers.append(check_char(i + 1, j + 1))  # Under til høyre
                temp_numbers.append(check_char(i, j + 1))  # Til høyre
                temp_numbers.append(check_char(i - 1, j + 1))  # Over til høyre
                temp_numbers.append(check_char(i, j))  # Punktet selv

                sup = []
                for num in temp_numbers:
                    if num != 0:
                        sup.append(num)
                print(sup)




                if len(sup) == 2:
                    temp_sum = sup[0] * sup[1]
                    sum += temp_sum
    print(sum)


def check_char(i, j):
    if arr[i][j][0].isdigit() and arr[i][j][1] is False:
        number = get_number(i, j)
        return number
    return 0

def get_number(i, j):
    number = ""
    while arr[i][j-1][0].isdigit():
        j -= 1
    while arr[i][j+1][0].isdigit():
        number += arr[i][j][0]
        arr[i][j][1] = True
        j += 1
    number += arr[i][j][0]
    arr[i][j][1] = True

    return int(number)


def main():
    check_numbers()

if __name__ == "__main__":
    main()