from secret_santa.selector import Selector


if __name__ == '__main__':
    print('Ho ho ho! Let\'s assign some santas!')
    print()

    selector: Selector = Selector()

    add_santa: bool = true
    while add_santa:
        name: str = input('Name: ')
        phone_number: str = input('Phone Number: ')
        selector.add_santa(name, phone_number)
        add_santa = input('Would you like to add another? (Y/n) ') == 'Y'
    print()

    print('Assigning and notifying santas...')
    selector.select_and_notify_santas()
    print()

    print('All done!')

