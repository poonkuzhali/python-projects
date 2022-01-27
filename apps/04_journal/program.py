import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print('------------------------------------------')
    print('         JOURNAL APP')
    print('------------------------------------------')


def run_event_loop():
    command = 'Empty'
    data = journal.load_file('journal.txt')
    print('What do you want to do with your journal?')
    while command != 'x' and command:
        command = input('[L]ist entries, [A]dd entry or E[x]it journal\n').lower()
        if command == 'l':
            journal.list_entries(data)
        elif command == 'a':
            entry = input('Enter your journal entry: ')
            data = journal.add_entries(data, entry)
        elif command != 'x':
            print('Wrong command. Try again!')

    print('Saving journal...')
    journal.save(data)
    print('Exit journal')


if __name__ == '__main__':
    main()
