import os


def load_file(filename):
    print('Loading the journal...')
    data = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            for entry in f.readlines():
                data.append(entry.rstrip())
    return data


def check_file(filename):
    if os.path.getsize(filename) > 0:
        return True
    return False


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


def main():
    command = 'z'
    data = load_file('journal.txt')
    while command != 'x':
        command = input('What do you want to do? [L]ist, [A]dd or E[x]it ').lower()
        if command == 'l':
            list_entries(data)
        elif command == 'a':
            entry = input('Enter your journal entry: ')
            data = add_entries(data, entry)
        elif command == 'x':
            print('Saving journal...')
            save(data)
            print('Exit journal')


if __name__ == '__main__':
    main()
