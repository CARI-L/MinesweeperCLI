from random import randint
from enum import Enum

class State(Enum):
    COVERED = 0
    UNCOVERED = 1
    FLAGGED = 2

class Plot:
    def __init__(self):
        self.state = State.COVERED
        # self.state = State.UNCOVERED
        self.value = 0

    def __str__(self):
        if self.state == State.COVERED: return "■"
        if self.state == State.FLAGGED: return "⚑"
        if self.state == State.UNCOVERED:
            if self.value == 0: return " "
            if self.value == 9: return "☠"
            if self.value < 10: return str(self.value) 
            if self.value == 10: return "🙠"
            if self.value == 11: return "੬"
            if self.value == 12: return "🙢"
            if self.value == 13: return "☙"
            if self.value == 14: return "❀"
            if self.value == 15: return "❧"
            if self.value == 16: return "🙡"
            if self.value == 17: return "੩"
            if self.value == 18: return "🙣"
        return str(" ")

    def __repr__(self):
        return self.__str__()

class Board:
    def __init__(self, count: int, length: int, width: int = None):
        # allow a single-dimension constructor for square boards
        if width is None: width = length

        if length <= 0 or width <= 0 or length >= 100 or width >= 100:
            raise ValueError("Board dimensions out of bounds")
        if count <= 0 or count >= 0.31 *length * width:
            raise ValueError("Invalid mine count for board size")

        self.length = length
        self.width = width
        self.field = [[Plot() for _ in range(length)] for _ in range(width)]

        while count > 0:
            target = self.field[randint(0, width - 1)][randint(0, length - 1)]
            if target.value != 9:
                target.value = 9
                count -= 1

        for i in range(self.width):
            for j in range(self.length):
                if self.field[i][j].value == 9:
                    adjacent_positions = {(i + 1, j), (i - 1, j), (i, j + 1), 
                                          (i, j - 1), (i + 1, j + 1), (i + 1, j - 1),
                                          (i - 1, j + 1), (i - 1, j - 1)}
                    for y, x in adjacent_positions:
                        if 0 <= y < self.width and 0 <= x < self.length:
                            if self.field[y][x].value != 9: self.field[y][x].value += 1
                    
    def __str__(self):
        result = ""
        for i in range(self.width):
            for j in range(self.length):
                if j == 0:
                    if (self.width - i) >= 10: result += f"{self.width - i}  |"
                    else: result += f"{self.width - i}   |"
                result += f" {self.field[i][j]} |"
            result += "\n"
            if i != self.width - 1:
                result += "    "
                for j in range(self.length * 4 + 1): 
                    result += "-"
                result += "\n"
        result += "\n     "
        for i in range(1, self.length + 1):
            if i >= 10: result += f" {i} "
            else: result += f" {i}  "
        return result

    def flag(self, x: int, y: int):
        if not (0 <= y < self.width and 0 <= x < self.length):
            raise ValueError("Coordinates out of bounds")
        plot = self.field[y][x]
        if plot.state == State.COVERED: plot.state = State.FLAGGED
        elif plot.state == State.FLAGGED: plot.state = State.COVERED
 
    def dig(self, x: int, y: int) -> bool:
        if not self.digHelper(x, y): return False
        for i in range(self.width):
            for j in range(self.length):
                plot = self.field[i][j]
                if plot.state == State.UNCOVERED and plot.value == 0:
                    adjacent_positions = {(i + 1, j), (i - 1, j), (i, j + 1), 
                                          (i, j - 1), (i + 1, j + 1), (i + 1, j - 1),
                                          (i - 1, j + 1), (i - 1, j - 1)}
                    for new_y, new_x in adjacent_positions:
                        if 0 <= new_y < self.width and 0 <= new_x < self.length:
                            self.digHelper(new_x, new_y)
        return True
    
    def digHelper(self, x: int, y: int) -> bool:
        if not (0 <= y < self.width and 0 <= x < self.length):
            raise ValueError("Coordinates out of bounds")
        plot = self.field[y][x]
        if plot.state == State.UNCOVERED or plot.state == State.FLAGGED: return True
        else:
            plot.state = State.UNCOVERED
            if plot.value == 9: return False
            else:
                adjacent_positions = {(x, y), (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)}
                for new_x, new_y in adjacent_positions:
                    if 0 <= new_y < self.width and 0 <= new_x < self.length:
                        if self.field[new_y][new_x].value == 0: 
                            self.digHelper(new_x, new_y)
            return True
   
    def win(self) -> bool:
        mines = []
        for i in range(self.width):
            for j in range(self.length):
                plot = self.field[i][j]
                if plot.value == 9: mines.append((i, j))
                elif plot.state != State.UNCOVERED:
                    return False
        values = range(0, 9)
        for i, j in mines:
            positions = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                         (i, j - 1), (i, j), (i, j + 1),
                         (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
            for value in values:
                y = positions[value][0]
                x = positions[value][1]
                if 0 <= y < self.width and 0 <= x < self.length:
                    self.field[y][x].state = State.UNCOVERED
                    self.field[y][x].value = value + 10
        return True
