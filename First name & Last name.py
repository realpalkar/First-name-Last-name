def print_full_name(first, last):
    print('Hello ' + first + ' ' + last + '!' + ' You just delved into python.')


if __name__ == '__main__':
    first_name = input('enter first name: ')
    last_name = input('enter last name: ')
    print_full_name(first_name, last_name)