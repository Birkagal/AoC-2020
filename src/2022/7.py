''' 
Part One - Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
Part Two - Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?
'''


def read_filesystem(lines):
    fs = {'/': 0}
    current_path = []
    for line in lines:
        line = line.split(' ')
        if line[0] == '$':
            if line[1] == 'cd':
                if line[2] == '/':
                    current_path = []
                elif line[2] == '..':
                    current_path.pop()
                else:
                    current_path.append(line[2])
        elif line[0] != 'dir':
            add_filesize(int(line[0]), fs, current_path)
    return fs


def add_filesize(size, fs, current_path):
    path = '/'
    fs['/'] += size
    for dir in current_path:
        path += f'{dir}/'
        if path in fs:
            fs[path] += size
        else:
            fs[path] = size


def part_one(input):
    fs = read_filesystem(input)
    return sum([size for size in fs.values() if size <= 100000])


def part_two(input):
    fs = read_filesystem(input)
    system_size = fs.pop('/')
    return min([size for size in fs.values() if system_size - size <= 40000000])
