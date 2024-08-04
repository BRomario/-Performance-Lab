import sys


def load_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = list(map(int, file.read().split()))
    return numbers


def min_moves_to_equal(numbers):
    numbers.sort()
    n = len(numbers)
    median = numbers[n // 2]
    moves = sum(abs(num - median) for num in numbers)
    return moves


def main(file_path):
    numbers = load_numbers_from_file(file_path)
    moves = min_moves_to_equal(numbers)
    print(moves)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python task4.py numbers.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
