def slicer(board, start, vector):
    result = list()
    for idx in range(len(vector)):
        idx_l = start[0] + vector[idx][0]
        idx_c = start[1] + vector[idx][1]
        if 0 <= idx_l < len(board) and 0 <= idx_c < len(board[0]) and board[idx_l][idx_c] in ("M", "S"):
            result.append(board[idx_l][idx_c])
        else:
            return result
    return "".join(result)

def find_xmas(board, start):
    target = "MS"
    checker = (target, "".join(list(reversed(target))))
    dir1 = ((1, 1), (-1, -1))
    dir2 = ((-1, 1), (1, -1))
    slc1 = slicer(board, start, dir1)
    slc2 = slicer(board, start, dir2)
    if board[start[0]][start[1]] == "A" and slc1 in checker and slc2 in checker:
        return 1
    return 0

if __name__ == '__main__':
    with open('data/day04.txt') as f:
        lines = list(map(lambda l: l.strip(), f.readlines()))
        count = 0
        for si in range(len(lines)):
            for sj in range(len(lines[0])):
                count += find_xmas(lines, (si,sj))

        print(f"Total: {count}")