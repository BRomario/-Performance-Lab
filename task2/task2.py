import sys


def read_circle(file_path):
    with open(file_path, 'r') as file:
        line1 = file.readline().strip()
        x, y = map(float, line1.split())
        line2 = file.readline().strip()
        radius = float(line2)
        return x, y, radius


def read_dots(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.split())
            points.append((x, y))
    return points


def point_position(circle, point):
    center_x, center_y, radius = circle
    point_x, point_y = point

    distance_squared = (point_x - center_x) ** 2 + (point_y - center_y) ** 2
    radius_squared = radius ** 2

    if distance_squared < radius_squared:
        return 1
    elif distance_squared == radius_squared:
        return 0
    else:
        return 2


def main(circle_file, dots_file):
    circle = read_circle(circle_file)
    points = read_dots(dots_file)

    for point in points:
        position = point_position(circle, point)
        print(position)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("python task2.py circle.txt dot.txt")
        sys.exit(1)

    circle_file = sys.argv[1]
    dots_file = sys.argv[2]
    main(circle_file, dots_file)

# python task2.py circle.txt dot.txt
