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

for j in range(len(arr)):
    print(arr[j])


def check_numbers():
    sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j][0] != "." and not arr[i][j][0].isdigit():
                sum += check_char(i-1, j)
                sum += check_char(i - 1, j - 1)  # Over til venstre
                sum += check_char(i, j - 1)  # Til venstre
                sum += check_char(i + 1, j - 1)  # Under til venstre
                sum += check_char(i + 1, j)  # Under
                sum += check_char(i + 1, j + 1)  # Under til høyre
                sum += check_char(i, j + 1)  # Til høyre
                sum += check_char(i - 1,j + 1)  # Over til høyre
                sum += check_char(i,j)  # Punktet selv
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