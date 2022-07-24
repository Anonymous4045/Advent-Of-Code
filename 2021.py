# Advent of Code 2021 code solutions

with open('input.txt') as file:
    main_input = file.read().splitlines()
with open('test_input.txt') as file:
    test_input = file.read().splitlines()


def part1(l):
    return sum([l[i]<l[i+1]for i in range(len(l)-1)])


def part2(l):
    l = [int(i) for i in l]
    new_list = [sum([l[i], l[i+1], l[i+2]]) for i in range(len(l) - 2)]
    return part1(new_list)


def part3(data):
    h = v = 0
    for i in data:
        k = int(i[-1])
        if i[0] == 'f':
            h += k
        elif i[0] == 'd':
            v += k
        elif i[0] == 'u':
            v -= k

    return h * v


def part4(data):
    h_pos = depth = aim = 0
    for instruction in data:
        l = instruction[0]
        x = int(instruction[-1])
        if l == 'd':
            aim += x
        if l == 'u':
            aim -= x
        if l == 'f':
            h_pos += x
            depth += aim * x

    return h_pos * depth


def part5(data):
    b = [[],[],[],[],[],[],[],[],[],[],[],[]]
    for e in data:
        for i,a in enumerate(e):
            b[i].append(a)
    g=''.join([__import__('collections').Counter(q).most_common()[0][0]for i,q in enumerate(b)])
    e=''.join([{'1':'0','0':'1'}[i]for i in g])
    return int(g, 2)*int(e, 2)


def part6(data):
    ...


if __name__ == '__main__':
    result = part6(test_input)
    print(result)
