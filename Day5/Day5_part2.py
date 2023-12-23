f = open("res/Day5_text.txt")
lines = f.read()
lines = lines.split("\n\n")

def format_arr(num):
    """formats maps to make it into arrays which consists of only integers"""
    arr = lines[num]

    arr = arr.strip().split("\n")
    arr.pop(0)
    for i in range(len(arr)):
        arr[i] = arr[i].split(" ")
    return_arr = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = int(arr[i][j])

    for i in range(len(arr)):
        return_arr.append([])
        return_arr[i].append(arr[i][1])
        return_arr[i].append(arr[i][1] + (arr[i][2] - 1 ))
        return_arr[i].append(arr[i][0] - arr[i][1])
    return return_arr


def calculate_seed_list(seeds):
    """calculate an array with multiple arrays of eachs seeds first and last digits"""
    new_seed_list = []
    for i in range(len(seeds)):
        if i % 2 == 0:
            new_seed_list.append([])
            new_seed_list[i // 2].append(int(seeds[i]))
        else:
            new_seed_list[i//2].append((int(seeds[i-1]) + int(seeds[i])))
    return new_seed_list



def calculate_new_val(seed_arr, map_arr):
    """Splits the seed arrays into the ranges matching the arrays of the maps,
    and calculate the correct new value for each seed"""
    while True:
        temp_arr = []
        for j in range(len(map_arr)):
            for i in range(len(seed_arr)):
                # If both the lowest and highest number in the seed interval is in the map interval, provide new value
                if map_arr[j][0] <= seed_arr[i][0] <= map_arr[j][1] and map_arr[j][0] <= seed_arr[i][1] <= map_arr[j][1]:
                    temp_arr.append(get_new_val(map_arr[j], seed_arr[i]))
                    seed_arr[i] = [-1, -1]

                # If one of the numbers of the seed interval is in the map interval
                elif map_arr[j][0] <= seed_arr[i][0] <= map_arr[j][1] or map_arr[j][0] <= seed_arr[i][1] <= map_arr[j][1]:
                    # If the the seed intervals lowest numbers is outside of the map interval
                    if seed_arr[i][0] < map_arr[j][0]:
                        tmp = [map_arr[j][0], seed_arr[i][1]]
                        temp_arr.append(get_new_val(map_arr[j], tmp))

                        tmp = [seed_arr[i][0], map_arr[j][0] - 1]
                        seed_arr[i] = tmp

                    # If the highest number of the seed interval is outside of the map interval
                    elif seed_arr[i][1] > map_arr[j][1]:
                        tmp = [seed_arr[i][0], map_arr[j][1]]
                        temp_arr.append(get_new_val(map_arr[j], tmp))

                        tmp = [map_arr[j][1] + 1, seed_arr[i][1]]
                        seed_arr[i] = tmp

        if len(temp_arr) == 0 :
            return seed_arr

        for i in range(len(seed_arr)):
            if seed_arr[i] != [-1, -1]:
                temp_arr.append(seed_arr[i])

        return temp_arr

def get_new_val(map_arr, seed_arr):
    increment_value = map_arr[2]
    tmp = [seed_arr[0] + increment_value, seed_arr[1] + increment_value]
    return tmp

def main():
    low_num = 0
    seeds = lines[0].strip("seeds: ").strip("\n").split(" ")
    seeds = calculate_seed_list(seeds)
    maps = []

    for i in range(1, 8):
        maps.append(format_arr(i))

    for arr in seeds:
        val = [arr]

        for i in range(len(maps)):
            val = calculate_new_val(val, maps[i])

        for seed in val:
            if low_num == 0 or seed[0] < low_num:
                low_num = seed[0]
    print(low_num)

if __name__ == "__main__":
    main()