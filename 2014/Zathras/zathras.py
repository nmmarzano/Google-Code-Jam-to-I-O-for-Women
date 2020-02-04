import math


DATA_FILE = './zathras_input.txt'


def get_input(file_name):
    file = open(file_name, 'r')
    lines = file.read().split('\n')
    file.close()
    result = lines[1:int(lines[0])+1]
    return [[int(x) for x in line.split(' ')] for line in result]


def simulate(a, b, alfa, beta, y):
    last_a = a
    last_b = b
    for x in range(y):
        # Day 1: Great Decision
        reproductive_pairs = min(a, b)
        decomissioned_a = math.floor(a * 0.01)
        decomissioned_b = math.floor(b * 0.01)
        
        # Day 2: Reproduction
        offspring = math.floor(reproductive_pairs * 0.02)
        new_a = math.floor(offspring * alfa / 100)
        new_b = math.floor(offspring * beta / 100)
        remainder = offspring - new_a - new_b
        a += new_a + remainder // 2
        b += new_b + remainder // 2 + remainder % 2
        
        # Day 3: Decomissioning
        a -= decomissioned_a
        b -= decomissioned_b

        # Check for stable value to break early
        # Problem hints towards this and it does indeed work on large datasets
        if last_a == a and last_b == b:
            break
        last_a = a
        last_b = b
        
    return [a, b]


if __name__ == '__main__':
    for index, data in enumerate(get_input(DATA_FILE)):
        result = simulate(data[0], data[1], data[2], data[3], data[4])
        print(f'Case #{index}: {result[0]} {result[1]}')
