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

def minimum_cubes_nb(game, color):  
    regex = r"\d+ {}".format(color)
    occurrences = re.findall(regex, game)
    max = 0
    if len(occurrences) == 0:
        return 0
    for occurrence in occurrences:
        nb_of_cubes = int(occurrence.split(' ')[0])
        if nb_of_cubes > max:
            max = nb_of_cubes
    return max

def check_games(input):

    games = load_text_from_file(input)
    games_list = games.split('\n')

    sum = 0
    possible_games = []
    for id, game in enumerate(games_list):
        r = minimum_cubes_nb(game, 'red')
        g = minimum_cubes_nb(game, 'green')
        b = minimum_cubes_nb(game, 'blue')

        if r and g and b:
            possible_games.append([id+1,r,g,b])
            sum += r*g*b

    print(possible_games)

    print(sum)
if __name__ =='__main__':
    check_games('input_test.txt')  
    check_games('input.txt')  
