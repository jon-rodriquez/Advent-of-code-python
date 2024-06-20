class Game:
    __valid_game = {
            "red":12,
            "green": 13,
            "blue": 14
            }

    def __init__(self, id, text_input) -> None:
       self.id = id
       self.rounds = self.__parse_rounds(text_input)
    
    # sample input 
    # 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    # return [
    #        {"blue": 3, "red": 4},
    #        {"red": 1, "green": 2},
    #        { "blue": 6, "green": 2}
    #        ]
    def __parse_rounds(self, text_input):
        rounds = list()
        raw_rounds = text_input.split(";")

        for round in raw_rounds:
            color_counts = round.split(",")
            temp_map={}
            for color_count in color_counts:
                count, color = color_count.strip().split(" ") 
                temp_map[color] = int(count)

            rounds.append(temp_map)

        return rounds

    def get_id(self):
        return self.id 

    def is_valid_game(self):
        for round in self.rounds:
            for key, value in round.items():
                if value > self.__valid_game[key]:
                    return False


        return True
