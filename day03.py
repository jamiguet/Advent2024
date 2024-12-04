import re

if __name__ == '__main__':
    with open('data/day03.txt') as f:
        total = 0
        compute = True
        for line in f.readlines():
            line = line.strip()
            params = re.findall("mul\(([0-9]*),([0-9]*)\)|(do\(\))|(don't\(\))",line)
            for pair in params:
                print(f"Debug: {pair} -> {compute}")
                if compute:
                    try:
                        total += int(pair[1]) * int(pair[0])
                    except ValueError as ve:
                        print("skip")
                if "don't()" in pair:
                    compute = False
                if "do()" in pair:
                    compute = True

        print(f"Total: {total}")