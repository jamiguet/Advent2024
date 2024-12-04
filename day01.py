
def list_to_map(vect):
    result = dict()
    for v in vect:
        if v not in result:
            result[v] = 1
        else:
            result[v] += 1

    return result


if __name__ == "__main__":
    left = list()
    right = list()
    with open("data/day01.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            left.append(int(line.split()[0]))
            right.append(int(line.split()[1]))
    left = sorted(left)
    right = sorted(right)
    print(f"lc1: {len(left)}, lc2: {len(right)}")
    total_distance = 0
    for i in range(len(left)):
        total_distance += abs(left[i] - right[i])

    print(f"Distance: {total_distance}")

    similarity = 0
    right_map = list_to_map(right)
    for r in left:
        freq = 0
        if r in right_map:
            freq = right_map[r]
        similarity += r * freq

    print(f"Similarity: {similarity}")

