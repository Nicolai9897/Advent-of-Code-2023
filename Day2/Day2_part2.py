max_cubes = {
    "blue" : 14,
    "red" : 12,
    "green" : 13
}
min_cubes = {
    "blue" : 1,
    "red" : 1,
    "green" : 1
}


def calculate(f):


    sum_of_powers = 0
    for line in f.readlines():
        current_sum_of_powers = 1
        valid_draw = True
        draws = []
        _reset_min_cuber()

        game = line.split(":")

        game_draw = _new_line_formatter(game)
        for draw in game_draw:
            draws += draw.split(",")

        for draw in draws:
            if(valid_draw):
                valid_draw = _check_max_cubes(draw)

        print(min_cubes)

        for cube in min_cubes:
            current_sum_of_powers *= min_cubes.get(cube)
            print(current_sum_of_powers)
        sum_of_powers += current_sum_of_powers
        print(f"sum: {sum_of_powers}")


    return sum_of_powers

def _reset_min_cuber():
    min_cubes["blue"] = 1
    min_cubes["red"] = 1
    min_cubes["green"] = 1

def _check_max_cubes(draw):
    for cube_color in max_cubes:
        if cube_color in draw:
            blue_draw = int(draw.strip(cube_color).strip())
            print(draw)
            print(min_cubes)
            if min_cubes.get(cube_color) < blue_draw:
                min_cubes[cube_color] = blue_draw
            print(min_cubes)
    return True


def _new_line_formatter(game):
    game_draw = game[1].split(";")
    game_draw[-1] = game_draw[-1].strip("\n")
    return game_draw


def main():
    f = open('res/Day1_part1_file.txt')
    total_IDs = calculate(f)
    print(total_IDs)


if __name__ == "__main__":
    main()
