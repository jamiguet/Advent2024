import numpy as np

def find_xmas(board, start, vector):
    target = "XMAS"
    pos = start
    for idx in range(len(target)):
        if  (0 <= pos[0] < len(board)
                and 0 <= pos[1] < len(board[0])
                and board[pos[0]][pos[1]] == target[idx]):
            pos = (pos[0] + vector[0], pos[1] + vector[1])
        else:
            return 0
    return 1



if __name__ == '__main__':
    with open('data/day04.txt') as f:
        lines = list(map(lambda l: l.strip(), f.readlines()))
        count = 0
        directions = ((0, 1),(-1, 0),(0,-1),(1,0), (1,1), (-1,-1), (-1,1), (1,-1))
        for vect in directions:
            for si in range(len(lines)):
                for sj in range(len(lines[0])):
                 count += find_xmas(lines, (si,sj), vect)

        print(f"Total: {count}")