f = open("res/DAy5_example.txt")
lines = f.read()
lines = lines.split("\n\n")




def format_arr(num):
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
        return_arr[i].append(arr[i][0]-arr[i][1])
    return return_arr

"""
def calculate_new_val(num, arr):
    num = int(num)
    for i in range(len(arr)):
        if arr[i][0] <= num <= arr[i][1]:
            num += arr[i][2]
            return num
    return num
"""

def calculate_new_val(seed_arr, map_arr):
    tmp = []
    bool = True
    tmp.append([])

    for seed in seed_arr:
        tmp[0].append(seed)
    seed_arr = tmp
    while bool:
        temp_arr = []
        for j in range(len(map_arr)):
            for i in range(len(seed_arr)):
                print("--------------------------------")
                print(map_arr)
                print(seed_arr)
                print(map_arr[j][0])
                print(seed_arr[i][0])
                print(map_arr[j][1])
                print(map_arr[j][0])
                print(seed_arr[i][1])
                print(map_arr[j][1])
                if map_arr[j][0] <= seed_arr[i][0] <= map_arr[j][1] and map_arr[j][0] <= seed_arr[i][1] <= map_arr[j][1]:
                    bool = True
                elif map_arr[j][0] <= seed_arr[i][0] <= map_arr[j][1] or map_arr[j][0] <= seed_arr[i][1] <= map_arr[j][1]:
                    if seed_arr[i][0] < map_arr[j][0]:
                        temp_arr.append([])
                        temp_arr[-1].append(seed_arr[i][0])
                        temp_arr[-1].append(map_arr[j][0] - 1)
                        temp_arr.append([])
                        temp_arr[-1].append(map_arr[j][0])
                        temp_arr[-1].append(seed_arr[i][1])
                    elif seed_arr[i][1] > map_arr[j][1]:
                        temp_arr.append([])
                        temp_arr[-1].append(map_arr[j][1] + 1)
                        temp_arr[-1].append(seed_arr[i][1])
                        temp_arr.append([])
                        temp_arr[-1].append(seed_arr[i][0])
                        temp_arr[-1].append(map_arr[j][1])
                    else:
                        temp_arr.append([])
                        temp_arr[-1].append(seed_arr[j][0])
                        temp_arr[-1].append(seed_arr[i][1])
        seed_arr = temp_arr


    for i in range(len(temp_arr)):
        for j in range(map_arr):
            if map_arr[j][0] <= temp_arr[i][0] <= map_arr[j][1] and map_arr[j][0] <= temp_arr[i][1] <= map_arr[j][1]:
                temp_arr[i][0] += map_arr[j][2]
                temp_arr[i][1] += map_arr[j][2]

    return temp_arr

    """
    for i in range(len(map_arr)):
        if map_arr[i][0] <= seed_arr <= map_arr[i][1]:
            seed_arr += map_arr[i][2]
            return seed_arr
    return seed_arr
    """



def calculate_seed_list(seeds):
    new_seed_list = []
    for i in range(len(seeds)):
        if i % 2 == 0:
            new_seed_list.append([])
            new_seed_list[i // 2].append(int(seeds[i]))
        else:
            new_seed_list[i//2].append((int(seeds[i-1]) + int(seeds[i])))
    return new_seed_list


def main():
    seeds = lines[0].strip("seeds: ").strip("\n").split(" ")
    print("")
    seeds = calculate_seed_list(seeds)
    seed_soil = format_arr(1)
    soil_fertilizer = format_arr(2)
    fertilizer_water = format_arr(3)
    water_light = format_arr(4)
    light_temperature = format_arr(5)
    temperature_humidity = format_arr(6)
    humidity_location = format_arr(7)

    #calculate_seed_list(seeds)

    #print(seed_soil)
    print(f"Number off seeds: {len(seeds)}")
    low_num = None
    tall = 0
    print(seeds)
    for val in seeds:
        tall += 1
        print(f"seed: {tall}    Seed number: {val}")
        val = calculate_new_val(val, seed_soil)
        val = calculate_new_val(val, soil_fertilizer)
        val = calculate_new_val(val, fertilizer_water)
        val = calculate_new_val(val, water_light)
        val = calculate_new_val(val, light_temperature)
        val = calculate_new_val(val, temperature_humidity)
        val = calculate_new_val(val, humidity_location)
        print(f"seed location: {val}")
        print("-------------")
        if low_num is None or low_num > val:
            low_num = val
    print(low_num)
    #for seed in seeds:




if __name__ == "__main__":
    main()