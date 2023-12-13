import re

bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def load_text_from_file(filename):
    """Load text from a given file and return its content."""
    with open(filename, 'r') as file:
        return file.read()

def is_color_possible(game, color):  
    regex = r"\d+ {}".format(color)
    occurrences = re.findall(regex, game)
    if len(occurrences) == 0:
        return False
    for occurrence in occurrences:
        if bag[color] < int(occurrence.split(' ')[0]):
            return False
    return True

def check_games(input):

    games = load_text_from_file(input)
    games_list = games.split('\n')

    sum = 0
    possible_games = []
    for id, game in enumerate(games_list):
        r = is_color_possible(game, 'red')
        g = is_color_possible(game, 'green')
        b = is_color_possible(game, 'blue')

        if r and g and b:
            possible_games.append(id + 1)
            sum += id+1

    print(possible_games)

    print(sum)
if __name__ =='__main__':
    check_games('input_test.txt')  
    check_games('input.txt')  
