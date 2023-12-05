max_cubes = {
    "blue" : 14,
    "red" : 12,
    "green" : 13
}


def calculate(f):
    IDs_added = 0
    for line in f.readlines():
        valid_draw = True
        draws = []

        game = line.split(":")
        game_number = int(game[0].strip("Game").strip())

        game_draw = _new_line_formatter(game)
        for draw in game_draw:
            draws += draw.split(",")

        for draw in draws:
            if(valid_draw):
                valid_draw = _check_max_cubes(draw)

        if valid_draw:
            IDs_added += game_number
    return IDs_added

def _check_max_cubes(draw):
    for cube_color in max_cubes:
        if cube_color in draw:
            blue_draw = draw.strip(cube_color).strip()
            if int(blue_draw) > max_cubes.get(cube_color):
                return False
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
