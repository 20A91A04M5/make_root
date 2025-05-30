# first code :- # first and last digt sum ## ("4nineeightseven2", 42)

def solve_trebuchet():
    calibration_sum = 0
    with open("input.txt", "r") as file: 
        for line in file:
            line = line.strip()
            first_digit = None
            last_digit = None
            for char in line:
                if char.isdigit():
                    first_digit = char
                    break
            for char in reversed(line):
                if char.isdigit():
                    last_digit = char
                    break
            if first_digit is not None and last_digit is not None:
                calibration_value = int(first_digit + last_digit)
                calibration_sum += calibration_value
    return calibration_sum

result = solve_trebuchet()
print(result)

############################################################
# if digit sum digit else letters to digit convert sum and all sum togethrt  ("xtwone3four", 24),
        # ("4nineeightseven2", 42),
#second sum :-
WORD_TO_DIGIT_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def get_combined_digits(line):
    positions = [
        (idx, digit)
        for word, digit in WORD_TO_DIGIT_MAP.items()
        for idx in range(len(line))
        if line.startswith(word, idx)
    ]
    positions.extend((idx, ch) for idx, ch in enumerate(line) if ch.isdigit())
    if not positions:
        return 0
    positions.sort(key=lambda x: x[0])
    first, last = positions[0][1], positions[-1][1]
    return int(first + last)
def sum_calibration_values(lines):
    sum = 0
    for line in lines:
        tmp = get_combined_digits(line.strip())
        sum += tmp
    return sum
def main():
    with open("./input.txt") as f:
        lines = f.readlines()
        print(sum_calibration_values(lines))
if __name__ == "__main__":
    # test_calibration_values()
    main()

#############################################################
## 3rd code :-

class CubeGameAnalyzer:
    def __init__(self, max_cubes):
        self.max_cubes = max_cubes
    def sum_of_possible_game_ids(self, games):
        sum_ids = 0
        for game in games:
            try:
                game_id, sequences = game.split(": ")
                if self._is_game_possible(sequences):
                    sum_ids += int(game_id.split()[1])
            except ValueError as e:
                print(f"Error processing game data: {e}")
        return sum_ids
    def _is_game_possible(self, game_sequence):
        sequences = game_sequence.split(";")
        for sequence in sequences:
            sequence = sequence.strip()
            if not self._is_sequence_possible(sequence):
                return False
        return True
    def _is_sequence_possible(self, sequence):
        cubes = sequence.split(",")
        for cube in cubes:
            count, color = cube.strip().split()
            if int(count) > self.max_cubes[color]:
                return False
        return True
def main():
    with open("./input2.txt") as f:
        games = f.readlines()
    max_cubes = {"red": 12, "green": 13, "blue": 14}
    analyzer = CubeGameAnalyzer(max_cubes)
    print(analyzer.sum_of_possible_game_ids(games))
# def test_cube_game_analyzer():
#     games = [
#         "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#         "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#         "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#         "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#         "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
#     ]
#     max_cubes = {"red": 12, "green": 13, "blue": 14}
#     analyzer = CubeGameAnalyzer(max_cubes)
#     sum_of_ids = analyzer.sum_of_possible_game_ids(games)
#     assert sum_of_ids == 8, f"Test failed: Expected 8, got {sum_of_ids}"
#     print(f"Test passed: Sum of IDs is {sum_of_ids}")
if __name__ == "__main__":
    # run the test function
    # test_cube_game_analyzer()
    # execute the main function
    main() 
####################################
    
# --- Day 2: Cube Conundrum ---
# --- Part Two ---

from functools import reduce
from operator import mul
class CubeGameAnalyzer:
    def __init__(self, games, max_cubes=None):
        self.games = games
        self.max_cubes = max_cubes
    def sum_of_possible_game_ids(self):
        sum_ids = 0
        for game in self.games:
            try:
                game_id, sequences = game.split(": ")
                if self._is_game_possible(sequences):
                    sum_ids += int(game_id.split()[1])
            except ValueError as e:
                print(f"Error processing game data: {e}")
        return sum_ids
    def sum_of_power_of_games(self):
        sum_power_of_games = 0
        for game in self.games:
            game_sets = game.split(": ")[1].split("; ")
            min_cubes_required = {"red": 0, "green": 0, "blue": 0}
            for cubes in game_sets:
                for count, color in map(str.split, cubes.split(", ")):
                    min_cubes_required[color] = max(int(count), min_cubes_required[color])
            game_power = reduce(mul, min_cubes_required.values(), 1)
            sum_power_of_games += game_power
        return sum_power_of_games
    def _is_game_possible(self, game_sequence):
        sequences = game_sequence.split(";")
        for sequence in sequences:
            sequence = sequence.strip()
            if not self._is_sequence_possible(sequence):
                return False
        return True
    def _is_sequence_possible(self, sequence):
        cubes = sequence.split(",")
        for cube in cubes:
            count, color = cube.strip().split()
            if int(count) > self.max_cubes[color]:
                return False
        return True
def main():
    with open("input2.txt") as f:
        games = f.readlines()
    analyzer = CubeGameAnalyzer(games)
    print(analyzer.sum_of_power_of_games())
# def test_cube_game_analyzer():
#     games = [
#         "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#         "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#         "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#         "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#         "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
#     ]
#     analyzer = CubeGameAnalyzer(games)
#     sum_of_power_of_games = analyzer.sum_of_power_of_games()
#     assert (
#         sum_of_power_of_games == 2286
#     ), f"Test failed: Expected 2286, got {sum_of_power_of_games}"
#     print(f"Test passed: Sum of Power of Games is {sum_of_power_of_games}")
if __name__ == "__main__":
    # run the test function
    # test_cube_game_analyzer()
    main()
    
#################################################################

#5th code

# class EngineSchematicAnalyzer:
#     DIRECTIONS = [
#         (-1, -1), # Top-left
#         (-1, 0),  # Up
#         (-1, 1),  # Top-right
#         (0, -1),  # Left
#         (0, 1),   # Right
#         (1, -1),  # Bottom-left
#         (1, 0),   # Down
#         (1, 1)    # Bottom-right
#     ]
#     def __init__(self, schematic):
#         self.schematic = [list(line) for line in schematic.split('\n')]
#         self.processed_locations = set()
#     def is_valid_symbol(self, char):
#         return not (char.isdigit() or char == '.')
#     def is_adjacent_to_symbol(self, row, col):
#         for dx, dy in self.DIRECTIONS:
#             if 0 <= row + dx < len(self.schematic) and 0 <= col + dy < len(self.schematic[row + dx]):
#                 if self.is_valid_symbol(self.schematic[row + dx][col + dy]):
#                     return True
#         return False
#     def calculate_sum_of_part_numbers(self):
#         total_sum = 0
#         for i, row in enumerate(self.schematic):
#             j = 0
#             while j < len(row):
#                 if row[j].isdigit() and (i, j) not in self.processed_locations:
#                     number, init_j = row[j], j
#                     while j + 1 < len(row) and row[j + 1].isdigit():
#                         number += row[j + 1]
#                         j += 1                
#                     for col_index in range(init_j, j + 1):
#                         self.processed_locations.add((i, col_index))
#                         if self.is_adjacent_to_symbol(i, col_index):
#                             total_sum += int(number)
#                             break
#                 j += 1         
#         return total_sum
# def main():
#     with open("./input3.txt") as file:
#         engine_schematic = file.read()
#     analyzer = EngineSchematicAnalyzer(engine_schematic)
#     total_sum = analyzer.calculate_sum_of_part_numbers()
#     print(f"Sum of part numbers is {total_sum}")
# def test_sum_of_part_numbers():
#     engine_schematic = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# """
#     analyzer = EngineSchematicAnalyzer(engine_schematic)
#     calculated_sum = analyzer.calculate_sum_of_part_numbers()
#     assert calculated_sum == 4361, f"sum of part numbers is {calculated_sum}"
#     print("All tests passed successfully!")
# if __name__ == "__main__":
#     # test_sum_of_part_numbers()
#     main()