print('1. Enter your choise')
print('2. Search for a contact')
print('3. List all contacts')
print('4. Exit\n')
dct = {}
ls = []
x = None
while x != 4:
    x = int(input('Enter your choise: '))
    if x == 1:
        name = input('\nEnter your name: ')
        phone_number = input('Enter your phone number: ')
        ls.append({'name': name, 'phone': phone_number})
        print('\nContact added succesfully!\n')
    elif x == 2:
        search = input('\nEnter name: ')
        for person in ls:
            if search == person['name']:
                print(f'Phone number: {person["phone"]}')
                print()
    elif x == 3:
        print('\nContacts:\n')
        for person in ls:
            print(f'{person["name"]}: {person["phone"]}')
        print()
    elif x == 4:
        print('\nGoodbye!')