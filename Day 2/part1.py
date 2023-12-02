import re

# Function to parse the input string into a structured format
def parse_input(input_data):
    games = {}
    # Each line represents a game
    lines = input_data.strip().split('\n')
    pattern = r"Game (\d+): (.+)"

    for line in lines:
        match = re.match(pattern, line)
        if match:
            game_id = int(match.group(1))
            subsets = match.group(2).split('; ')
            games[game_id] = []

            # Extracting the number of cubes of each color in each subset
            for subset in subsets:
                cubes = re.findall(r'(\d+) (red|green|blue)', subset)
                for count, color in cubes:
                    games[game_id].append((color, int(count)))

    return games

# Function to check if a game is possible given the cube limits
def is_game_possible(game_data, limits):
    max_cubes = {"red": 0, "green": 0, "blue": 0}
    
    for color, count in game_data:
        max_cubes[color] = max(max_cubes[color], count)

    # Compare with the limits
    for color, limit in limits.items():
        if max_cubes[color] > limit:
            return False
    return True

# Main function to process the input file and solve the puzzle
def solve_puzzle(input_file):
    # Reading the input file
    with open(input_file, 'r') as file:
        input_data = file.read()

    # Parsing the input data
    games_data = parse_input(input_data)
    limits = {"red": 12, "green": 13, "blue": 14}

    # Determining the sum of IDs of possible games
    sum_of_ids = sum(game_id for game_id, game_data in games_data.items() if is_game_possible(game_data, limits))
    return sum_of_ids

# Path to the input file
input_file_path = 'input2.txt'

# Solve the puzzle
result = solve_puzzle(input_file_path)
print(f"The sum of the IDs of the possible games is: {result}")
