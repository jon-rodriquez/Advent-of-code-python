from game import Game

# read file line by line


def readFile(filename):
    file = open(filename, 'r')
    sum = 0
    for line in file:
        game_id, input_string = line.split(": ")
        game_s, g_id = game_id.split(" ")
        g = Game(int(g_id), input_string)

        if g.is_valid_game():
            sum += g.get_id()


    print(sum)


def main():
    readFile("./input.txt")

if __name__ == "__main__":
    main()

