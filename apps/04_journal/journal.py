import os


def load_file(filename):
    print('Loading the journal...')
    data = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            for entry in f.readlines():
                data.append(entry.rstrip())
    return data


def list_entries(data):
    count = len(data)
    print('You have {} entries.'.format(count))
    for i, entry in enumerate(data, 1):
        print(str(i) + '.', entry)


def add_entries(data, entry):
    data.append(entry)
    return data


def save(data):
    with open('journal.txt', 'w') as f:
        for entry in data:
            f.write(entry + '\n')
