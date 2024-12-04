
def safe_with_dampen(report):
    if check_safe(report):
        return True

    for i in range(len(report)):
        temp = report.copy()
        # print(f"report: {report} -> {i}")
        temp.pop(i)
        if check_safe(temp):
            return True
    return False

def check_safe(report):
    prev = report[0]
    deltas = list()
    for i in range(1, len(report)):
        deltas.append(int(prev) - int(report[i]))
        prev = report[i]
    signs = list(map(lambda x: 1 if x > 0 else -1, deltas))
    same_sign = abs(sum(signs)) == len(deltas)
    deltas = list(map(lambda x: abs(x), deltas))
    min_delta = min(deltas)
    max_delta = max(deltas)
    is_safe = min_delta > 0 and max_delta <= 3 and same_sign
    # print(f"Deltas: {deltas} -> {min_delta}, {max_delta} -> {same_sign} -> T: {is_safe}")

    return is_safe


if __name__ == "__main__":
    with open("data/day02.txt") as f:
        lines = f.readlines()
        safe = 0
        for line in lines:
            line = line.strip()
            levels = line.split()
            if safe_with_dampen(levels):
                safe += 1
        print(f"Safe: {safe}")