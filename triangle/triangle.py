import sys


def get_lines_from_file(file_name):
    file = open(file_name)
    lines = file.readlines()
    file.close()
    return lines


def writeToFile(coordinates, file_name):
    file = open(file_name, "w")
    file.write(coordinates)
    file.close()


def getCoordinates(line):
    list_crd = list(map(int, line.strip('\n').split()))
    if len(list_crd) == 6:
        first_crd = Coordinate(list_crd[:2])
        second_crd = Coordinate(list_crd[2:4])
        third_crd = Coordinate(list_crd[4:])
    else:
        first_crd = Coordinate([0, 0])
        second_crd = Coordinate([0, 0])
        third_crd = Coordinate([0, 0])
    return first_crd, second_crd, third_crd


class Coordinate:
    def __init__(self, list_crd):
        self.X = int(list_crd[0])
        self.Y = int(list_crd[1])


class Length:
    def __init__(self, first_crd, second_crd):
        self.length = float((((first_crd.X - second_crd.X) ** 2)
                             + ((first_crd.Y - second_crd.Y) ** 2)) ** 0.5)


class Triangle:
    def __init__(self, coordinates):
        self.first_side = Length(coordinates[0], coordinates[1]).length
        self.second_side = Length(coordinates[0], coordinates[2]).length
        self.third_side = Length(coordinates[1], coordinates[2]).length

    def isTriangle(self):
        if self.first_side + self.second_side > self.third_side \
                and self.second_side + self.third_side > self.first_side \
                and self.first_side + self.third_side > self.second_side:
            return True
        return False

    def isIsosceles(self):
        if self.first_side == self.second_side \
                or self.second_side == self.third_side \
                or self.first_side == self.third_side:
            return True
        return False

    def isoscelesSquare(self):
        if self.isTriangle() and self.isIsosceles():
            p = (self.first_side + self.second_side + self.third_side) / 2
            square = (p * (p - self.first_side) * (p - self.second_side) * (p - self.third_side)) ** 0.5
            return square
        return 0


def main(data, result):
    lines = get_lines_from_file(data)
    max_square = 0
    coordinates = ''
    for i in range(len(lines)):
        triangle = Triangle(getCoordinates(lines[i]))
        square = triangle.isoscelesSquare()
        if square > max_square:
            max_square = square
            coordinates = lines[i]
    writeToFile(coordinates, result)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
