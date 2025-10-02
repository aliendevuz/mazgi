

def beginning_maze():
    a = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', '*', '=', 'o', ' '],
        [' ', ' ', ' ', '=', ' '],
        [' ', '#', '=', 'o', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    b = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', 'o', '=', '=', ' '],
        [' ', ' ', ' ', '=', ' '],
        [' ', 'o', '=', '=', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    return a, b

def intermediate_maze():
    a = []
    b = []
    return a, b

def advanced_maze():
    a = []
    b = []
    return a, b

def sample_maze():
    a = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ]
    b = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ]
    return a, b

def generate_maze(width, height):
    a = [[1 for _ in range(width)] for _ in range(height)]
    b = [[1 for _ in range(width)] for _ in range(height)]
    return a, b
