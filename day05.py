from functools import cmp_to_key


def valid(pred, after, seq):
    for pos in range(0, len(seq)):
        prefix = seq[:pos]
        suffix = seq[pos+1:]
        # print(f"Debug: {seq} -> {prefix}; {seq[pos]} {suffix}")
        # print(f"P: {pred} -> A: {after}")
        if seq[pos] in pred.keys() or seq[pos] in after.keys():
            for pel in prefix:
               if seq[pos] not in pred.keys() or pel not in pred[seq[pos]]:
                   return False
            for sel in suffix:
                if seq[pos] not in after.keys() or sel not in after[seq[pos]]:
                    return False
    return True

def compare(x, y):
    if x in pred.keys() and y in pred[x]:
        return 1
    else:
        return -1


def fix(pred, after, seq):
    fixed = sorted(seq.copy(), key=cmp_to_key(compare))
    print(f"Debug: {seq} -> {fixed}")
    return fixed


if __name__ =="__main__":
    with open("data/day05.txt") as f:
        lines = f.readlines()
        pred = dict()
        after= dict()
        total_g = 0
        total_b = 0
        for line in lines:
            if "|" in line:
                # Dealing with prec list
                l_comps = line.strip().split("|")
                if l_comps[1] not in pred.keys():
                    pred[l_comps[1]] = list()
                pred[l_comps[1]].append(l_comps[0])
                if l_comps[0] not in after.keys():
                    after[l_comps[0]] = list()
                after[l_comps[0]].append(l_comps[1])
            elif "," in line:
                # dealing with instructions
                seq = line.strip().split(",")
                sol = valid(pred, after, seq)
                print(f"Debug: {seq} ->  {sol}")
                if sol:
                    total_g += int(seq[int(len(seq) / 2)])
                else:
                    fixed = fix(pred, after, seq)
                    total_b += int(fixed[int(len(fixed) / 2)])

        print(f"Total Good: {total_g}")
        print(f"Total Bad: {total_b}")