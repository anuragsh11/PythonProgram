import fileinput


def main():
    t = [line for line in fileinput.input()]
    t = list(map(lambda s: s.strip(), t))
    length = int(t[0])
    Stud_lis = [int(x) for x in t[1].split()]
    print(Stud_lis)
    lis1 = []
    for i in range(length):
        sub = length - i
        if sub not in Stud_lis:
            lis1.append(sub)
    lis1 = sorted(lis1)
    print(' '.join(str(x) for x in lis1))


# Write code here

main()
