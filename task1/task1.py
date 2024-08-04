import sys


def circular_array_path(n, m):
    circular_array = list(range(1, n + 1))

    path = []
    index = 0

    while True:
        end_index = (index + m - 1) % n
        path.append(circular_array[index])
        index = end_index

        if index == 0:
            break

    return path


def main():
    if len(sys.argv) != 3:
        print("python task1.py <n> <m>")
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])
    result = circular_array_path(n, m)
    print(result)


if __name__ == "__main__":
    main()

# python task1.py 5 4