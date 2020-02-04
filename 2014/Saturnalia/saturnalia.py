DATA_FILE = './saturnalia_input.txt'


def decorate(text):
    horizontal_border = ''.join(['-' for c in range(len(text))])
    horizontal_border = '+-' + horizontal_border + '-+'
    middle_line = '| ' + text + ' |'
    return '{0}\n{1}\n{0}'.format(horizontal_border, middle_line)


def get_input(file_name):
    file = open(file_name, 'r')
    lines = file.read().split('\n')
    file.close()
    return lines[1:int(lines[0])+1]


if __name__ == '__main__':
    data = get_input(DATA_FILE)
    for index, line in enumerate(data):
        print(f'Case #{index}:')
        print(decorate(line))
