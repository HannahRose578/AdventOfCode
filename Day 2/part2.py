import re

# Function to parse the input string into a structured format
def parse_input(input_data):
    games = {}
    lines = input_data.strip().split('\n')
    pattern = r"Game (\d+): (.+)"

    for line in lines:
        match = re.match(pattern, line)
        if match:
            game_id = int(match.group(1))
            subsets = match.group(2).split('; ')
            games[game_id] = []

            for subset in subsets:
                cubes = re.findall(r'(\d+) (red|green|blue)', subset)
                for count, color in cubes:
                    games[game_id].append((color, int(count)))

    return games

# Function to find the minimum set of cubes for each game and calculate its power
def find_min_set_and_power(game_data):
    min_set = {"red": 0, "green": 0, "blue": 0}

    for color, count in game_data:
        min_set[color] = max(min_set[color], count)

    power = min_set["red"] * min_set["green"] * min_set["blue"]
    return power

# Main function to process the input file and solve the puzzle
def solve_puzzle_part_two(input_file):
    with open(input_file, 'r') as file:
        input_data = file.read()

    games_data = parse_input(input_data)
    
    # Summing the powers of the minimum sets of all games
    sum_of_powers = sum(find_min_set_and_power(game_data) for game_data in games_data.values())
    return sum_of_powers

# Path to the input file
input_file_path = 'input2.txt'

# Solve the puzzle for Part Two
result_part_two = solve_puzzle_part_two(input_file_path)
print(f"The sum of the power of the minimum sets is: {result_part_two}")
