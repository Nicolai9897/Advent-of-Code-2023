f = open("res/Day5_text.txt")
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

def calculate_new_val(num, arr):
    num = int(num)
    for i in range(len(arr)):
        if arr[i][0] <= num <= arr[i][1]:
            num += arr[i][2]
            return num
    return num

def calculate_seed_list(seeds):
    new_seed_list = []
    for i in range(len(seeds)):
        print(f" {i} seeds of {len(seeds)}")
        if i % 2 != 0 and i < 18:
            for j in range(int(seeds[i])):
                new_seed_list.append(int(new_seed_list[i-1])+j)

        else:
            new_seed_list.append(int(seeds[i]))
    return new_seed_list

def main():
    seeds = lines[0].strip("seeds: ").strip("\n").split(" ")
    seeds = calculate_seed_list(seeds)
    seed_soil = format_arr(1)
    soil_fertilizer = format_arr(2)
    fertilizer_water = format_arr(3)
    water_light = format_arr(4)
    light_temperature = format_arr(5)
    temperature_humidity = format_arr(6)
    humidity_location = format_arr(7)


    print(f"Number off seeds: {len(seeds)}")
    low_num = None
    tall = 0
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