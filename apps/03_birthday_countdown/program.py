import datetime

print('---------------------------------------------------------------')
print('             BIRTHDAY APP')
print('---------------------------------------------------------------')
print()


def get_birthday():
    year = int(input('What year were you born [yyyy]? '))
    month = int(input('What month were you born [mm]? '))
    day = int(input('What day were you born [dd]? '))
    print()

    date = datetime.datetime(year, month, day)
    print('It looks like you were born on ' + date.strftime('%Y/%m/%d'))
    current_date = datetime.date.today()
    diff = current_date - datetime.date(current_date.year, month, day)
    return diff.days


def check_birthday(days):
    if days < 0:
        print('Your birthday is in {} days'.format(str(abs(days))))
        print('Hope you\'re looking forward to it!')
    elif days > 0:
        print('Your birthday was {} days ago. Hope you had fun!'.format(str(days)))
    else:
        print('Happy birthday!')


def main():
    days = get_birthday()
    check_birthday(days)


main()
